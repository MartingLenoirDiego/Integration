from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.games, name='games'),
    path('<int:game_id>/', views.game, name='game'),

]

urlpatterns += staticfiles_urlpatterns()