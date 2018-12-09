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
# StdLib
import time
import os
import random
import logging
import logging.handlers
import datetime
import json
import cookielib
import re
import xml.etree.ElementTree as ET# https://docs.python.org/2.7/library/xml.etree.elementtree.html
# Remote libraries
import requests
import requests.exceptions
# local
import common
from login import tumblr_login# tumblr_login(req_ses, email, username, password)
import dev_config as config# For my personal development use
# import config# For disribution use






def list_followed(req_ses, followed_xml_path, followed_list_path):
    logging.info('Listing followed blogs')
    # Get followed list file
    save_followed_file(req_ses, followed_xml_path)
    # Parse followed list
    parse_followed_file(followed_xml_path, followed_list_path)
    return


def save_followed_file(req_ses, followed_list_path):
    logging.info('Saving list of followed blogs')
    followed_list_path = os.path.join('dl', 'followed.opml')
    # Get followed list file
    # www.tumblr.com/following.opml
    logging.debug('Loading followed list')
    followed_res = common.fetch(
        requests_session=req_ses,
        url='https://www.tumblr.com/following.opml',
        method='get',
    )
    common.write_file(# Save to file
        file_path=followed_list_path,
        data=followed_res.content
    )
    logging.info('Saved list of followed blogs')
    return


def parse_followed_file(followed_xml_path, followed_list_path):
    logging.info('Parsing list of followed blogs')
    # Load followed list
    followed_list_xml = common.read_file(file_path=followed_xml_path)
    # Parse followed list
    followed_blogs_urls = re.findall('htmlUrl="([^"]+)"/>', followed_list_xml)
##    followed_blogs = []
##    tree = ET.parse(followed_list_path)
##    root = tree.getroot()
##    for child in root:
##        blog_url = child.htmlurl
##        followed_blogs.append()
    # Export list as text
    with open(followed_list_path, 'a') as f:
        for followed_blogs_url in followed_blogs_urls:
            f.write('{0}\n'.format(followed_blogs_url))
    logging.info('Parsed list of followed blogs')




def main():
    # Setup requests
    req_ses = requests.Session()# Setup requests session
    cookie_dir = os.path.dirname(config.cookie_path)# Ensure folder we're storing cookie in exists
    if (cookie_dir):
        if not os.path.exists(cookie_dir):
            os.makedirs(cookie_dir)
        assert(os.path.exists(cookie_dir))# This folder should exist by this point.
    req_ses.cookies = cookie_jar = cookielib.MozillaCookieJar(config.cookie_path)# Prepare cookiejar for later use

    # Log in
    tumblr_login(
        req_ses,
        email=config.email,
        username=config.username,
        password=config.password
    )

    # List followed blogs
    list_followed(
        req_ses,
        followed_xml_path=config.followed_xml_path,
        followed_list_path=config.followed_list_path
    )
    return


if __name__ == '__main__':
    common.setup_logging(os.path.join("debug", "list_following.log.txt"))# Setup logging
    try:
        main()
    # Log exceptions
    except Exception, e:
        logging.critical(u"Unhandled exception!")
        logging.exception(e)
    logging.info(u"Program finished.")