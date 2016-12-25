#! /usr/bin/env python3
# pw.py - An insecure password locker program
# run in the command line e.g. $ p3 pw.py email

import sys
import pyperclip

passwords = {'email': 'password123',
             'blog': 'anotherStupidPassword',
             'luggage': '123456'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

# first command line arg is the acc name
account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print ('There is no account named ' + account)
