from api.views.user_list import UserModelViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.book_list import BookView

r = DefaultRouter()

r.register(r'users', UserModelViewSet, basename='users')


urlpatterns = [
    path('book/', BookView.as_view()),
    path('', include(r.urls)),
]

