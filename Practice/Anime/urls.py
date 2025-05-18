from django.urls import path,include
from . import views

urlpatterns = [
     path('', views.listTweets,name="listTweets"),
     path('create/', views.createTweet,name="createTweet"),
     path('<int:tweet_id>/delete/', views.deleteTweet,name="deleteTweet"),
     path('<int:tweet_id>/edit/', views.editTweet,name="editTweet"),

] 