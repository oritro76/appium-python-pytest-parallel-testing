import os
import subprocess
import re
from utils.adb_commands import *


def get_android_desired_caps_from_os_env():
    from utils.constants import worker_name, android_device_name, android_device_os, udid

    num_workers = int(os.getenv('PYTEST_XDIST_WORKER_COUNT'))
    android_system_port = 8205
    increment_system_port_by = 5
    desired_caps = dict()

    for temp in range(num_workers):
        if os.getenv('PYTEST_XDIST_WORKER') == worker_name + str(temp):
            desired_caps['systemPort'] = android_system_port + increment_system_port_by * temp
            desired_caps['udid'] = os.environ[udid + str(temp)]
            desired_caps['platformVersion'] = os.environ[android_device_os + str(temp)]
            desired_caps['deviceName'] = os.environ[android_device_name + str(temp)]
            return desired_caps

def adb_get_device_udids():
    command = adb_command_get_udid.split()
    output = subprocess.check_output(command)
    udids = re.findall('\\n(.*?)\\t', output.decode("utf-8"))
    return udids


def adb_get_device_name(udid):
    command = adb_command_get_android_device_name.format(udid).split()
    output = subprocess.check_output(command)
    return output.decode("utf-8").strip()


def adb_get_device_android_version(udid):
    command = adb_command_get_android_version.format(udid).split()
    output = subprocess.check_output(command)
    return output.decode("utf-8").strip()

