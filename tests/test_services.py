from src.services import TweetService, FollowService
from src.models import Tweet, Follow
from src.repositories import TweetRepository, FollowRepository

def test_post_tweet():
    tweet_repository = TweetRepository()
    tweet_service = TweetService(tweet_repository)
    tweet = Tweet(user_id="user123", content="Hello, Twitter!")

    tweet_service.post_tweet(tweet)

    assert tweet_repository.get_user_tweets("user123") == [tweet]

def test_get_user_tweets():
    tweet_repository = TweetRepository()
    tweet_service = TweetService(tweet_repository)
    user_id = "user123"
    tweet1 = Tweet(user_id=user_id, content="Tweet 1")
    tweet2 = Tweet(user_id=user_id, content="Tweet 2")

    tweet_repository.save_tweet(tweet1)
    tweet_repository.save_tweet(tweet2)

    user_tweets = tweet_service.get_user_tweets(user_id)

    assert user_tweets == [tweet2, tweet1]

def test_get_followers_tweets():
    tweet_repository = TweetRepository()
    tweet_service = TweetService(tweet_repository)
    follow_repository = FollowRepository()
    follow_service = FollowService(follow_repository)

    user_id = "user123"
    follower_id = "follower123"

    follow = Follow(follower_id=follower_id, following_id=user_id)
    follow_service.follow_user(follow)

    tweet1 = Tweet(user_id=user_id, content="Tweet 1")
    tweet2 = Tweet(user_id=follower_id, content="Tweet 2")

    tweet_repository.save_tweet(tweet1)
    tweet_repository.save_tweet(tweet2)

    followers_tweets = tweet_service.get_followers_tweets(user_id)

    assert followers_tweets == [tweet2]

def test_get_tweets_with_tag():
    tweet_repository = TweetRepository()
    tweet_service = TweetService(tweet_repository)
    user_id = "user123"
    tag = "python"
    tweet1 = Tweet(user_id=user_id, content="Tweet 1", tags=[tag])
    tweet2 = Tweet(user_id=user_id, content="Tweet 2")

    tweet_repository.save_tweet(tweet1)
    tweet_repository.save_tweet(tweet2)

    tagged_tweets = tweet_service.get_tweets_with_tag(user_id, tag)

    assert tagged_tweets == [tweet1]

def test_follow_user():
    follow_repository = FollowRepository()
    follow_service = FollowService(follow_repository)
    follow = Follow(follower_id="user456", following_id="user123")

    follow_service.follow_user(follow)

    assert follow_repository.get_user_followers("user123") == ["user456"]

def test_unfollow_user():
    follow_repository = FollowRepository()
    follow_service = FollowService(follow_repository)
    follow = Follow(follower_id="user456", following_id="user123")

    follow_service.unfollow_user(follow)

    assert follow_repository.get_user_followers("user123") == []

def test_get_user_followers():
    follow_repository = FollowRepository()
    follow_service = FollowService(follow_repository)
    user_id = "user123"
    follower1 = "follower1"
    follower2 = "follower2"

    follow1 = Follow(follower_id=follower1, following_id=user_id)
    follow2 = Follow(follower_id=follower2, following_id=user_id)

    follow_service.follow_user(follow1)
    follow_service.follow_user(follow2)

    user_followers = follow_service.get_user_followers(user_id)

    assert user_followers == [follower1, follower2]