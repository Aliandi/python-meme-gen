import json
from api.meme_requests import MemeRequests
from meme import Meme


class MemeProcessor:

    @staticmethod
    def request_get_memes() -> [Meme]:
        """
            Gets all the memes from the API

            Returns:
            dict: Returns the object with all the memes available on the imgflip API
        """

        memes = MemeRequests.get_memes()['data']['memes']
        my_meme_collection = {}
        for meme in memes:
            my_meme_collection[memes.index(meme)] = MemeProcessor.__process_memes(meme)
        return my_meme_collection

    @staticmethod
    def __process_memes(meme) -> Meme:
        return Meme(meme['id'], meme['name'], MemeProcessor.get_meme_keywords(meme['name']))

    @staticmethod
    def store_get_memes()-> [Meme]:
        """
            Gets all the memes from the stored JSON file

            Returns:
            dict: Returns the object with all the memes available on the imgflip API that were stored
        """
        with open('C:\\Aliandi\\python-meme-gen\\api\\memes.json') as memes_file:
            memes = json.load(memes_file)['data']['memes']
            my_meme_collection = {}
            for meme in memes:
                my_meme_collection[memes.index(meme)] = MemeProcessor.__process_memes(meme)
            return my_meme_collection

    @staticmethod
    def get_meme_keywords(meme_name: str) -> [str]:
        return [meme_name.lower()] + meme_name.lower().split()

    @staticmethod
    def get_meme_by_keyword(keyword: str) -> [Meme]:
        norm_keywords = keyword.lower()
        result_memes = []
        memes = MemeProcessor.store_get_memes()

        for meme in memes:
            if norm_keywords in memes[meme].keywords:
                result_memes.append(memes[meme])

        return result_memes


a = MemeProcessor.store_get_memes()
print(a)
