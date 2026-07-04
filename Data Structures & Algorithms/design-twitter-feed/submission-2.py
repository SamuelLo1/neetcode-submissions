from collections import deque
import heapq
class Twitter:
    

    class User(object): 

        def __init__(self,userId): 
            self.Id = userId
            self.friends = set()
            self.tweets = deque()
            self.friends.add(userId)
    """
    - stores users
    global time: keeps track of date on each post
    assuming that posts cannot be posted at the same time
    create each post with a time. This way we would merge posts together judging by time
    
    have a dictionary of users : {
        user : {
            friends : {}
            tweets : [] deque()
        }
    }

    """
    def __init__(self):
        self.users = {}
        self.postTime = 0
        self.feedCap = 10

    def getUserObj(self, userId): 
        if (userId not in self.users):
            self.users[userId] = self.User(userId)
        return self.users[userId]
  
    def postTweet(self, userId, tweetId):
        currUser = self.getUserObj(userId)
        currUser.tweets.appendleft([self.postTime, tweetId])
        self.postTime += 1
        print(currUser.tweets)
    """

    - Mappings of tweets to users
    - Queue ? most recent

    - current user
        - Id
        - followerIds
            - getTweets
    
    fetch at most: 10 most recent tweet IDs 
        - each tweet posted by following users other than self
        - ordered most recent to least 

    """
    def getNewsFeed(self, userId):
        currUser = self.getUserObj(userId)
        feed = []
        heapq.heapify(feed)
        for friend in currUser.friends: 
            print(friend)
            currFriend = self.users[friend]
            for tweet in currFriend.tweets: 
                #maintain heap of size 10
                if (len(feed) >= self.feedCap): 
                    if (tweet[0] > feed[0][0]): 
                        heapq.heappop(feed)
                        heapq.heappush(feed, tweet)
                    else: 
                        continue
                else: 
                    heapq.heappush(feed, tweet)
                    
        #get the 10 most recent posts
        feedIds = []
        while feed: 
            feedIds.append(heapq.heappop(feed)[1])
        return feedIds[::-1]
       
        
        
    """
    one user follows another user
    """
    def follow(self, followerId, followeeId):
        currUser = self.getUserObj(followerId)
        currUser.friends.add(followeeId)

    """
    remove user from followed
    """
    def unfollow(self, followerId, followeeId):
        if (followerId == followeeId): 
            return
        currUser = self.getUserObj(followerId)
        if (followeeId in currUser.friends):
            currUser.friends.remove(followeeId)

def main(): 
    newClient = Twitter() 
    newClient.follow(1,4)
    newClient.postTweet(4,30)
    newClient.postTweet(1,20)
    newClient.postTweet(4,50)
    newClient.postTweet(1,60)
    newClient.postTweet(4,10)
    newClient.getNewsFeed(1)
main()
    