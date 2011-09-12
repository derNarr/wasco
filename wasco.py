#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./wasco/wasco.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)


"""
wasco.py gives you an object wasco which is a handle for wasco card
and already initialized.
It also gives you the boardId and boardInfo in the variables boardId and 
boardInfo.
"""

# Grundsaetzlich werden aus der wasco.h einige Definitionen uebernommen,
# dann wird mit ctypes die dll geladen und die Karte vorbereitet.

from ctypes import c_int,c_ulong,byref
import WascoConstants
from exceptions import OSError, ImportError

try:
    from ctypes import windll

    ## load dll
    wasco = windll.wasco
    
    # define some important variables
    boardId = c_int(1)
    error = c_ulong()
    boardInfo = WascoConstants.WascoBoardInfo()
    
    ## error if board-id is not valid
    error = wasco.wasco_getBoardInfo(boardId, byref(boardInfo))
    
    if( error ):
        print error
    
    ## warning if there are no analog outputs
    if( not boardInfo.nAnalogOut ):
        print "WARNING: no analog outputs found"
    
    ## initialize card
    wasco.wasco_openBoard( byref(boardId), boardInfo.pBoardName)
except (OSError, ImportError):
    class Wasco(object):
        """
        Small class to create slim wasco dummy.
        """

        def __init__(self):
            pass

        def wasco_outportW(self, board_id, channel, value):
            """
            dummy function
            """
            pass
    wasco = Wasco()
    boardId = c_int(1)
        




