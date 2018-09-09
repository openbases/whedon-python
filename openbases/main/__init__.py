# Copyright (c) 2018, Vanessa Sochat All rights reserved.
# See the LICENSE in the main repository at:
#    https://www.github.com/openbases/openbases-python

def get_client(quiet=False, debug=False):
    '''return the helper function client for OpenBases.
       This is a client that spans the different modules (papers, badges,
       etc.) for interaction with functions from one interface.

       Parameters
       ==========
       quiet: if True, suppress most output about the client
       debug: turn on debugging mode

    '''
    from .base import Client

    Client.quiet = quiet
    Client.debug = debug

    # Paper
    from openbases.main.papers import Paper
    Client.paper = Paper

    # Badge
    from openbases.main.badges import Badge
    Client.badge = Badge

    # Initialize
    cli = Client()
    return cli

Client = get_client()
