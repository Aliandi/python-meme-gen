from api.meme_processor import MemeProcessor


class TestMemes:
    def test_process(self):
        processed_memes = MemeProcessor.store_get_memes()
        assert len(processed_memes) > 0
        assert len(processed_memes[0]['keywords']) > 0

    def test_get_keywords(self):
        keywords = MemeProcessor.get_meme_keywords('My meme name')
        for keyword in keywords:
            assert keyword in ['my', 'meme', 'name', 'my meme name']

    def test_memes_by_keyword(self):
        assert 'drake' in MemeProcessor.get_meme_by_keyword('drake')[0].name.lower()
