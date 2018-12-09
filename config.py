#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     09-12-2018
# Copyright:   (c) User 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os



# login info
email = ''# Tumblr account email
username = ''# Tumblr account username
password = ''# Tumblr account password



# make_cookie.py
cookie_path = os.path.join('cookie.txt')# Location to put the cookie file


# list_following.py
followed_xml_path = os.path.join('dl', 'followed.opml')# Location to store tumblr-provided xml followed list
followed_list_path = os.path.join('dl', 'followed_list.txt')# Location to write list of followed blogs to



def main():
    pass

if __name__ == '__main__':
    main()
