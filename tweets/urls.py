from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='tweets'),
    path('<int:tweet_id>/', views.tweet, name="tweet"),
    path('post/', views.post, name="post"),
    path('like/<int:tweet_id>/', views.like, name="like"),
    path('comment/<int:tweet_id>/', views.comment, name="comment"),
    path('retweet/<int:tweet_id>/', views.retweet, name="retweet"),
    path('following/', views.following, name='following_feed'),
    path('delete/<int:tweet_id>/', views.delete_tweet, name='delete_tweet'),
    path('delete/comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('search', views.search, name='search')
]
