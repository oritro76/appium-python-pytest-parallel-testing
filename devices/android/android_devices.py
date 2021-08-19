from devices.common_desire_cps import android_common_desired_caps

android_desired_caps = {"device1": {
                                        "platformName": "Android",
                                        "platformVersion": "11",
                                        "deviceName": "Android Emulator",
                                        "automationName": "UiAutomator2",
                                        "udid": "emulator-5554",
                                        "systemPort": 8200,
                                        **android_common_desired_caps
                                    },
                        "device2": {
                                        "platformName": "Android",
                                        "platformVersion": "10",
                                        "deviceName": "realme 3 pro",
                                        "automationName": "UiAutomator2",
                                        "udid": "c3dbca28",
                                        "systemPort": 8205,
                                        **android_common_desired_caps
                                }
                        }
