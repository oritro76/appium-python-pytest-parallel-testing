import argparse
import os
import sys
import subprocess

from utils.functions import (
    adb_get_device_udids,
    adb_get_device_android_version,
    adb_get_device_name
)

from utils.constants import udid, android_device_os, android_device_name

device_type = "android"
hub_host = "127.0.0.1"
hub_port = "4723"
hub_protocol = "http"
num_device = "0"
marker = "choco"

parser = argparse.ArgumentParser()

parser.add_argument("-d",
                    "--device",
                    help="specify device type. supports {android, ios}",
                    default=device_type,
                    choices=["android", "ios"],
                    type=str)

parser.add_argument("-hu",
                    "--hubhost",
                    default=hub_host,
                    help="specify hub host. ex: 127.0.0.1",
                    type=str)

parser.add_argument("-hp",
                    "--hubport",
                    default=hub_port,
                    help="specify hub port. ex: 4723",
                    type=str)

parser.add_argument("--hubprotocol",
                    default=hub_protocol,
                    choices=["http", "https"],
                    help="specify hub portocot. ex: http",
                    type=str)

parser.add_argument("--devnum",
                    default=num_device,
                    help="specify number of devices",
                    type=str)

parser.add_argument("--testmarker",
                    help="mark tests",
                    type=str)

args = parser.parse_args()

if args.device:
    device_type = args.device

if args.hubhost:
    hub_host = args.hubhost

if args.hubprotocol:
    hub_protocol = args.hubprotocol

if args.devnum:
    num_device = args.devnum

devices = adb_get_device_udids()

if num_device == "0":
    print("please provide --devnum argument's value")
    sys.exit()

# if 3 < int(num_device) <= 0:
#     print("Running max 3 devices are supported")
#     sys.exit()

if len(devices) == 0:
    print("No devices attached. Please attach a device/emulator.")
    sys.exit()

elif int(num_device) > len(devices):
    print(f"Found connected devices {len(devices)} but given as arg {int(num_device)}")
    sys.exit()

os.environ["DEVICE_TYPE"] = device_type
os.environ["HUB_URL"] = hub_protocol + "://" + hub_host + ":" + hub_port + "/wd/hub"

for temp in range(int(num_device)):
    os.environ[udid + str(temp)] = devices[temp]
    os.environ[android_device_name + str(temp)] = adb_get_device_name(devices[temp])
    os.environ[android_device_os + str(temp)] = adb_get_device_android_version(devices[temp])


test_env = os.environ.copy()
subprocess.call(["python", "-m", "pytest",
                 "-n", num_device,
                 "-k", marker,
                 "-p", "no:cacheprovider",
                 "--alluredir=./test_results"], env=test_env)
