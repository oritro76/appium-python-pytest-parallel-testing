# Automated tests for Choco App

**Tech Stack**
Python 3.8, Appium, Pytest-BDD, Allure Reports, Pytest-xdist

## Prerequisites
1. Install Allure Reports from https://docs.qameta.io/allure/#_installing_a_commandline
2. Install Android Studio from https://developer.android.com/studio
3. Install Appium from https://appium.io/
4. Install Python from https://www.python.org/downloads/
5. Install virtualenv from https://virtualenv.pypa.io/en/latest/installation.html

## Solution Explained
This solution can test the testcases in multiple devices. As a result test execution time improves significantly. Find below the time taken for all test case execution in local machine:
#### 1 Device
277.56s (0:04:37)
#### 2 Devices
168.26s (0:02:48)
#### 3 Devices
119.15s (0:01:59)

### Test Markers
Four markers have been introduced.
1. choco -> Run all the tests. For marking feature
2. debug -> Run single or multiple tests. For Marking scenarios 
3. successful-onboard-> marks all the scenarios related to successful onboard 
4. other-> marks all the scenarios which are not related to successful onboard


## Project Structure At A Glance
```
|-- activities
|   |-- __init__.py
|   |-- onboard_success_activity.py
|   |-- otp_input_activity.py
|   `-- phone_number_input_activity.py
|-- conf
|   |-- conf.py
|   `-- __init__.py
|-- conftest.py
|-- custom_excepitons
|   |-- appium_exceptions.py
|   |-- base_exception.py
|   |-- env_variable_exceptions.py
|   `-- __init__.py
|-- data
|   |-- apps
|   |   |-- android
|   |   |   `-- app-debug.apk
|   |   `-- ios
|   |-- data_gen.py
|   |-- __init__.py
|   `-- valid_data.py
|-- definitions.py
|-- devices
|   |-- android
|   |   |-- android_devices.py
|   |   `-- __init__.py
|   |-- common_desire_cps.py
|   |-- __init__.py
|   `-- ios
|       |-- __init__.py
|       `-- ios_devices.py
|-- driver
|   |-- appium_driver.py
|   `-- __init__.py
|-- logs
|   `-- tests
|-- pytest.ini
|-- README.md
|-- requirements.txt
|-- runner.py
|-- screenshots
|-- show_report.sh
|-- TESTCASES.MD
|-- test_results
|-- tests
|   |-- features
|   |   `-- onboard_to_choco_app.feature
|   |-- fixtures
|   |   |-- __init__.py
|   |   `-- test_helpers.py
|   `-- step_defs
|       |-- conftest.py
|       |-- __init__.py
|       |-- test_entering_wrong_otp_code_show_error_message_and_correcting_it_results_successful_onboard.py
|       |-- test_from_otpinputactivity_device_back_button_press.py
|       |-- test_in_otpinputactivity_description_phone_number_where_otp_was_sent_is_shown.py
|       |-- test_onboard_into_choco_app_by_entering_phone_number_and_then_selecting_country_code.py
|       |-- test_onboard_into_choco_app_when_mobile_is_in_landscape.py
|       |-- test_onboard_into_choco_app_when_valid_text_is_entered_for_country_code_filtering.py
|       |-- test_tapping_on_back_button_in_otp_input_activity_will_take_user_to_phone_number_input_activity.py
|       `-- test_wrong_country_code_wrong_and_invalid_phone_number_input_shows_error_message.py
`-- utils
    |-- adb_commands.py
    |-- classes.py
    |-- constants.py
    |-- functions.py
    `-- __init__.py

```
## Getting Started

#### Clone the repo
```
git clone git@github.com:<repo_name>
```

#### Create vitual environment for the project
```
virtualenv venv
```
#### Activate the virtual environment
Windows
```
venv\Scripts\activate
```
Linux
```
source venv/bin/activate
```
#### Install requirements

```
pip install -r requirements.txt
```

### Before Running the tests 
1. Start the appium server
2. Start Android Emulators or connect real devices


#### Run tests
To run tests, runner.py has been introduced. 

usage: 
```
runner.py [-h] [-d {android,ios}] [-hu HUBHOST] [-hp HUBPORT] [--hubprotocol {http,https}] [--devnum DEVNUM] [--testmarker TESTMARKER]

optional arguments:
  -h, --help            show this help message and exit
  -d {android,ios}, --device {android,ios}
                        specify device type. supports {android, ios}
  -hu HUBHOST, --hubhost HUBHOST
                        specify hub host. ex: 127.0.0.1
  -hp HUBPORT, --hubport HUBPORT
                        specify hub port. ex: 4723
  --hubprotocol {http,https}
                        specify hub portocot. ex: http
  --devnum DEVNUM       specify number of devices
  --testmarker TESTMARKER
                        mark tests
```


1. Go to project root directory
2. Run runner.py with with argument `devnum` if appium is running locally and connected to `4723` port
```
python runner.py --devnum 2
```
3. Run show_report.sh to see the report

```
chmod +x show_report.sh
./show_report.sh
```
or
```
bash show_report.sh
```
