from django.db import models

class TweetData(models.Model):
   profile_image_url = models.TextField()
   user_name = models.TextField()

   def __str__(self):
       return self.user_name

class FriendID(models.Model):
    friend_id = models.TextField()

    def __str__(self):
        return self.friend_id

class FriendFriendID(models.Model):
    friend_friend_id = models.TextField()

    def __str__(self):
        return self.friend_friend_id
