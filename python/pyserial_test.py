#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial, time

port = "/dev/ttyACM0"

print("Open Port")
ser =serial.Serial(port, 9600)
while True:
	# #  LED点灯
	# ser.write(b"1")
	# time.sleep(2)
	# #  LED消灯
	# ser.write(b"0")
	# time.sleep(1)
    # #  LED点灯
	# ser.write(b"1440")
	# time.sleep(2)

    #ヘッダー
    ser.write(b"191")

    # ser.write(b"0")
    # ser.write(b"25")
    # ser.write(b"25")
    # ser.write(b"25")
    # ser.write(b"25")
    # ser.write(b"25")
    # ser.write(b"25")
    # ser.write(b"0")

print("Close Port")
ser.close()
