#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./wasco/wasco.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2010-04-20, KS


"""
wasco.py gives you an object wasco which is a handle for the wasco-card
and allready initialized.
It also gives you the boardId and boardInfo in the variables boardId and 
boardInfo.
"""

# Grundsaetzlich ist aus der wasco.h einige Definitionen uebernommen, dann
# wird mit ctypes die dll geladen und die Karte vorbereitet.

from ctypes import * # TODO reduce *-import
import WascoConstants


## load dll
wasco = windll.wasco

# define some important variables
boardId = c_int(1)
error = c_ulong()
boardInfo = WascoConstants.WascoBoardInfo()

## error, if the board-id is not valid
error = wasco.wasco_getBoardInfo(boardId, byref(boardInfo))

if( error ):
    print error

## warning, if there are no analog outputs
if( not boardInfo.nAnalogOut ):
    print "WARNING: no analog outputs found"

## initialize the card
wasco.wasco_openBoard( byref(boardId), boardInfo.pBoardName)

