from django.db import models

class Team(models.Model):
    name = models.CharField()
    acronym = 
    conference = 


class PlayerInfo(models.model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    home_country = models.CharField(max_length=30)
    weight = models.IntegerField()  #double check this is right
    height = models.IntegerField()  # double check this is right
    jersey_number = models.IntegerField()
    team = models.ForeignKey("Team")
    shooting_hand = models.CharField(max_length=30, choices=(("L", "Left"), ("R", "Right")))
#bplayer by listed on card but am not sure how to write it out correctly
    #birth_date = models.CharField()



#tbh dont remember where i was going with this one
    #player_name = models.CharField(max_length=6)
    #shooting_hand = models.CharField(max_length=1, choices = shooting_hand)


