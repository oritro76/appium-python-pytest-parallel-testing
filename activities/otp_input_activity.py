from appium.webdriver.common.mobileby import MobileBy

from activities.app import App


class OTPInputActivity():

    back_button = (MobileBy.CLASS_NAME, 'android.widget.ImageButton')
    title = (MobileBy.ID, 'app.choco.dummyqa:id/title')
    description = (MobileBy.ID, 'app.choco.dummyqa:id/description')
    otp_input = (MobileBy.CLASS_NAME, 'android.widget.EditText')
    error_indicator = (MobileBy.ID, 'app.choco.dummyqa:id/errorIndicator')
    loading = (MobileBy.ID, 'app.choco.dummyqa:id/loadingText')

    desciption_text = 'We sent the code to '
    title_text = 'We just sent you an SMS with a code. Please type it below!'
    loading_text = 'Loading…'



