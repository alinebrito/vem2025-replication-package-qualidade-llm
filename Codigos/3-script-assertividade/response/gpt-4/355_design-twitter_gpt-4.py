class Solution:
    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        if userId in self.following:
            for followee in self.following[userId]:
                if followee in self.tweets:
                    feed.extend(self.tweets[followee])
        if userId in self.tweets:
            feed.extend(self.tweets[userId])
        feed.sort(reverse=True)
        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)