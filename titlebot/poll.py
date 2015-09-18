#!/usr/bin/env python
import json
from os import environ
import sys
import os

f = environ.get("TITLEDB",'suggestions.json')
def load_db(f):
    try:
        with open(f) as fl:
            return json.load(fl)
    except:
        #default db is []
        return []

def save_db(f,db):
    with open(f,"w") as x:
        json.dump(db,x)

def title_in_db(t,d):
    for index,entry in enumerate(d):
        if t == entry['title']:
            print("Title is already in list.")
            print("To vote for this type '.up %d'" %index)
            return True
    return False

def sort_by_votes(db):
    return sorted(db,key=lambda entry:sum(entry['votes'].values()),reverse=True)

def clear():
    db = save_db(f,[])
    print("cleared database")

def down():
    print("not implemented")

def help():
    print( """BGT Title Poll Bot:
  .new TITLE              - suggest a new title
  .list <(age|votes)>     - list all suggestions
  .highest <NUM>          - lists the NUM highest voted suggestions
  .top <NUM>              - alias for .highest
  .up NUM (NUM ...)       - upvote one or more suggestions from .list
  .undo NUM (NUM ...)     - undo an upvote
  .clear                  - clear the poll (auth required)""")

def highest():
    title=" ".join(sys.argv[1:])
    db = load_db(f)
    # only print the last N values (default 1)
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    num =  0
    last_vote = 9001
    # stolen from http://stackoverflow.com/questions/9647202/ordinal-numbers-replacement
    suffixes = ["th", "st", "nd", "rd", ] + ["th"] * 16

    for entry in sort_by_votes(db):
        # if two entries have the same number of upvotes, do not increment the rank
        current_vote = sum(entry['votes'].values())
        if current_vote < last_vote:
            num = num + 1
        last_vote = current_vote
        # exit if we are above the limit
        if num > limit:
            sys.exit(0)

        suffixed_num = str(num) + suffixes[num % 100]
        print("%s: '%s' (%d votes)" %
                (suffixed_num,entry['title'],sum(entry['votes'].values())))
def list():
    db = load_db(f)
    if len(sys.argv) > 1 and ("-h" in sys.argv[1]  or "usage" == sys.argv[1]):
        print("""usage: list <(age|votes)>
        sort by age or by votes (default: age)
    """)
        sys.exit(0)

    if len(sys.argv) > 1 and ("votes" in sys.argv[1]):
        use = sort_by_votes(db)
    elif len(sys.argv) > 1 and ("age" in sys.argv[1]) or len(sys.argv) == 1:
        use = db
    else:
        print("unknown sorting method")
        sys.exit(1)

    for entry in use:
        print("#%d %s (votes: %d)" %
                (db.index(entry),entry['title'],sum(entry['votes'].values())))

def new():
    title=" ".join(sys.argv[1:])
    db = load_db(f)

    suggester = environ['_from']
    if not title_in_db(title,db):
        db.append( { 'by': suggester,
                    'votes':{},'title': title})
        print("Thank you for your suggestion '%s'!"%environ["_from"])
        print("To vote type '.up %d'"%(len(db)-1))
    save_db(f,db)

def undo():
    db = load_db(f)
    votes = []
    try:
        votes = sys.argv[1:]
    except:
        print("""usage: undo number (...)
        undos vote of one or more entries based on .list""")
        sys.exit(1)
    voter = environ['_prefix'].split("@")[1]
    voter_name = environ['_from']
    for vote in votes:
        try:
            vote = int(vote)
            if not voter in db[vote]['votes']:
                print("%s, you never voted for '%s'!"%(voter_name,db[vote]['title']))
            else:
                del(db[vote]['votes'][voter] )
                print("%s undid vote for '%s'" %(voter_name,db[vote]['title'] ))
        except:
            print("%s undo voting for #%d failed" %(voter_name,vote))

    save_db(f,db)

def up():
    db = load_db(f)
    votes = []
    votes = sys.argv[1:]
    if not votes:
        print("""usage: up number (...)
        upvotes one or more entries based on .list""")
        sys.exit(1)

    voter = environ['_prefix'].split("@")[1]
    voter_name =environ['_from']
    for vote in votes:
        try:
            vote = int(vote)
            if vote < 0:
                raise Exception()
            if voter in db[vote]['votes']:
                print("%s, you already have voted for '%s'"%(voter_name,db[vote]['title']) )
            else:
                db[vote]['votes'][voter] = 1
                print("%s voted for '%s'"%(voter_name,db[vote]['title']))
        except:
            print("%s, voting for #%s failed" %(voter_name,vote))

    save_db(f,db)
