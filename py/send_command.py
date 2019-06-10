#!/usr/bin/env python

import sys
from dbb_utils import *


try:

    password = '0000'

    openHid()


    # Start up options - factory reset; initial password setting
    if 0:
        hid_send_encrypt('{"reset":"__ERASE__"}', password)
        hid_send_plain('{"password":"' + password + '"}')
        sys.exit()

    if 0:
        # message = '{"bootloader": "unlock"}'
        # hid_send_encrypt(message, password)
        message = '{"bootloader": "lock"}'
        hid_send_plain(message)
        sys.exit()

    # Example JSON commands - refer to digitalbitbox.com/api
    # message = '{"led":"blink"}'
    # message = '{"backup":"list"}'
    # message = '{"random":"pseudo"}'
    # message = '{"bootloader":"lock"}'
    # message = '{"bootloader":"unlock"}'
    # message = '{"feature_set":{"U2F":false}}'
    # message = '{"seed":{"source":"create", "filename":"testing.pdf", "key":"password"}}'
    # message = '{"sign":{"meta":"hash", "data":[{"keypath":"m/1p/1/1/0", "hash":"0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"},{"keypath":"m/1p/1/1/1", "hash":"123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0"}]}}'
    # message = '{"sign":{"meta":"hash", "data":[{"keypath":"m/1p/1/1/0", "hash":"0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef", "tweak":"0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"},{"keypath":"m/1p/1/1/1", "hash":"123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0"}]}}'

    message = '{"device":"info"}'
    hid_send_encrypt(message, password)

    # Send a JSON command
    keypath = 'm/44p/0p/9p/0/0' # 9p represents DLC contract

    message = '{"xpub" : "%s"}' % keypath
    hid_send_encrypt(message, password)

    h = "582ae2090fa1247980226a9e88216ab4a88cf3640cb95ee418188d4ff04c801f"
    message = '{"sign": {"meta": "hash", "data": [{"keypath": "%s", "hash": "%s", "tweak": "c53260a779e799341271547b20e0092974a9141bfba6cc574dd10654d5775524"}]}}' % (keypath, h)
    hid_send_encrypt(message, password)
    message = '{"sign": ""}'
    hid_send_encrypt(message, password)

    message = '{"sign": {"meta": "hash", "data": [{"keypath": "%s", "hash": "%s"}]}}' % (keypath, h)
    hid_send_encrypt(message, password)
    message = '{"sign": ""}'
    hid_send_encrypt(message, password)

except IOError as ex:
    print(ex)
except(KeyboardInterrupt, SystemExit):
    print("Exiting code")

dbb_hid.close()

