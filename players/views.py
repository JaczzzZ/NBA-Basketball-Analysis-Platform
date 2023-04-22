from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import *
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt


def players(request):
    playername = request.GET.get('playername', '')
    position = request.GET.get('position', '')
    team = request.GET.get('team', '')
    players = Player.objects.all()
    if playername:
        players = players.filter(name__icontains=playername)
    if position:
        players = players.filter(pos__icontains=position)
    if team:
        players = players.filter(tm__icontains=team)
    print(playername, position, team)
    paginator = Paginator(players, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'players/players.html', {
        'page_obj': page_obj,
        'playername': playername,
        'position': position,
        'team': team,
        'labels': Label.objects.all()
    })


@csrf_exempt
def teams(request):
    if request.method == 'POST':
        visit_team = request.POST.get('visit_team')
        home_team = request.POST.get('home_team')
        pred_model = request.POST.get('model')
        print(visit_team, home_team, pred_model)
        game = Game.objects.filter(
            visit_team=visit_team,
            home_team=home_team,
            pred_model=pred_model,
        )
        if len(game) != 1:
            return JsonResponse({
                'error': 'Cannot predict the result. Check the team names.'
            })
        else:
            return JsonResponse({
                'visit_win': int(game[0].visit_win * 1000) / 1000,
                'home_win': int(game[0].home_win * 1000) / 1000,
                'win_team': visit_team if game[0].visit_win > game[0].home_win else home_team
            })
    teams = Team.objects.all()
    paginator = Paginator(teams, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'players/teams.html', {
        'page_obj': page_obj
    })


def playercreate(request):
    from .forms import PlayerForm
    if request.method == 'POST':
        playerform = PlayerForm(request.POST)
        if playerform.is_valid():
            playerform.save()
            return HttpResponseRedirect(reverse('players'))
    else:
        playerform = PlayerForm()
    return render(request, 'players/form.html', {
        'formset': playerform,
        'title': 'New Player'
    })


def playeredit(request, pk):
    from .forms import PlayerForm
    obj = Player.objects.get(pk=pk)
    if request.method == 'POST':
        playerform = PlayerForm(request.POST, instance=obj)
        if playerform.is_valid():
            playerform.save()
            return HttpResponseRedirect(reverse('players'))
    else:
        playerform = PlayerForm(instance=obj)
    return render(request, 'players/form.html', {
        'formset': playerform,
        'title': 'Edit Player'
    })


def playerdelete(request, pk):
    player = Player.objects.get(pk=pk)
    player.delete()
    return HttpResponseRedirect(reverse('players'))


def teamcreate(request):
    from .forms import TeamForm
    if request.method == 'POST':
        teamform = TeamForm(request.POST)
        if teamform.is_valid():
            teamform.save()
            return HttpResponseRedirect(reverse('teams'))
    else:
        teamform = TeamForm()
    return render(request, 'players/form.html', {
        'formset': teamform,
        'title': 'New Team'
    })


def teamedit(request, pk):
    print(pk)
    from .forms import TeamForm
    obj = Team.objects.get(pk=pk)
    if request.method == 'POST':
        teamform = TeamForm(request.POST, instance=obj)
        if teamform.is_valid():
            teamform.save()
            return HttpResponseRedirect(reverse('teams'))
    else:
        teamform = TeamForm(instance=obj)
    return render(request, 'players/form.html', {
        'formset': teamform,
        'title': 'Edit Team'
    })


def teamdelete(request, pk):
    team = Team.objects.get(pk=pk)
    team.delete()
    return HttpResponseRedirect(reverse('teams'))
