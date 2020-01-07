from django.urls import path
from.import views
urlpatterns = [
    path('',views.home,name="home"),
    path('O_mnie.html',views.O_mnie,name="O_mnie"),

    ]