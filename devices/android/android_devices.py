from devices.common_desire_cps import android_common_desired_caps

android_desired_caps = {"device1": {
                                        "platformName": "Android",
                                        "platformVersion": "11",
                                        "deviceName": "Android Emulator",
                                        "automationName": "UiAutomator2",
                                        "udid": "emulator-5554",
                                        **android_common_desired_caps
                                    },
                        "device2": {
                                        "platformName": "Android",
                                        "platformVersion": "10",
                                        "deviceName": "Android Emulator",
                                        "automationName": "UiAutomator2",
                                        "udid": "emulator-5556",
                                        **android_common_desired_caps
                                }
                        }
