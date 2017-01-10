#! /usr/bin/env python3
# scaf_p.py - Scaffold a new project

# [START imports]
import os
from git import Repo
# [END imports]


projects = ["1", "2"]


# asks for project type
def get_p_type():
    p_type = input(
        'What type of project do you want to scaffold?\n'
        'Select\n1 (Front-End with Gulp)'
        '\n2 Front and Back End (coming soon!)\n')
    while p_type not in projects:
        p_type = input('Selection not recognised, please try again.')
    return p_type


# asks for the project name
def get_p_name():
    p_name = input('What is the name of the project?\n')
    return p_name


# creates front-end folder structure
def create_fe_dir(p_name):
    os.chdir('/Users/samatkins/projects/' + p_name)
    print('changing directory...')
    print('now in directory' + os.getcwd())
    os.makedirs('app/images_src')
    print('directories created!')


# git clone workflow front end with gulp
def clone_workflow(p_name):
    git_url = 'https://github.com/cubiio/workflow_frontend_gn.git'
    repo_dir = ('/Users/samatkins/projects/' + p_name)
    Repo.clone_from(git_url, repo_dir)
    print ('Git clone complete!')


def scaffold_p():
    p_type = get_p_type()
    p_name = get_p_name()
    if p_type == '1':
        clone_workflow(p_name)
        create_fe_dir(p_name)
    else:
        print ('Project scaffold coming soon, watch this space!')
    return


scaffold_p()
