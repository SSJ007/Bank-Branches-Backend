from django.contrib import admin
from django.urls import path
from . import views
from .views import BranchesListAPIView, BanksListAPIView, BranchesAutoCompleteListAPIView, BranchesCityAPIView

urlpatterns = [
    path('api/branches', BranchesListAPIView.as_view() ,name="branch"),
    path('api/branches/autocomplete', BranchesAutoCompleteListAPIView.as_view() ,name="branch_auto"),
    path('api/banks', BanksListAPIView.as_view() ,name="bank"),
    path('api/branches/', BranchesCityAPIView.as_view() ,name="branch_city"),
]
