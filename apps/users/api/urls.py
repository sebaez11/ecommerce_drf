# Django imports
from django.urls import path

# Views
from apps.users.api.views import UserAPIView, UserDetailAPIView

urlpatterns = [
    path(
        route='',
        view=UserAPIView.as_view(),
        name='users',
    ),

    path(
        route='<int:id>/',
        view=UserDetailAPIView.as_view(),
        name='user_detail_actions',
    ),
]
