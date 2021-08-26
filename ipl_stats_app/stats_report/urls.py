from django.conf.urls import url
from stats_report import views
from django.urls import path, include
# from django.views.generic import TemplateView
# from django.contrib.auth.views import LogoutView
# from django.contrib.auth import logout

urlpatterns = [
        url(r'^home', views.home, name='index'),
        url(r'^top_4_teams', views.top_4_teams_win_season_wise, name='top_4_teams'),
        url(r'^top_toss_winner', views.top_most_toss_win_season_wise, name='top_toss_winner'),
        url(r'^max_player_of_match', views.max_player_of_match, name='max_player_of_match'),
        url(r'^top_winner_team_whole_season', views.top_winner_team_whole_season, name='top_winner_team_whole_season'),
        url(r'^top_location_winner_team_whole_season', views.top_location_top_team_whole_season, name='top_location_winner_team_whole_season'),
        url(r'^top_hosted_location_whole_season', views.top_hosted_location_all_season, name='top_hosted_location_whole_season'),
        url(r'^highest_margin_team_winner', views.highest_margin_run_team_winner, name='highest_margin_team_winner'),
        url(r'^highest_wicket_taker_team_winner', views.highest_wicket_taker_team_winner, name='highest_wicket_taker_team_winner'),
        url(r'^toss_winner_match_winner_team', views.toss_winner_and_match_winner_team, name='toss_winner_match_winner_team'),
        url(r'^percentage_team_and_toss_winner', views.percentage_team_and_toss_winner, name='percentage_team_and_toss_winner'),

]