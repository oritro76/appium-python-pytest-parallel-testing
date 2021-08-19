from appium.webdriver.common.mobileby import MobileBy


class OnboardSuccessActivity:
    title = (MobileBy.ID, 'app.choco.dummyqa:id/success_title')

    success_text = 'Welcome to Choco!!'