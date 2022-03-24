import tweepy

Consumer_key = "vfy19WnfwMT7sSqBLGiqUv9aV"
Consumer_secret = "2vvXZhilZsm6EjkkdqpWtRf5Js1A4McuSx0enUvBqKsc8vFV2p"
Access_token = "1347438187472293888-0P3oYhijqgqibUzaZaO7HYEy1SXJXg"
Access_secret = "PVclQbjXUrDhJ7ImkbYe4z5LyZzhDv9A1G0Uv1jyGgM9t"
auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_token, Access_secret)

class TweeterMain:
  def __init__(self):


      self.api = tweepy.API(auth)

  def timeline_screen(self, user, num):
      friend_ids = []

      # タイムライン
      for friend_id in tweepy.Cursor(self.api.friends_ids, user_id=user).items(num):
          friend_ids.append(friend_id)


      return friend_ids

class Tweet:

   def __init__(self, num):
       self.t = TweeterMain()
       self.friend_ids = []
       self.num = num

   def get_timeline(self, name):


       for i in (self.t.timeline_screen(name, self.num)):
           #print(i)
           self.friend_ids.append(i)

       return self.friend_ids
