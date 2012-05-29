#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# wasco/wasco.py
#
# (c) 2010-2012 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: 
#
# input: --
# output: --
#
# created 2010
# last mod 2012-05-29 12:38 DW

from ctypes import c_int,c_ulong,byref
import WascoConstants
from exceptions import OSError, ImportError, BaseException 

class Wasco(object): 
    """ 
    Gives you an object wasco which is a handle for wasco card and already
    initialized. 
    
    It also gives you the boardId and boardInfo in the
    variables boardId and boardInfo.

    In principle, some definitions from wasco.h are taken, then dll is
    loaded using ctypes, and card is initialized.
    """
    def __init__(self, dummy=False):
        self.dummy = dummy
        try: 
            if self.dummy is True:
                raise(BaseException) # GOTO: Exception is just used to jump to the except block
            from ctypes import windll
            # load dll
            self.wasco = windll.wasco
            
            # define some important variables
            self.boardId = c_int(1)
            self.error = c_ulong()
            self.boardInfo = WascoConstants.WascoBoardInfo()
            
            # error if board-id is not valid
            self.error = self.wasco.wasco_getBoardInfo(self.boardId, byref(self.boardInfo))
            
            if( self.error ):
                print self.error
            
            # warning if there are no analog outputs
            if( not self.boardInfo.nAnalogOut ):
                print "WARNING: no analog outputs found"
            
            # initialize card
            self.wasco.wasco_openBoard( byref(self.boardId), self.boardInfo.pBoardName)

            self.wasco_outportW = self.wasco.wasco_outportW

        except (OSError, ImportError, BaseException):
            if self.dummy is False:
                print('''########## WARNING ##########
                        Cannot load wasco.dll. Creating wasco dummy!''')
            self.boardId = c_int(1)
            self.error = c_ulong()
            self.boardInfo = WascoConstants.WascoBoardInfo()
            pass

    def wasco_outportW(self, board_id, channel, value):
        """
        Dummy function is only called when dummy=True.
        """
        # dummy for the only function we use
        pass

wasco = Wasco()
boardId = c_int(1)
        




