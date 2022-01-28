from .views import PostList,PostDetail
from django.urls import path

urlpattern = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]
