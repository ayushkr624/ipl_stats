from django.shortcuts import render
from .models import Deliveries,Matches
from django.db.models import Count,Max,Avg
import pandas as pd
from operator import itemgetter

# Create your views here.

def home(request):
    if request.method == 'POST':
        print("Inside home View")
        return render(request, 'index.html', context={"message": "Request has been accepted.", "values": None})

    elif request.method == 'GET':
        return render(request, 'index.html',  context={"message": "", "values": None})


def get_top_score(ipl_team, top_value):
    final_dict, count = {}, 0

    while (count < top_value):
        k, v = '', 0
        for i in range(len(ipl_team)):
            if ipl_team[i]:
                if i == 0:
                    pos, k, v = i, list(ipl_team[i].keys())[0], list(ipl_team[i].values())[0]
                else:
                    if list(ipl_team[i].values())[0] > v:
                        pos, k, v = i, list(ipl_team[i].keys())[0], list(ipl_team[i].values())[0]

        final_dict[k] = v
        del ipl_team[pos][k]
        count += 1

    return final_dict



def top_4_teams_win_season_wise(request):
    if request.method == 'POST':
        print("Inside top_4_teams_win_season_wise View")
        season = request.POST.get('Season')
        print(season)
        fetch_top_winner_team = list(Matches.objects.filter(season = season).values_list('winner', flat=True))
        print("fetch_top_winner_team", fetch_top_winner_team)
        teams_and_win_count = list(map(lambda letter: {letter: fetch_top_winner_team.count(letter)}, set(fetch_top_winner_team)))
        print(teams_and_win_count)

        retval = get_top_score(teams_and_win_count, 4)
        print("retval", retval)

        return render(request, 'top_4_teams_win.html',
                      context={"message": "Request has been accepted.Post Completion Mail be sent",
                               "values": retval})

    elif request.method == 'GET':
        return render(request, 'top_4_teams_win.html', context={"message": "", "values": None})


def top_most_toss_win_season_wise(request):
    if request.method == 'POST':
        print("Inside top_most_toss_win_season_wise View")
        season = request.POST.get('Season')
        print(season)
        top_toss_winner_team = list(Matches.objects.filter(season = season).values_list('toss_winner', flat=True))
        print("top_toss_winner_team", top_toss_winner_team)
        top_toss_winner_team_count = list(map(lambda letter: {letter: top_toss_winner_team.count(letter)}, set(top_toss_winner_team)))
        print("top_toss_winner_team_count", top_toss_winner_team_count)

        retval = get_top_score(top_toss_winner_team_count, 1)
        print("retval", retval)

        return render(request, 'top_most_toss_win.html', context={"message": "Request has been accepted.", "values": retval})

    elif request.method == 'GET':
        return render(request, 'top_most_toss_win.html', context={"message": "", "values": None})

def max_player_of_match(request):
    if request.method == 'POST':
        print("Inside max_player_of_match View")
        season = request.POST.get('Season')
        print(season)

        max_player_of_match_season = list(Matches.objects.filter(season = season).values_list('player_of_match', flat=True))
        print("max_player_of_match_season", max_player_of_match_season)
        print(list(map(lambda letter: {letter: max_player_of_match_season.count(letter)}, set(max_player_of_match_season))))
        player_of_match_count = list(map(lambda letter: {letter: max_player_of_match_season.count(letter)}, set(max_player_of_match_season)))
        print("player_of_match_count", player_of_match_count)

        retval = get_top_score(player_of_match_count, 1)
        print("retval", retval)

        return render(request, 'top_player_of_match.html', context={"message": "Request has been accepted.", "values": retval})

    elif request.method == 'GET':
        return render(request, 'top_player_of_match.html', context={"message": "", "values": None})

def top_winner_team_whole_season(request):
    if request.method == 'POST':
        print("Inside top_winner_team_whole_season View")
        season = request.POST.get('Season')
        print(season)
        fetch_top_winner_team = list(Matches.objects.filter(season = season).values_list('winner', flat=True))
        print(fetch_top_winner_team)
        teams_and_win_count = list(map(lambda letter: {letter: fetch_top_winner_team.count(letter)}, set(fetch_top_winner_team)))
        print(teams_and_win_count)

        retval = get_top_score(teams_and_win_count, 1)

        return render(request, 'top_winner_team_whole_season.html', context={"message": "Request has been accepted.", "values": retval})

    elif request.method == 'GET':
        return render(request, 'top_winner_team_whole_season.html', context={"message": "", "values": None})

def top_location_top_team_whole_season(request):
    if request.method == 'POST':
        print("Inside top_location_top_team_whole_season View")
        season = request.POST.get('Season')
        print(season)
        top_location_winner_team = list(Matches.objects.filter(season = season).values_list('winner', flat=True))
        print("top_location_winner_team", top_location_winner_team)
        teams_and_win_count = list(map(lambda letter: {letter: top_location_winner_team.count(letter)}, set(top_location_winner_team)))
        print(teams_and_win_count)

        retval = get_top_score(teams_and_win_count, 1)

        team_name, val = next(iter(retval.items()))
        print("team_name", team_name)
        fetch_top_location_season = list(Matches.objects.filter(winner=team_name, season = season).values_list('venue', flat=True))

        fetch_top_location_season_count = list(map(lambda letter: {letter: fetch_top_location_season.count(letter)}, set(fetch_top_location_season)))
        print(fetch_top_location_season_count)

        retval = get_top_score(fetch_top_location_season_count, 1)

        return render(request, 'location_top_winner.html', context={"message": "Request has been accepted.", "values": retval})

    elif request.method == 'GET':
        return render(request, 'location_top_winner.html', context={"message": "", "values": None})

def top_hosted_location_all_season(request):
    if request.method == 'POST':
        print("Inside top_hosted_location_all_season View")
        season = request.POST.get('Season')
        print(season)
        fetch_top_hosted_location = list(Matches.objects.filter(season = season).values_list('venue', flat=True))
        print("fetch_top_hosted_location", fetch_top_hosted_location)
        top_hosted_location_count = list(map(lambda letter: {letter: fetch_top_hosted_location.count(letter)}, set(fetch_top_hosted_location)))
        print(top_hosted_location_count)

        retval = get_top_score(top_hosted_location_count, 1)
        print("retval", retval)
        return render(request, 'top_hosted_location.html', context={"message": "Request has been accepted.", "values": retval})

    elif request.method == 'GET':
        return render(request, 'top_hosted_location.html', context={"message": "", "values": None})


def highest_margin_run_team_winner(request):
    if request.method == 'POST':
        print("Inside top_hosted_location_all_season View")
        season = request.POST.get('Season')
        print(season)

        highest_margin_winner_team = list(Matches.objects.all().filter(season= season).values('winner').annotate(max=Max('win_by_runs')))
        print("highest_margin_winner_team", highest_margin_winner_team)

        max_margin_team = max(highest_margin_winner_team, key=lambda x: x['max'])
        retval = dict([(max_margin_team['winner'], max_margin_team['max'])])
        print("retval", retval)

        return render(request, 'highest_margin_winner_team.html', context={"message": "Request has been accepted", "values": retval})

    elif request.method == 'GET':
        return render(request, 'highest_margin_winner_team.html', context={"message": "", "values": None})

def highest_wicket_taker_team_winner(request):
    if request.method == 'POST':
        print("Inside highest_wicket_taker_team_winner View")
        season = request.POST.get('Season')
        print(season)

        highest_margin_winner_team = list(Matches.objects.all().filter(season= season).values('winner').annotate(max=Max('win_by_wickets')))
        print("highest_margin_winner_team", highest_margin_winner_team)


        max_margin_team = max(highest_margin_winner_team, key=lambda x: x['max'])
        retval = dict([(max_margin_team['winner'], max_margin_team['max'])])
        print("retval", retval)

        return render(request, 'highest_wicket_taker_team.html', context={"message": "Request has been accepted", "values": retval})

    elif request.method == 'GET':
        return render(request, 'highest_wicket_taker_team.html', context={"message": "", "values": None})


def toss_winner_and_match_winner_team(request):
    if request.method == 'POST':
        print("Inside highest_wicket_taker_team_winner View")
        season = request.POST.get('Season')
        print(season)

        toss_winner_match_winner_team = list(Matches.objects.all().filter(season=season).values('winner','toss_winner'))
        print("toss_winner_match_winner_team", toss_winner_match_winner_team)

        winning_team = {}
        for i in range(len(toss_winner_match_winner_team)):
            # if winner and toss_winner match and winner is present in list, increment with one
            if toss_winner_match_winner_team[i]['winner'] == toss_winner_match_winner_team[i]['toss_winner']:
                winning_team[toss_winner_match_winner_team[i]['winner']] = winning_team.get(toss_winner_match_winner_team[i]['winner'], 0) + 1


        print("winning_team", winning_team)

        return render(request, 'toss_winner_match_winner_team.html',
                      context={"message": "Request has been accepted", "values": winning_team})

    elif request.method == 'GET':
        return render(request, 'toss_winner_match_winner_team.html', context={"message": "", "values": None})

def percentage_team_and_toss_winner(request):
    if request.method == 'POST':
        print("Inside highest_wicket_taker_team_winner View")
        season = request.POST.get('Season')
        print(season)

        toss_winner_batting_team = list(Matches.objects.all().filter(season=season).values('toss_winner','toss_decision'))
        print("toss_winner_batting_team", toss_winner_batting_team)

        toss_winner = {}
        toss_decision = {}

        for i in range(len(toss_winner_batting_team)):
            toss_winner[toss_winner_batting_team[i]['toss_winner']] = toss_winner.get(toss_winner_batting_team[i]['toss_winner'], 0) + 1
            if toss_winner_batting_team[i]['toss_decision'] == 'bat':
                toss_decision[toss_winner_batting_team[i]['toss_winner']] = toss_decision.get(toss_winner_batting_team[i]['toss_winner'], 0) + 1

        print("toss_winner", toss_winner)
        percentage = {}
        for key, val in toss_winner.items():
            if key in toss_decision:
                perc = (toss_decision[key] * 100) / val
                percentage[key] = perc

        print("winning_team", percentage)

        return render(request, 'percentage_toss_winner_team_winner.html',
                      context={"message": "Request has been accepted", "values": percentage})

    elif request.method == 'GET':
        return render(request, 'percentage_toss_winner_team_winner.html', context={"message": "", "values": None})

