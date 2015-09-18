# reaktor-titlebot
Commands and config for the Binärgewitter Titlebot

# Usage

    $ export TITLEDB='/tmp/aids.json'
    $ export _from=bobob
    $ export _prefix=bob@bob.com

    $ help
    BGT Title Poll Bot:
      .new TITLE              - suggest a new title
      .list <(age|votes)>     - list all suggestions
      .highest <NUM>          - lists the NUM highest voted suggestions
      .top <NUM>              - alias for .highest
      .up NUM (NUM ...)       - upvote one or more suggestions from .list
      .undo NUM (NUM ...)     - undo an upvote
      .clear                  - clear the poll (auth required)
    $ new 'aids balls'
    Thank you for your suggestion 'bobob'!
    To vote type '.up 0'
    $ top
    1st: 'aids balls' (0 votes)
    up 0
    $ up 0
    bobob voted for 'aids balls'
    $ new 'herp-derp'
    $ top 3
    1st: 'aids balls' (1 votes)
    2nd: 'herp-derp' (0 votes)
    $ list
    #0 aids balls (votes: 1)
    #1 herp-derp (votes: 0)
