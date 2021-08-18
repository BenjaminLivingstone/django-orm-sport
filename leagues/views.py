from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count
from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_leagues": League.objects.filter(name__contains='baseball'),
		"women_leagues": League.objects.filter(name__contains='women'),
		"hockey_leagues": League.objects.filter(name__contains='hockey'),
		"other_than_football": League.objects.exclude(name__contains='football'),
		"conference_leagues": League.objects.filter(name__contains='conference'),
		"atlantic_leagues": League.objects.filter(name__contains='atlantic'),
		"dallas_teams": Team.objects.filter(location__contains='dallas'),
		"raptor_teams": Team.objects.filter(team_name__contains='raptors'),
		"city_teams": Team.objects.filter(location__contains='city'),
		"t_teams": Team.objects.filter(team_name__startswith='t'),
		"location_order_teams": Team.objects.all().order_by('location'),
		"inv_location_order_teams": Team.objects.all().order_by('-location'),
		"cooper_players": Player.objects.filter(last_name__contains='cooper'),
		"joshua_players": Player.objects.filter(first_name__contains='joshua'),
		"exclude_joshua_from_coopers": Player.objects.filter(last_name__contains="cooper").exclude(first_name__contains="joshua"),
		"alexanderorwyatt": Player.objects.filter(first_name="Alexander") | Player.objects.filter(first_name="Wyatt"),
		
		#Sports ORM II
		"asc_teams": Team.objects.filter(league__name="Atlantic Soccer Conference"),
		"bp_players": Player.objects.filter(curr_team__team_name="Penguins", curr_team__location="Boston") , 
		"icbc_players": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		"icbc_players": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		"acafl_players": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football",last_name="Lopez"),
		"f_players": Player.objects.filter(curr_team__league__sport="Football"),
		"s_teams": Team.objects.filter(curr_players__first_name="Sophia"),
		"s_teams": Team.objects.filter(curr_players__first_name="Sophia"),
		"flores_players": Player.objects.filter(last_name__contains="Flores").exclude(curr_team__team_name="Roughriders",curr_team__location="Washington"),
		"se_teams": Team.objects.filter(all_players__first_name = "Samuel", all_players__last_name = "Evans"),
		"tc_players": Player.objects.filter(all_teams__team_name = "Tiger-Cats", all_teams__location = "Manitoba"),
		"wv_players": Player.objects.filter(all_teams__team_name = "Vikings", all_teams__location = "Wichita").exclude(curr_team__team_name = "Vikings", curr_team__location = "Wichita"),
        "jg_teams": Team.objects.filter(all_players__first_name = "Jacob", all_players__last_name = "Gray").exclude(team_name = "Colts", location = "Oregon"),
        "j_players": Player.objects.filter(first_name = "Joshua", all_teams__league__name = "Atlantic Federation of Amateur Baseball Players"),
        "12_teams": Team.objects.annotate(x = Count('all_players')).filter(x__gt=11),
        "p_players": Player.objects.annotate(x = Count('all_teams')).order_by('-x'),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")