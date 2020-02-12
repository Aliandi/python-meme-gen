from meme_requests import MemeWrapper


class TestMemes:
    def test_create(self):
        response = MemeWrapper.create_meme('165198998', text_down='its not nice code, but it is code')
        print(response)
        assert response['success']
