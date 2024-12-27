#!/usr/bin/python3

import sys
from urllib.parse import quote, urlparse
from pymd5 import md5, padding


##########################
# Example URL parsing code:
res = urlparse('https://project1.ecen4133.org/test/lengthextension/api?token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')
# res.query returns everything after '?' in the URL:
assert(res.query == 'token=41bd1ccd26a75c282922c2b39cc3bb0a&command=Test1')

###########################
# Example using URL quoting
# This is URL safe: a URL with %00 will be valid and interpreted as \x00
assert(quote('\x00\x01\x02') == '%00%01%02')

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)
        sys.exit(-1)

    # Get url from command line argument (argv)
    url = sys.argv[1]

    #################################
    # Your length extension code here

    # define constants for secret size and appended command
    SECRET_KEY_SIZE = 8
    APPENDED_SAFE_UNLOCK_COMMAND = "&command=UnlockSafes"
    URL_QUERY = urlparse(url).query

    # stores token and commands sections of the url into variables
    url_token = URL_QUERY[6:38]
    url_commands = URL_QUERY[39:]
    # print("url_token = " + url_token)
    # print("url_commands = " + url_commands)

    # calculate size of m and store in variable
    m_length = SECRET_KEY_SIZE + len(url_commands)

    # calculate the hash of m + padding + suffix
    bits =  (m_length + len(padding(m_length*8))) * 8
    h = md5(state=bytes.fromhex(url_token), count=bits)
    h.update(APPENDED_SAFE_UNLOCK_COMMAND)
    new_token = h.hexdigest()

    # calculate padding value
    padding_value = quote(padding(m_length*8))

    # at the end, assemble the new url!
    new_url = url[0:-len(URL_QUERY)] + "token=" + new_token + "&" + url_commands + padding_value + APPENDED_SAFE_UNLOCK_COMMAND
    print(new_url)