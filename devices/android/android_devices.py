from conf.conf import APK_PATH, APK_PACKAGE_NAME, APP_ACTIVITY

android_desired_caps = {"device1": {
                                        "platformName": "Android",
                                        "platformVersion": "11",
                                        "deviceName": "Android Emulator",
                                        "automationName": "UiAutomator2",
                                        "app": APK_PATH,
                                        "appPackage": APK_PACKAGE_NAME,
                                        "appActivity": APP_ACTIVITY,
                                        "autoGrantPermissions": True,
                                        "udid": "emulator-5554",
                                        "systemPort": 8200,
                                        "adbExecTimeout": 30000
                                   },
                        "device2": {
                                        "platformName": "Android",
                                        "platformVersion": "10",
                                        "deviceName": "realme 3 pro",
                                        "automationName": "UiAutomator2",
                                        "app": APK_PATH,
                                        "appPackage": APK_PACKAGE_NAME,
                                        "appActivity": APP_ACTIVITY,
                                        "autoGrantPermissions": True,
                                        "udid": "c3dbca28",
                                        "systemPort": 8205,
                                        "adbExecTimeout": 30000
                                }
                        }
