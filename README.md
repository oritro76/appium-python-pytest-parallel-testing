# Automated tests for Choco App

**Tech Stack**
Python 3.8, Appium, Pytest-BDD, Allure Reports

## Prerequisites
1. Install Allure Reports from https://docs.qameta.io/allure/#_installing_a_commandline
2. Install Android Studio from https://developer.android.com/studio
3. Install Appium from https://appium.io/
4. Install Python from https://www.python.org/downloads/
5. Install virtualenv from https://virtualenv.pypa.io/en/latest/installation.html

## Project Structure At A Glance
```
|-- activities
|   |-- app.py
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
|-- runner.sh
|-- screenshots
|-- TESTCASES.MD
|-- test_results
|-- tests
|   |-- features
|   |   `-- onboard_to_choco_app.feature
|   `-- step_defs
|       |-- conftest.py
|       |-- __init__.py
|       `-- test_onboarding_steps.py
`-- utils
    |-- classes.py
    `-- __init__.py
```
## Getting Started

#### Clone the repo
```
git clone git@github.com:choco-hire/QA-automation-exercise-AritraB.git
```

#### Create vitual environment for the project
```commandline
virtualenv venv
```
#### Activate the virtual environment
Windows
```commandline
venv\Scripts\activate
```
Linux
```commandline
source venv/bin/activate
```
#### Install requirements

```commandline
pip install -r requirements.txt
```
### Before Running the tests
1. Start an android emulator with Android Platformversion 11.
If any other emulator is used please change desired capabilities in devices/android/android_devices.py
2. Start the appium server

### Test Markers
Two markers have been introduced.
1. choco -> Run all the tests. For marking feature
2. debug -> Run single or multiple tests. For Marking scenarios 

#### Run tests
To run tests do the following
1. Go to project root directory
2. Execute the runner.sh

### runner.sh
runner.sh takes three arguments.
1. device type {android, ios}
2. hub url ex: http://127.0.0.1:4723/wd/hub
3. marker {choco, debug}

to run runner.sh use either one of the methods
chmod
```
chmod +x runner.sh
./runner.sh android "http://127.0.0.1:4723/wd/hub" choco
```
or

```
bash runner.sh android "http://127.0.0.1:4723/wd/hub" choco
```
