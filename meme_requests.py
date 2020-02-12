import requests
from settings import Config


class MemeWrapper:

    @staticmethod
    def get_memes() -> dict:
        """
            Gets all the memes listed by imgflip

            Returns:
            dict: Returns the object containing all of the memes

        """
        return requests.get("https://api.imgflip.com/get_memes").json()

    @staticmethod
    def create_meme(meme_id, text_up='', text_down='') -> dict:
        """
            Creates a meme from a template ID

            Parameters:
            meme_id (str): The id of the template to create the meme with
            text_up (str): The text for the first part of the meme
            text_down (str): The text for the second part of the meme

            Returns:
            dict: Returns the object with the created meme information

        """
        params = {
            "template_id": meme_id,
            "text0": text_up,
            "text1": text_down,
            "username": 'aliandi',
            "password": 'fibo10946',
        }
        return requests.get("https://api.imgflip.com/caption_image", params=params).json()
