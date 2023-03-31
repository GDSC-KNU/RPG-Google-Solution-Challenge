from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('init/', views.db_init),
    path('total/',views.search_all),
    path('search/',views.search_by_name),
    path('inference/',views.inference),
]