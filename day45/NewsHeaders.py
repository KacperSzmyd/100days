class NewsHeader:
    def __init__(self, title_, link, score):
        self.title_ = title_
        self.link = link
        self.score = score

    def __str__(self) -> str:
        return f"Title: {self.title_}\nLink:{self.link}\nScore: {self.score}"
