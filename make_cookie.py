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
# Remote libraries
import requests
import requests.exceptions
# local
import common
import dev_config as config# For my personal development use
# import config# For disribution use



def tumblr_login(req_ses, email, username, password):
    logging.info('Logging in as {0!r}'.format(username))

    # Load front page to look normal
    logging.debug('Loading front page to prepare login attempt')
    response_1 = common.fetch(
        requests_session=req_ses,
        url='https://www.tumblr.com/login',
        method='get',
    )
    common.write_file(
        file_path=os.path.join('debug', 'login.response_1.html'),
        data=response_1.content
    )

    # Load login page
    logging.debug('Loading login page')
    response_2 = common.fetch(
        requests_session=req_ses,
        url='https://www.tumblr.com/login',
        method='get',
    )
    common.write_file(
        file_path=os.path.join('debug', 'login.response_2.html'),
        data=response_2.content
    )

    # Get key from login page
    #'<meta name="tumblr-form-key" id="tumblr_form_key" content="!1231544361914|zzONO1XougbCpvRupb561N630">'
    token_search = re.search('<meta name="tumblr-form-key" id="tumblr_form_key" content="([a-zA-Z0-9!|]+)">', response_2.content, re.IGNORECASE)
    token = token_search.group(1)

    # Perform login
    logging.debug('Sending login request')
    response_3 = common.fetch(
        requests_session=req_ses,
        url='https://www.tumblr.com/login',
        method='post',
        data={
            'determine_email': email,
            'user[email]': email,
            'user[password]': password,
            'form_key': token,
        },
        expect_status=200,
    )
    common.write_file(
        file_path=os.path.join('debug', 'login.response_3.html'),
        data=response_3.content
    )

    # Validate login worked
    logging.debug('Checking if login worked')
    response_4 = common.fetch(
        requests_session=req_ses,
        url='https://www.tumblr.com/dashboard',
        method='get',
    )
    common.write_file(
        file_path=os.path.join('debug', 'login.response_4.html'),
        data=response_4.content
    )

    logging.info('Logged in as {0!r}'.format(username))
    return


def main():
    # Setup requests
    req_ses = requests.Session()# Setup requests session
    cookie_dir = os.path.dirname(config.cookie_path)# Ensure folder we're storing cookie in exists
    if not os.path.exists(cookie_dir):
        os.makedirs(cookie_dir)
    assert(os.path.exists(cookie_dir))# This folder should exist by this point.
    requests_session.cookies = cookie_jar = cookielib.MozillaCookieJar(config.cookie_path)# Prepare cookiejar for later use

    # Log in
    tumblr_login(req_ses, email=config.email, username=config.username, password=config.password)

    # Save cookie to file
    req_ses.cookies.save()
    return


if __name__ == '__main__':
    common.setup_logging(os.path.join("debug", "make_cookie.log.txt"))# Setup logging
    try:
        main()
    # Log exceptions
    except Exception, e:
        logging.critical(u"Unhandled exception!")
        logging.exception(e)
    logging.info(u"Program finished.")
