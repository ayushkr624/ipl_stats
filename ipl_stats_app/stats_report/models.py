from django.db import models
import datetime
from datetime import date



# Create your models here.
class Matches(models.Model):
    season = models.IntegerField(max_length=4, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(null=True)
    team1 = models.CharField(max_length=50, blank=True, null=True)
    team2 = models.CharField(max_length=50, blank=True, null=True)
    toss_winner = models.CharField(max_length=50, blank=True, null=True)
    toss_decision = models.CharField(max_length=5, blank=True, null=True)
    result = models.CharField(max_length=10, blank=True, null=True)
    dl_applied = models.BooleanField(default=0)
    winner = models.CharField(max_length=50, blank=True, null=True)
    win_by_runs = models.IntegerField(max_length=4, null=True)
    win_by_wickets = models.IntegerField(max_length=2, null=True)
    player_of_match = models.CharField(max_length=50, blank=True, null=True)
    venue = models.CharField(max_length=100, blank=True, null=True)
    umpire1 = models.CharField(max_length=50, blank=True, null=True)
    umpire2 = models.CharField(max_length=50, blank=True, null=True)
    umpire3 = models.CharField(max_length=50, blank=True, null=True)



#match_id	inning	batting_team	bowling_team	over	ball	batsman	non_striker	bowler	is_super_over	wide_runs	bye_runs	legbye_runs	noball_runs	penalty_runs	batsman_runs	extra_runs	total_runs	player_dismissed	dismissal_kind	fielder

class Deliveries(models.Model):
    match_id = models.ForeignKey(Matches,null=True,on_delete=models.CASCADE )
    inning = models.IntegerField(max_length=2, null=True)
    batting_team = models.CharField(max_length=50, blank=True, null=True)
    bowling_team = models.CharField(max_length=50, blank=True, null=True)
    over = models.IntegerField(max_length=2, null=True)
    ball = models.IntegerField(max_length=2, null=True)
    batsman = models.CharField(max_length=50, blank=True, null=True)
    non_striker = models.CharField(max_length=50, blank=True, null=True)
    bowler = models.CharField(max_length=5, blank=True, null=True)
    is_super_over = models.BooleanField(default=0)
    wide_runs = models.IntegerField(max_length=2, null=True)
    bye_runs = models.IntegerField(max_length=2, null=True)
    legbye_runs = models.IntegerField(max_length=2, null=True)
    noball_runs = models.IntegerField(max_length=2, null=True)
    penalty_runs = models.IntegerField(max_length=2, null=True)
    batsman_runs = models.IntegerField(max_length=3, null=True)
    extra_runs = models.IntegerField(max_length=2, null=True)
    total_runs = models.IntegerField(max_length=2, null=True)
    player_dismissed = models.CharField(max_length=50, blank=True, null=True)
    dismissal_kind = models.CharField(max_length=10, blank=True, null=True)
    fielder = models.CharField(max_length=50, blank=True, null=True)