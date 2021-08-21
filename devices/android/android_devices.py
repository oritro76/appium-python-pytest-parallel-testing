from devices.common_desire_cps import android_common_desired_caps

android_desired_caps = {"device1": {

                                        "platformVersion": "11",
                                        "deviceName": "Android Emulator",

                                        **android_common_desired_caps
                                    },
                        "device2": {
                                        "platformName": "Android",
                                        "platformVersion": "10",
                                        "deviceName": "Android Emulator",
                                        "automationName": "UiAutomator2",
                                        **android_common_desired_caps
                                },
                        "device3": {
                                        "platformName": "Android",
                                        "platformVersion": "10",
                                        "deviceName": "realme 3 pro",
                                        "automationName": "UiAutomator2",
                                        **android_common_desired_caps
                                    },
                        }
