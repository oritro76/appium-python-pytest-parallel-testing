from conf.conf import APK_PATH, APK_PACKAGE_NAME, APP_ACTIVITY

android_desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        "app": APK_PATH,
        "appPackage": APK_PACKAGE_NAME,
        "appActivity": APP_ACTIVITY
    }
