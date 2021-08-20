import os


def android_system_port():
    if os.getenv('PYTEST_XDIST_WORKER') == 'gw2':
        return 8215
    elif os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
        return 8210
    if os.getenv('PYTEST_XDIST_WORKER') == 'gw0':
        return 8205


def device():
    device1 = "device1"
    device2 = "device2"
    device3= "device3"

    if os.getenv('PYTEST_XDIST_WORKER') == 'gw2':
        return device3
    elif os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
        return device2
    if os.getenv('PYTEST_XDIST_WORKER') == 'gw0':
        return device1

def udid():
    udid1 = "udid0"
    udid2 = "udid1"
    udid3= "udid2"

    if os.getenv('PYTEST_XDIST_WORKER') == 'gw2':
        return os.environ[udid3]
    elif os.getenv('PYTEST_XDIST_WORKER') == 'gw1':
        return os.environ[udid2]
    if os.getenv('PYTEST_XDIST_WORKER') == 'gw0':
        return os.environ[udid1]