class Solution:
    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = {}
        self.followees = defaultdict(set)

    def postTweet(self, userId, tweetId):
        time = next(self.timer)
        self.tweets[time] = (userId, tweetId)

    def getNewsFeed(self, userId):
        feed = []
        i = 0
        for time, (uid, tweetId) in sorted(self.tweets.items()):
            if uid == userId or uid in self.followees[userId]:
                feed.append(tweetId)
                i += 1
            if i == 10:
                break
        return feed

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)
