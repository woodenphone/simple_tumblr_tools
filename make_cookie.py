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
    pass


def save_cookie(req_ses, cookie_path):
    pass













def main():
    # Setup requests session
    req_ses = requests.Session()
    # Log in
    tumblr_login(req_ses, email-config.email, username=config.username, password=config.password)
    # Save cookie to file
    save_cookie(req_ses, cookie_path=config.cookie_path)
    return


if __name__ == '__main__':
    main()
