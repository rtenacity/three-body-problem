#!/usr/bin/env python3
# encoding:utf-8
import sys
import time
sys.path.append('/home/pi/ArmPi_mini/')
from ArmIK.ArmMoveIK import *


AK = ArmIK()


AK.setPitchRangeMoving((0, 6, 18), 80,-90, 90, 1500)
