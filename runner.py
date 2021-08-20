import argparse
import subprocess
import os
import sys
import re
import pytest

device_type = "android"
hub_host = "127.0.0.1"
hub_port = "4723"
hub_protocol = "http"
num_device = "0"
udid = "udid"
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
    print(args.devnum)
    num_device = args.devnum

process = subprocess.check_output(['adb', 'devices'])

devices = re.findall('\\n(.*?)\\t', process.decode("utf-8") )

if int(num_device) > 3 and int(num_device) <= 0:
    print("Running max 3 devices are supported")
    sys.exit()

if len(devices) == 0:
    print("No devices attached. Please attach a device/emulator.")
    sys.exit()

elif len(devices) != int(num_device):
    print(f"Found connected devices {len(devices)} but given as arg {int(num_device)}")
    sys.exit()

os.environ["DEVICE_TYPE"] = device_type
os.environ["HUB_URL"] = hub_protocol + "://" + hub_host + ":" + hub_port + "/wd/hub"

for temp in range(int(num_device)):
    os.environ[udid + str(temp)] = devices[temp]
    print(os.environ[udid + str(temp)])


test_env = os.environ.copy()
subprocess.call(["python", "-m", "pytest",
                 "-n", num_device,
                 "-k", marker,
                 "-p", "no:cacheprovider",
                 "--alluredir=./test_results"], env=test_env)
