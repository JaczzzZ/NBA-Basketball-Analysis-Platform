from django.urls import path

from . import views

urlpatterns = [
    path('', views.players, name='players'),
    path('playercreate/', views.playercreate, name='playercreate'),
    path('playerdelete/<int:pk>', views.playerdelete, name='playerdelete'),
    path('playeredit/<int:pk>', views.playeredit, name='playeredit'),
    path('teams/', views.teams, name='teams'),
    path('teamcreate/', views.teamcreate, name='teamcreate'),
    path('teamdelete/<int:pk>', views.teamdelete, name='teamdelete'),
    path('teamedit/<int:pk>', views.teamedit, name='teamedit'),
]