from django.urls import path, include
from . import views

urlpatterns = [
    path('update_avatar/', views.UpdateAvatarView.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('', include('allauth.urls'))
]
