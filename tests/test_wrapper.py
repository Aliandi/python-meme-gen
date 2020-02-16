from api.meme_requests import MemeRequests


class TestMemes:
    def test_create(self):
        response = MemeRequests.create_meme('165198998', text_down='its not nice code, but it is code')
        assert response['success']

    def test_get(self):
        response = MemeRequests.get_memes()
        assert response['success']
