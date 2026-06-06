import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId : [count, tweetId]
        self.followingMap = defaultdict(set) # userId: [followeeId] 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.followingMap[userId].add(userId)
        for followerid in self.followingMap[userId]:
            if followerid in self.tweetMap:
                index = len(self.tweetMap[followerid]) - 1
                while index > -1:
                    count, tweetId = self.tweetMap[followerid][index]
                    heap.append([count, tweetId])
                    index -= 1
        heapq.heapify(heap)
        while heap and len(res) < 10:
            count, tweetId = heapq.heappop(heap)
            res.append(tweetId)
        return res
        
                

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingMap[followerId]:
            self.followingMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)