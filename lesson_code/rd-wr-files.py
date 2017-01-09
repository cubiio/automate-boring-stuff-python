import os

# joins the path from arguments
os.path.join('usr', 'bin', 'spam')

# gets the current working directory
os.getcwd()

# change directory
os.chdir('/Users/samatkins/projects/automate-boring-stuff-python')

# make directory
os.makedirs('/Users/samatkins/projects/project-template')

# list dictory
os.listdir('/Users/samatkins/projects/automate-boring-stuff-python')

# returns a string of the absolute path of the argument
os.path.abspath('.')

# returns True if argument is an absolute path and False if a relative path
os.path.isabs('.')

# returns the relative path
os.path.relpath('/users/projects', '/automate-boring-stuff-python')
# output is: '../users/projects'

# returns the base path
path = '/users/projects/automate-boring-stuff-python/rd-wr-files.py'
os.path.basename(path)
# output is: 'rd-wr-files.py'
os.path.dirname(path)
# output is: '/users/projects/automate-boring-stuff-python'
os.path.split(path)
# output is: ('/users/projects/automate-boring-stuff-python', 'rd-wr-files.py')

# returns file size
calcFileSize = '/Users/samatkins/Documents/'
os.path.getsize(calcFileSize)

# adds path to list myFiles
myFiles = ['accounts.txt', 'cv.docx']
for filename in myFiles:
    print(os.path.join('usr/example/sam', filename))
