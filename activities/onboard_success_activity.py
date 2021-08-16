from appium.webdriver.common.mobileby import MobileBy

from activities.app import App


class OnboardSuccessActivity(App):
    title = (MobileBy.ID, 'app.choco.dummyqa:id/success_title')

    success_text = 'Welcome to Choco!!'

    def __init__(self, driver):
        super().__init__(driver=driver)