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








def list_followed(req_ses, followed_list_path):
    logging.info('Listing followed blogs')

    logging.info('Listed followed blogs')
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

    # List followed blogs
    list_followed(req_ses, followed_list_path=config.followed_list_path)
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