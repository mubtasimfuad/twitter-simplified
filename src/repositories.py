from typing import List
from models import Tweet, Follow


class TweetRepository:
    def __init__(self):
        # In-memory storage for tweets
        self.tweets = []

    def save_tweet(self, tweet: Tweet):
        #   to save the tweet in a data store
        self.tweets.append(tweet)

    def get_user_tweets(self, user_id: str) -> List[Tweet]:
        #   to retrieve user's tweets
        user_tweets = [tweet for tweet in self.tweets if tweet.user_id == user_id]
        return sorted(user_tweets, key=lambda x: x.created_at, reverse=True)

    def get_followers_tweets(self, user_id: str) -> List[Tweet]:
        #   to retrieve tweets from user's followers
        followers_tweets = [tweet for tweet in self.tweets if tweet.user_id == user_id]
        return sorted(followers_tweets, key=lambda x: x.created_at, reverse=True)

    def get_tweets_with_tag(self, user_id: str, tag: str) -> List[Tweet]:
        #   to retrieve tweets with a certain tag
        tagged_tweets = [
            tweet
            for tweet in self.tweets
            if tag in tweet.tags and tweet.user_id == user_id
        ]
        return sorted(tagged_tweets, key=lambda x: x.created_at, reverse=True)


class FollowRepository:
    def __init__(self):
        # In-memory storage for follow relationships
        self.follows = []

    def follow_user(self, follow: Follow):
        #   to record a user following another user
        self.follows.append(follow)

    def unfollow_user(self, follow: Follow):
        #  to remove a user following another user
        self.follows = [
            f
            for f in self.follows
            if not (
                f.follower_id == follow.follower_id
                and f.following_id == follow.following_id
            )
        ]

    def get_user_followers(self, user_id: str) -> List[str]:
        # to retrieve user's followers
        user_followers = [
            follow.follower_id
            for follow in self.follows
            if follow.following_id == user_id
        ]
        return user_followers
