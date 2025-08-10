class Solution:
class Twitter:
    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((next(self.timer), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        if userId in self.follows:
            for followeeId in self.follows[userId]:
                if followeeId in self.tweets:
                    feed.extend(self.tweets[followeeId])
        if userId in self.tweets:
            feed.extend(self.tweets[userId])
        feed.sort(reverse=True)
        return [tweet[1] for tweet in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)