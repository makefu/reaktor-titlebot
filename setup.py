import sys
from setuptools import setup

setup(
    name='Reaktor-titlebot',
    version='2.1.0',

    description='Titlebot for Reaktor',
    long_description=open("README.md").read(),
    license='WTFPL',
    url='http://krebsco.de/',
    # download_url='https://pypi.python.org/pypi/Reaktor/',

    author='makefu',
    author_email='spam@krebsco.de',
    # install_requires = [ ],

    packages=['titlebot'],
    entry_points={
        'console_scripts' : [
            'clear = titlebot.poll:clear',
            'down = titlebot.poll:down',
            'help = titlebot.poll:help',
            'highest = titlebot.poll:highest',
            'top = titlebot.poll:highest',
            'list = titlebot.poll:list',
            'new = titlebot.poll:new',
            'undo = titlebot.poll:undo',
            'up = titlebot.poll:up'
            ]
        },

    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)

