# THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
# APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
# HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT
# WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND
# PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE
# DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR
# CORRECTION.

# Name: rest.py
# Since: Aug. 22nd, 2019
# Author: Christen Ford
# Purpose: Exposes the database connector as a REST API. The primary purpose
#   of this module is to allow ad-hoc interaction with the database connector.

import aiohttp

async def rest_handler(request):
    '''
    Defines a GET handler for the '/rest' endpoint.

    Users make requests of this handler with a query string containing the
    following arguments:
        cmd: The command c to execute | c E {find, find_one}
        target: The target t to run the command against | t E {groups, rtypes, sensors, readings}.
        params: A list of key-value parameters corresponding to the targets attributes.

    This handler will return an error if the querystring is in an incorrect format.
    
    Args:
        request (aiohttp.web.Request): The web request that initiated the handler.
    '''
    pass
