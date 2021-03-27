from django.urls import path
from . import views


urlpatterns = [
    path('dashboard' , views.index, name="index"),
    # path('' , views.index, name="home"),
    path('delete/<int:id>' , views.delete),
    path('update/<int:id>' , views.update),
    path('upload' , views.simple_upload),
    path('login' , views.login_form),
    path('loginpath' , views.my_view),
    path('logout' , views.logout_view, name="logout"),
    path('' , views.landing, name="landing"),

    # path('population-chart/', views.population_chart, name='population-chart'),


]



