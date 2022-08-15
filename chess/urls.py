from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import SignUpView


urlpatterns = [
    path('', views.games, name='games'),
    path('success/', views.success, name='success'),
    path('<int:game_id>/', views.game, name='game'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("play/", views.play, name="play"),
    path("test/", views.test, name="test")
]

urlpatterns += staticfiles_urlpatterns()
