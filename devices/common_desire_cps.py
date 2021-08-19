from conf.conf import APK_PATH, APK_PACKAGE_NAME, APP_ACTIVITY

android_common_desired_caps = {
    "newCommandTimeout": 60,
    "deviceReadyTimeout": 60,
    "adbExecTimeout": 50000,
    "app": APK_PATH,
    "appPackage": APK_PACKAGE_NAME,
    "appActivity": APP_ACTIVITY,
    "autoGrantPermissions": True,
    "adbExecTimeout": 30000

}