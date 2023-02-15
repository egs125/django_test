from django.urls import path, include
from .views import users
from . import views

urlpatterns = [
  path('', views.index, name='index'),

  path("users/", users),
  #path("<int:id>/", randomQuiz)
]