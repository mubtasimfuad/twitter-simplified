from typing import List
from models import Tweet, Follow
from repositories import TweetRepository, FollowRepository


class TweetService:
    def __init__(self, tweet_repository: TweetRepository = TweetRepository()):
        self.tweet_repository = tweet_repository

    def post_tweet(self, tweet: Tweet):
        #   for posting a tweet
        self.tweet_repository.save_tweet(tweet)

    def get_user_tweets(self, user_id: str) -> List[Tweet]:
        #   for retrieving user's tweets
        return self.tweet_repository.get_user_tweets(user_id)

    def get_followers_tweets(self, user_id: str) -> List[Tweet]:
        #   for retrieving tweets from user's followers
        return self.tweet_repository.get_followers_tweets(user_id)

    def get_tweets_with_tag(self, user_id: str, tag: str) -> List[Tweet]:
        #   for retrieving tweets with a certain tag
        return self.tweet_repository.get_tweets_with_tag(user_id, tag)


class FollowService:
    def __init__(self, follow_repository: FollowRepository = FollowRepository()):
        self.follow_repository = follow_repository

    def follow_user(self, follow: Follow):
        #   for a user following another user
        self.follow_repository.follow_user(follow)

    def unfollow_user(self, follow: Follow):
        #   for a user unfollowing another user
        self.follow_repository.unfollow_user(follow)

    def get_user_followers(self, user_id: str) -> List[str]:
        #   for retrieving user's followers
        return self.follow_repository.get_user_followers(user_id)
