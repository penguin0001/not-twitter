from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('profile/likes', views.profile, name='profile_likes'),
    path('profile/comments', views.profile, name='profile_comments'),
    path('profile/retweets', views.profile, name='profile_retweets'),
    path('settings/', views.settings, name='settings'),
    path('profile/<int:user_id>/', views.profile_public, name='profile_public'),
    path('profile/<int:user_id>/likes', views.profile_public, name='profile_public_likes'),
    path('profile/<int:user_id>/comments', views.profile_public, name='profile_public_comments'),
    path('profile/<int:user_id>/retweets', views.profile_public, name='profile_public_retweets'),
    path('follow/<int:user_id>', views.follow, name='follow'),
    path('followers/<int:user_id>', views.followers, name='followers'),
    path('following/<int:user_id>', views.following, name='following'),
    path('change-password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
]