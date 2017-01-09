#! /usr/bin/env python3
# deploy_hugo.py - Automate deploy new content to my blog powered by Hugo


# [START imports]
import sh
# [END imports]


# specify the local repo
git = sh.git.bake(_cwd='/Users/samatkins/projects/cubiio-hugo-blog/public')


# deploy to Hugo
def deploy_Hugo():
    """ Publishes /public folder to remote """

    # git add all
    print (git.add('-A'))

    # print status after add all
    print (git.status())

    # git commit
    print (git.commit(m='chore: Publish new content to Hugo blog'))

    # print status after add all
    print (git.status())

    # git push origin master
    print (git.push.origin("master"))

    # print status after push to origin
    print (git.status())

    # print final message confirming job complete
    print ("Deployment complete")


deploy_Hugo()
