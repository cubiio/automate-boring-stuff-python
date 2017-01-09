#! Python 3
# Set-up of a new project

# [START imports]
import os
# [END imports]


# asks for the project name
def get_name():
    project_name = input('What is the name of the project?\n')
    return project_name


# create directories
def create_dir():
    project_name = get_name()
    os.makedirs('/Users/samatkins/projects/' + project_name)
    print(project_name + ' created')
    os.chdir('/Users/samatkins/projects/' + project_name)
    print('changing directory...')
    print('now in directory' + os.getcwd())
    os.makedirs('app/responsive')
    os.makedirs('app/images')
    os.makedirs('app/images_src')
    print('directories created!')


create_dir()
