#! python 3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip
import re


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-z0-9._%+-]+                   #username contained in char class
    @                                   # @ symbol
    [a-zA-z0-9._%+-]+                   #domain
    (\.[a-zA-Z]{2,4})                   #dot-something
    )''', re.VERBOSE)


# find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[0]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


# copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
