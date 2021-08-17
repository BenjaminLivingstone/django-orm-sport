from django.shortcuts import render, redirect
from .models import League, Team, Player

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
		"bp_players": Player.objects.filter(curr_team__team_name="Penguins") , 
		#  se puede agregar la ubicacion, pero en esta situación basta con penguins curr_team__location="Boston"
		"icbc_players": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		"icbc_players": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		"acafl_players": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football",last_name="Lopez"),
		"f_players": Player.objects.filter(curr_team__league__sport="Football"),
		"s_teams":Team.objects.filter(curr_players__first_name="Sofia"),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")