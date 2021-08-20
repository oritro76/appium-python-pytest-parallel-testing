import os


def android_system_port():
    if os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
        return 8210
    else: # include 'master' and 'gw0'
        return 8205


def device():
    device1 = "device1"
    device2 = "device2"
    if os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
        return device1
    else: # include 'master' and 'gw0'
        return device2