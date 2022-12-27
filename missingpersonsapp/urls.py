from django.urls import path
from .views import homePageView, addPageView, resourcesPageView, searchPageView, tablePageView
urlpatterns= [
    path('', homePageView, name="home"),
    path('add/', addPageView, name="add"),
    path('resources/', resourcesPageView, name="resources"),
    path("search/", searchPageView, name="search"),
    path('table/', tablePageView, name="table"),

]