from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .tw import Tweet
from .models import TweetData, FriendID, FriendFriendID
import tweepy
import random
import webbrowser
import urllib
import mojimoji


class TWU(View):

    # def get_oauth_token(url:str)->str:
        # querys = urllib.parse.urlparse(url).query
        # querys_dict = urllib.parse.parse_qs(querys)
        # return querys_dict["oauth_token"][0]

    def get(self, request, user_id, access_token, access_token_secret):

       Consumer_key = "vfy19WnfwMT7sSqBLGiqUv9aV"
       Consumer_secret = "2vvXZhilZsm6EjkkdqpWtRf5Js1A4McuSx0enUvBqKsc8vFV2p"
       Access_token = access_token
       Access_secret = access_token_secret
       auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
       auth.set_access_token(access_token, access_token_secret)

       # try:
           # redirect_url = auth.get_authorization_url()
       # except tweepy.TweepError:
           # print('Error! Failed to get request token.')

       # oauth_token = self.get_oauth_token(redirect_url)
       # print("oauth_token:", oauth_token)
       # auth.request_token['oauth_token'] = oauth_token

       # Please confirm at twitter after login.
       # webbrowser.open(redirect_url)

       # verifier = input("You can check Verifier on url parameter. Please input Verifier:")
       # auth.request_token['oauth_token_secret'] = verifier

       # try:
           # auth.get_access_token(verifier)
       # except tweepy.TweepError:
           # print('Error! Failed to get access token.')

       # key = auth.access_token
       # secret = auth.access_token_secret

       # auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
       # auth.set_access_token(key, secret)

       api = tweepy.API(auth)
       # api.update_status('tweepy + oauth!')

       # self.api = tweepy.API(auth)

       u = user_id

       friend_ids = []
       follower_ids = []
       ff_ids = []
       ff_ids_random = []
       each_ff_ids = [[],[],[],[],[],[],[],[],[],[]]
       each_ff_ids_random = [[],[],[],[],[],[],[],[],[],[]]
       then_ff_ids = []
       # user_ids = []
       user_names = [[],[],[],[],[],[],[],[],[],[]]
       profile_image_urls = [[],[],[],[],[],[],[],[],[],[]]
       screen_names = [[],[],[],[],[],[],[],[],[],[]]
       then_user_names = []
       then_profile_image_urls = []
       then_screen_names = []
       # descriptions = []

       try:
           for friend_id in tweepy.Cursor(api.friends_ids, user_id=u).items():
               friend_ids.append(friend_id)
           for follower_id in tweepy.Cursor(api.followers_ids, user_id=u).items():
               follower_ids.append(follower_id)
       except tweepy.error.TweepError:
           print("user not found")

       for friend_id in friend_ids:
           for follower_id in follower_ids:
               if friend_id == follower_id:
                   ff_ids.append(friend_id)
       if len(ff_ids) >= 10:
           for ff_id in random.sample(ff_ids, 10):
               ff_ids_random.append(ff_id)
       else:
           for ff_id in ff_ids:
               ff_ids_random.append(ff_id)

       for i, ff_id in enumerate(ff_ids_random):
           then_ff_ids.append(ff_id)
           ff_friend_ids = []
           ff_follower_ids = []
           ff_ff_ids = []
           ff_ff_ids_random = []
           try:
               for ff_friend_id in tweepy.Cursor(api.friends_ids, user_id=ff_id).items():
                   ff_friend_ids.append(ff_friend_id)
               for ff_follower_id in tweepy.Cursor(api.followers_ids, user_id=ff_id).items():
                   ff_follower_ids.append(ff_follower_id)
           except tweepy.error.TweepError:
               print("user not found")

           for ff_friend_id in ff_friend_ids:
               for ff_follower_id in ff_follower_ids:
                   if ff_friend_id == ff_follower_id:
                       ff_ff_ids.append(ff_friend_id)

           for ff_id2 in ff_ids:
               for ff_ff_id in ff_ff_ids:
                   if ff_id2 == ff_ff_id:
                       each_ff_ids[i].append(ff_id2)

       for i, each_ff_id in enumerate(each_ff_ids):
           if len(each_ff_id) >= 10:
               for each_ff_id2 in random.sample(each_ff_id, 10):
                   each_ff_ids_random[i].append(each_ff_id2)
           else:
               for each_ff_id2 in each_ff_id:
                   each_ff_ids_random[i].append(each_ff_id2)

       for i, each_ff_id in enumerate(each_ff_ids_random):
           for each_ff_id2 in each_ff_id:
               try:
                   user = api.get_user(id=each_ff_id2)
                   user_names[i].append(mojimoji.han_to_zen(user.name))
                   profile_image_urls[i].append(user.profile_image_url)
                   screen_names[i].append(user.screen_name)
               except tweepy.error.TweepError:
                   print("user not found")

       for then_ff_id in then_ff_ids:
           try:
               user = api.get_user(id=then_ff_id)
               then_user_names.append(mojimoji.han_to_zen(user.name))
               then_profile_image_urls.append(user.profile_image_url)
               then_screen_names.append(user.screen_name)
           except tweepy.error.TweepError:
               print("user not found")

       # for k in random.sample(friend_friend_ids, 4):
       #     try:
       #  #       for user in api.lookup_users(user_id=k):
       #          user = api.get_user(id=k)
       #          user_ids.append(user.id)
       #          user_names.append(mojimoji.han_to_zen(user.name))
       #          profile_image_urls.append(user.profile_image_url)
       #          descriptions.append(mojimoji.han_to_zen(user.description))
       #     except tweepy.error.TweepError:
       #         print("user not found")

       # for user_name in random.sample(user_names, 5):
            # TweetData.objects.create(user_name=user_name)
       # for profile_image_url in random.sample(profile_image_urls, 5):
            # TweetData.objects.create(profile_image_url=profile_image_url)

       return render(request, 'base.xml', {'user_name0':user_names[0], 'user_name1':user_names[1], 'user_name2':user_names[2], 'user_name3':user_names[3], 'user_name4':user_names[4], 'user_name5':user_names[5], 'user_name6':user_names[6], 'user_name7':user_names[7], 'user_name8':user_names[8], 'user_name9':user_names[9], 'profile_image_url0':profile_image_urls[0], 'profile_image_url1':profile_image_urls[1], 'profile_image_url2':profile_image_urls[2], 'profile_image_url3':profile_image_urls[3], 'profile_image_url4':profile_image_urls[4], 'profile_image_url5':profile_image_urls[5], 'profile_image_url6':profile_image_urls[6], 'profile_image_url7':profile_image_urls[7], 'profile_image_url8':profile_image_urls[8], 'profile_image_url9':profile_image_urls[9], 'screen_name0':screen_names[0], 'screen_name1':screen_names[1], 'screen_name2':screen_names[2], 'screen_name3':screen_names[3], 'screen_name4':screen_names[4], 'screen_name5':screen_names[5], 'screen_name6':screen_names[6], 'screen_name7':screen_names[7], 'screen_name8':screen_names[8], 'screen_name9':screen_names[9], 'then_user_names':then_user_names, 'then_profile_image_urls':then_profile_image_urls, 'then_screen_names':then_screen_names})
