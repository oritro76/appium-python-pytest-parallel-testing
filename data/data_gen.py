from faker import Faker

from data.valid_data import *


class DataGenerator:

    def __init__(self):
        self.fake = Faker()

    def get_valid_country(self):
        return VALID_COUNTRY


    def get_valid_country_calling_code(self):
        return VALID_COUNTRY_CALLING_CODE


    def get_valid_phone_number(self):
        return VALID_PHONE_NUMBER


    def get_valid_otp(self):
        return VALID_OTP

    def get_random_country(self):
        country = self.fake.country()

        while country == self.get_valid_country():
            country = self.fake.country()

        return country

    def get_random_country_calling_code(self):
        country_calling_code = self.fake.country_calling_code()

        while country_calling_code == self.get_valid_country_calling_code():
            country_calling_code = self.fake.country_calling_code()

        return country_calling_code

    def get_random_phone_number(self):
        phone_number = self.fake.msisdn()[2:]

        while phone_number == self.get_valid_phone_number():
            phone_number = self.fake.msisdn()[2:]

        return phone_number

    def get_random_otp(self):
        Faker.seed(0)
        otp = str(self.fake.pyint(min_value=0, max_value=9999, step=1))

        while otp == self.get_valid_otp():
            otp = str(self.fake.pyint())

        return otp
