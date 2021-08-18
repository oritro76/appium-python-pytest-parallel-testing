from appium.webdriver.common.mobileby import MobileBy

from activities.app import App


class OnboardSuccessActivity():
    title = (MobileBy.ID, 'app.choco.dummyqa:id/success_title')

    success_text = 'Welcome to Choco!!'