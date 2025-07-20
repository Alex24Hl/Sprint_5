from random import randint

class GenerateUserData:

    @staticmethod
    def generate_user_email():
        return f'test_{randint(0, 999)}@yandex.ru'

    @staticmethod
    def generate_invalid_email():
        return f'{randint(0, 9999)}'
    
    def generate_password():
        return f'*{randint(0, 9999)}!@A'