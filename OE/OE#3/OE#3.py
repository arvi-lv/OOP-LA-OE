class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class igAccount(SocialMediaAccount):
    def __init__(self, username, password, followers):
        super().__init__(username, password)
        self.followers = followers

    def share_story(self):
        pass

class xAccount(SocialMediaAccount):
    def __init__(self, username, password, tweets):
        super().__init__(username, password)
        self.tweets = tweets

    def post_tweet(self):
        pass

user1 = igAccount("ewam", "ayaw", 69)
user2 = xAccount("ganonba", "wagbes", 10)