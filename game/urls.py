from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_board, name='game_board'),
    path('question/<int:question_id>/', views.reveal_question, name='reveal_question'),
    path('host_panel/', views.host_panel, name='host_panel'),
    path('get_current_question/', views.get_current_question, name='get_current_question'),
    path('set_current_question/<int:question_id>/', views.set_current_question, name='set_current_question'),
    path('update_score/<int:player_id>/<int:question_id>/<int:correct>/', views.update_score, name='update_score'),
    path('place_wager/<int:player_id>/<int:question_id>/<int:amount>/', views.place_wager, name='place_wager'),
]