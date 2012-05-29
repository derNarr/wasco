#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# wasco/WascoConstants.py
#
# (c) 2010-2012 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
# Maybe some Copyrights belong to www.wasco.de or the Messcomp Datentechnik
# GmbH.
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: Tubes and DevTubes classes, which provide functions for working
# with the tubes.
#
# input: --
# output: --
#
# created 2010
# last mod 2012-05-29 12:37 DW

# Grundsaetzlich werden aus der wasco.h einige Definitionen uebernommen,
# dann wird mit ctypes die dll geladen und die Karte vorbereitet.

"""
WascoConstants.py defines all important variables, constants and structures
for wasco card.
"""

from ctypes import Structure, c_ulong, c_char

##----------------------------------------------------------------------
## flags
##----------------------------------------------------------------------

## should 'wasco_readAnalogInp' wait for result:
WF_DONT_WAIT           = 0x00000001 ## function returns immediately

## what triggers the analog conversion:
WF_TRIGGER_EXTERNAL    = 0x00010000 ## analog input triggered externally
WF_TRIGGER_BY_TIMER    = 0x00020000 ## analog input triggered by timer

## the following flags can be OR'ed with the channel number:
WF_GAIN_1              = 0x01000000 ## gain of analog conversion is 1
WF_GAIN_2              = 0x02000000 ## gain of analog conversion is 2
WF_GAIN_4              = 0x03000000 ## gain of analog conversion is 4
WF_GAIN_8              = 0x05000000 ## gain of analog conversion is 8
WF_GAIN_16             = 0x08000000 ## gain of analog conversion is 16
WF_8_BIT               = 0x00800000 ## 8-bit analog conversion (else 12-bit)

## these functions describe 'functions' of WascoBoardInfo:
WASCO_DESCR_INTERRUPT  = 0x00000100
WASCO_DESCR_TIMER      = 0x00001000

##----------------------------------------------------------------------
## error codes
##----------------------------------------------------------------------

WASCO_OK                           = 0

WASCOERR_BOARD_NOT_FOUND           = (0x0f000000)
WASCOERR_BOARD_BUSY                = (0x0f010000)

WASCOERR_CANNOT_FIND_LIBRARY       = (0x10040000)
WASCOERR_CANNOT_FIND_ADDRESS       = (0x10050000)
WASCOERR_BAD_PARAM                 = (0x10060000)
WASCOERR_BAD_VERSION               = (0x10070000)
WASCOERR_INTERNAL                  = (0x10080000)
WASCOERR_UNKNOWN                   = (0x10090000)
WASCOERR_FUNCTION_NOT_AVAILABLE    = (0x100a0000)
WASCOERR_BOARD_NOT_OPENED          = (0x100b0000)
WASCOERR_NOT_ENOUGH_MEMORY         = (0x100c0000)
WASCOERR_CANNOT_OPEN_KERNEL        = (0x100d0000)
WASCOERR_BAD_KERNEL_VERSION        = (0x100f0000)
WASCOERR_CANNOT_FIND_KERNEL        = (0x10100000)
WASCOERR_INVALID_HANDLE            = (0x10110000)
WASCOERR_DEVICE_IO_FAILED          = (0x10120000)
WASCOERR_REGISTRY_FAILURE          = (0x10130000)
WASCOERR_CANNOT_START_KERNEL       = (0x10140000)
WASCOERR_ACCESS_DENIED             = (0x10160000)
WASCOERR_DEVICE_NOT_OPENED         = (0x10170000)
WASCOERR_TOO_MANY_OPEN_PROCESSES   = (0x101b0000)
WASCOERR_SIGNAL_OVERFLOW           = (0x101c0000)
WASCOERR_CANNOT_SIGNAL             = (0x101d0000)

WASCOERR_CANNOT_LOCK_MEM           = (0x12060000)

WASCOERR_CANNOT_INSTALL_HANDLER    = (0x13010000)

WASCOERR_CANNOT_CREATE_EVENT       = (0x17000000)
WASCOERR_CANNOT_CREATE_THREAD      = (0x17010000)
WASCOERR_CANNOT_BLOCK_THREAD       = (0x17020000)
WASCOERR_CANNOT_CREATE_SHARED      = (0x17050000)
WASCOERR_WAIT_TIMEOUT              = (0x17080000)
WASCOERR_EVENT_NOT_SIGNALED        = (0x17090000)
WASCOERR_CANNOT_CREATE_CALLBACK    = (0x170a0000)
WASCOERR_CANNOT_OPEN_BOARD         = (0x170b0000)

##----------------------------------------------------------------------
## i/o port offsets - 8 bit registers
##----------------------------------------------------------------------

##      port name               offset
##      -------------           ------
AD_CON_1               = 0x00
AD_CON_2               = 0x01
AD_CON_3               = 0x02
AD_CON_4               = 0x03
AD_CON_5               = 0x0e

PIO_PORT_A             = 0x04
PIO_PORT_B             = 0x05
PIO_PORT_C             = 0x06
PIO_CTRL               = 0x07

TIMER_0                = 0x08
TIMER_1                = 0x09
TIMER_2                = 0x0a
TIMER_CTRL             = 0x0b

DA_LOW                 = 0x0c
DA_HIGH                = 0x0d

OPTO_IN_A              = 0x00
OPTO_IN_B              = 0x01
OPTO_OUT_A             = 0x02
OPTO_OUT_B             = 0x03

OPTO_INPUT             = 0x0e
OPTO_INT_CTRL          = 0x21
OPT0_INT_RESET         = 0x20
OPT1_INT_RESET         = 0x21
OPT2_INT_RESET         = 0x22
OPT3_INT_RESET         = 0x23
OPT4_INT_RESET         = 0x24
OPT5_INT_RESET         = 0x25
OPT6_INT_RESET         = 0x26
OPT7_INT_RESET         = 0x27

TIMER_INT_CTRL         = 0x22
TIMER_INT_RESET        = 0x28

PIO1_PORT_A            = 0x00
PIO1_PORT_B            = 0x01
PIO1_PORT_C            = 0x02
PIO1_CTRL              = 0x03
PIO2_PORT_A            = 0x04
PIO2_PORT_B            = 0x05
PIO2_PORT_C            = 0x06
PIO2_CTRL              = 0x07
PIO3_PORT_A            = 0x0c
PIO3_PORT_B            = 0x0d
PIO3_PORT_C            = 0x0e
PIO3_CTRL              = 0x0f
PIO4_PORT_A            = 0x10
PIO4_PORT_B            = 0x11
PIO4_PORT_C            = 0x12
PIO4_CTRL              = 0x13
PIO5_PORT_A            = 0x14
PIO5_PORT_B            = 0x15
PIO5_PORT_C            = 0x16
PIO5_CTRL              = 0x17
PIO6_PORT_A            = 0x18
PIO6_PORT_B            = 0x19
PIO6_PORT_C            = 0x1a
PIO6_CTRL              = 0x1b
PIO7_PORT_A            = 0x1c
PIO7_PORT_B            = 0x1d
PIO7_PORT_C            = 0x1e
PIO7_CTRL              = 0x1f

PIO_RESET              = 0x2f

##----------------------------------------------------------------------
## i/o port offsets - 16 bit registers
##----------------------------------------------------------------------

AD_SWTRIG              = 0x00
AD_ADDAT               = 0x00
AD_ADRANGE             = 0x02
AD_ADCONT              = 0x04
AD_ADSTAT              = 0x06
AD_STARTCH             = 0x06
AD_STOPCH              = 0x08

INTCONT                = 0x0A
RESETINT               = 0x0C
RESETFIFO              = 0x0E
RESETERRORFLAG         = 0x10

DAOUT1                 = 0x20
DAOUT2                 = 0x22
DAOUT3                 = 0x24
DAOUT4                 = 0x26

DAOUT1_16              = 0x00
DAOUT2_16              = 0x02
DAOUT3_16              = 0x04
DAOUT4_16              = 0x06
DAOUT5_16              = 0x08
DAOUT6_16              = 0x0a
DAOUT7_16              = 0x0c
DAOUT8_16              = 0x0e
DAOUT9_16              = 0x10
DAOUT10_16             = 0x12
DAOUT11_16             = 0x14
DAOUT12_16             = 0x16
DAOUT13_16             = 0x18
DAOUT14_16             = 0x1a
DAOUT15_16             = 0x1c
DAOUT16_16             = 0x1e

OPTO_IN_A_16           = 0x00
OPTO_IN_B_16           = 0x02
OPTO_IN_C_16           = 0x04
OPTO_IN_D_16           = 0x06

OPTO_OUT_A_16          = 0x20
OPTO_OUT_B_16          = 0x22
OPTO_OUT_C_16          = 0x24
OPTO_OUT_D_16          = 0x26

TTL_IN_16              = 0x40
TTL_OUT_16             = 0x60

TIMER_0_16             = 0x80
TIMER_1_16             = 0x82
TIMER_2_16             = 0x84
TIMER_CTRL_16          = 0x86

INT_CTRL_16            = 0xa0
TIMER_INT_RESET_16     = 0xbe

OPTOIN_MASK_16         = 0xa2
OPTOIN_INPUT_16        = 0xb0
OPTOIN_RESET_16        = 0xc0

##----------------------------------------------------------------------
## i/o port offsets - 32 bit registers
##----------------------------------------------------------------------

TTL_IN_A_32            = 0x40
TTL_IN_B_32            = 0x44
TTL_IN_C_32            = 0x48
TTL_IN_D_32            = 0x4C
TTL_IN_E_32            = 0x50
TTL_OUT_A_32           = 0x60
TTL_OUT_B_32           = 0x64
TTL_OUT_C_32           = 0x68
TTL_OUT_D_32           = 0x6C
TTL_OUT_E_32           = 0x70

TIMER_0_32             = 0x80
TIMER_1_32             = 0x84
TIMER_2_32             = 0x88
TIMER_CTRL_32          = 0x8c

INT_CTRL_32            = 0xa0
TIMER_INT_RESET_32     = 0xbc

DIGIN_MASK_32          = 0xa4
DIGIN_INPUT_32         = 0xb0
DIGIN_RESET_32         = 0xc0

##----------------------------------------------------------------------
## type definitions
##----------------------------------------------------------------------

##typedef DWORD           WERROR; ## error type ## DWORD = c_ulong

## to determine the context of the interrupt:
#enum /*WascoContextType*/
#{ WASCO_ANALOG_IN,              ## result of 'wasco_readAnalogInp' function
#  WASCO_INTERRUPT               ## result of user stimulated interrupt
#};

## common context structure for all interrupt handlers:
class WascoContext(Structure):
    _fields_ = [("cType", c_ulong),    ## reason for the interrupt
                ("boardId", c_ulong)]  ## board ID

#typedef struct
#{ DWORD cType;                  ## reason for the interrupt
#  DWORD boardId;                ## board ID
#} WascoContext;

## special context structure as a result of the 'wasco_readAnalogInp' function:
class WascoAnalogInpContext(Structure):
    _fields_ = [("cType", c_ulong),    ## reason for the interrupt
                ("boardId", c_ulong),  ## board ID
                ("channel", c_ulong),  ## channel number of analog conversion
                ("value", c_ulong)]    ## analog value (8 bits or 12 bits used)

#typedef struct
#{ DWORD cType;                  ## reason for the interrupt
#  DWORD boardId;                ## board ID
#  DWORD channel;                ## channel number of analog conversion
#  DWORD value;                  ## analog value (8 bits or 12 bits used)
#} WascoAnalogInpContext;

## special context structure as a result of a user stimulated interrupt:
class WascoInterruptContext(Structure):
    _fields_ = [("cType", c_ulong),    ## reason for the interrupt
                ("boardId", c_ulong),  ## board ID
                ("status", c_ulong)]   ## board's interrupt status (low 8 bits)
                                       ## plus OPTOIN interrupt status (high 8 bits)

#typedef struct
#{ DWORD cType;                  ## reason for the interrupt
#  DWORD boardId;                ## board ID
#  DWORD status;                 ## board's interrupt status (low 8 bits)
#                                ## plus OPTOIN interrupt status (high 8 bits)
#} WascoInterruptContext;

## structure describing the properties of the board:
class WascoBoardInfo(Structure):
    _fields_ = [("pBoardName", c_char * 64),#create_string_buffer(64)),    ## name of the board (e.g. "ADIODA-PCI12/MCL#3")
                ("pBoardSpec", c_char * 256),#create_string_buffer(256)),   ## specification of the board
                ("ioBaseAddress", c_ulong),                  ## absolute I/O base address of the board
                ("irqNumber", c_ulong),                      ## IRQ number of the board
                ("nAnalogInp", c_ulong),                     ## number of analog input channels
                ("nAnalogOut", c_ulong),                     ## number of analog output channels
                ("nDigitalInOut", c_ulong),                  ## number of digital input/output bits
                ("nOptoInp", c_ulong),                       ## number of OPTOIN bits
                ("nOptoOut", c_ulong),                       ## number of OPTOUT bits
                ("functions", c_ulong)]                      ## functions of the board

#typedef struct
#{ CHAR pBoardName[ 64 ];        ## name of the board (e.g. "ADIODA-PCI12/MCL#3")
#  CHAR pBoardSpec[ 256 ];       ## specification of the board
#  WORD ioBaseAddress;           ## absolute I/O base address of the board
#  WORD irqNumber;               ## IRQ number of the board
#  WORD nAnalogInp;              ## number of analog input channels
#  WORD nAnalogOut;              ## number of analog output channels
#  WORD nDigitalInOut;           ## number of digital input/output bits
#  WORD nOptoInp;                ## number of OPTOIN bits
#  WORD nOptoOut;                ## number of OPTOUT bits
#  WORD functions;               ## functions of the board
#} WascoBoardInfo;               ## 

## prototype of the interrupt callback function:
#typedef WERROR (__stdcall* WascoCallBack)( VOID* pArgs, WascoContext* pContext );

