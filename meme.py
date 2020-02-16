class Meme:
    id: str
    name: str
    keywords: [str]

    def __init__(self, id: str, name: str, keywords: [str]):
        self.id = id
        self.name = name
        self.keywords = keywords
