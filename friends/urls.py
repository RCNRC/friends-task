from django.contrib import admin
from django.urls import path, include, re_path
from accounts.views import (
    FriendshipRequestAPIView,
    FriendshipAcceptAPIView,
    FriendshipDeclineAPIView,
    FriendshipRemoveAPIView,
    FriendshipRequestsAPIView,
    FriendshipsAPIView,
    FriendshipStatusAPIView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/status/', FriendshipStatusAPIView.as_view()),
    path('api/v1/friendships/', FriendshipsAPIView.as_view()),
    path('api/v1/requests/', FriendshipRequestsAPIView.as_view()),
    path('api/v1/request/', FriendshipRequestAPIView.as_view()),
    path('api/v1/accept/', FriendshipAcceptAPIView.as_view()),
    path('api/v1/decline/', FriendshipDeclineAPIView.as_view()),
    path('api/v1/remove/', FriendshipRemoveAPIView.as_view()),

    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
