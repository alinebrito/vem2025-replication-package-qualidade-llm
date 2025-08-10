class Solution:
    def __init__(self):
        self.users = {}
        self.tweets = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = {'follows': set(), 'tweets': []}
        self.users[userId]['tweets'].append(tweetId)
        self.tweets[tweetId] = userId

    def getNewsFeed(self, userId: int) -> list:
        if userId not in self.users:
            return []
        follows = self.users[userId]['follows'].copy()
        follows.add(userId)
        tweets = []
        for follow in follows:
            if follow in self.users:
                tweets.extend(self.users[follow]['tweets'][-10:])
        tweets = sorted(tweets, reverse=True)
        return tweets[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = {'follows': set(), 'tweets': []}
        self.users[followerId]['follows'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId]['follows'].discard(followeeId)