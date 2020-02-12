from meme_requests import MemeWrapper


class MemeProcessor:

    @staticmethod
    def get_meme_id(name: str):
        memes = MemeWrapper.get_memes()

