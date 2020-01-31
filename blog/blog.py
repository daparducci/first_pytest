class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __str__(self):
        return f"Blog {self.title}, {self.author}, {self.posts}"

    def __repr__(self):
        return f"<Blog{self.title}, {self.author}, {self.posts}"

    def create_post(self, title, content):
        pass

    def json(self):
        pass