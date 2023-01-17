from django.urls import path, include

from .views import homePageView

app_name='pages'
urlpatterns = [
    path('', homePageView, name='home'),
]