import requests
import os
from dotenv import load_dotenv


load_dotenv()


class CallMeBot:

    def __init__(self):
        self.__base_url = 'https://api.callmebot.com/whatsapp.php'
        self.__api_key = os.getenv('CALLMEBOT_API_KEY')
        self.__my_phone_number = os.getenv('MY_PHONE_NUMBER')

    def send_messaage(self, message):
        response = requests.get(
            url=f'{self.__base_url}?phone={self.__my_phone_number}&text={message}&apikey={self.__api_key}'
        )
        return response.text
