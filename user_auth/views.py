from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from django.http import HttpResponse
from django.views.generic import View
from .models import TweetData, FriendID, FriendFriendID
import tweepy
import random


@login_required
def top_page(request):
    user = UserSocialAuth.objects.filter(user_id=request.user.id)[0]

    # return render(request,'user_auth/top.html',{'user': user})


    Consumer_key = "vfy19WnfwMT7sSqBLGiqUv9aV"
    Consumer_secret = "2vvXZhilZsm6EjkkdqpWtRf5Js1A4McuSx0enUvBqKsc8vFV2p"
    # Access_token = "1347438187472293888-0P3oYhijqgqibUzaZaO7HYEy1SXJXg"
    # Access_secret = "PVclQbjXUrDhJ7ImkbYe4z5LyZzhDv9A1G0Uv1jyGgM9t"
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    # auth.set_access_token(Access_token, Access_secret)

    # session = []
    # session.append(auth.request_token['oauth_token'])
    # verifier = request.GET.get('oauth_verifier')

    # auth.request_token = { 'oauth_token' : user.access_token.oauth_token,
                             # 'oauth_token_secret' : user.access_token.oauth_token_secret }

    # try:
        # auth.get_access_token(verifier)
    # except tweepy.TweepError:
        # print('Error! Failed to get access token.')

    key = user.access_token.oauth_token
    secret = user.access_token.oauth_token_secret

    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(key, secret)

    api = tweepy.API(auth)

    u = request.user.id

    friend_ids = []
    friend_friend_ids = []
    user_names = []
    profile_image_urls = []


    for friend_id in tweepy.Cursor(api.friends_ids, user_id=u).items():
        friend_ids.append(friend_id)

    for friend_id_random in random.sample(friend_ids, 5):
        try:
            for friend_friend_id in tweepy.Cursor(api.friends_ids, user_id=friend_id_random).items():
                friend_friend_ids.append(friend_friend_id)
        except tweepy.error.TweepError:
            print("user not found")

    for k in random.sample(friend_friend_ids, 1):
        try:
            for user in api.lookup_users(user_id=k):
                user_names.append(user.name)
                profile_image_urls.append(user.profile_image_url_https)
        except tweepy.error.TweepError:
            print("user not found")

    # for user_name in random.sample(user_names, 5):
         # TweetData.objects.create(user_name=user_name)
    # for profile_image_url in random.sample(profile_image_urls, 5):
         # TweetData.objects.create(profile_image_url=profile_image_url)

    return render(request, 'base.xml', {'user_names':user_names, 'profile_image_urls':profile_image_urls})
