from django.urls import path

from . import views

app_name = "prices"

urlpatterns = [
    path("", views.home, name="home"),
    path("items/<int:pk>/", views.item_detail, name="item_detail"),
    path("report/", views.report_price, name="report_price"),
]