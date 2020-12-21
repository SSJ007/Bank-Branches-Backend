from django.shortcuts import render
from django.db.models import Q
from .models import Branches, Banks
from .serializers import BranchesSerializer, BanksSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class BranchesListAPIView(ListAPIView):
    def get_queryset(self):
        if ('q' in self.request.GET):
            if ('city' in self.request.GET):
                res= self.request.query_params['q']
                res2= self.request.query_params['city']
                return Branches.objects.filter(Q(city__icontains=res2) & (Q(ifsc__icontains=res) | Q(branch__icontains=res)  | Q(address__icontains=res) | Q(city__icontains=res) | Q(district__icontains=res) | Q(state__icontains=res)))
            else:
                res= self.request.query_params['q']
                return Branches.objects.filter(Q(ifsc__icontains=res) | Q(branch__icontains=res)  | Q(address__icontains=res) | Q(city__icontains=res) | Q(district__icontains=res) | Q(state__icontains=res) ).order_by('ifsc')
        else:
            return Branches.objects.all()
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(BranchesListAPIView, self).dispatch(*args, **kwargs)

class BranchesAutoCompleteListAPIView(ListAPIView):
    def get_queryset(self):
        if ('q' in self.request.GET):
            res= self.request.query_params['q']
            return Branches.objects.filter(branch__istartswith=res).order_by('ifsc')
        else:
            return Branches.objects.all()
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(BranchesAutoCompleteListAPIView, self).dispatch(*args, **kwargs)

class BanksListAPIView(ListAPIView):
    def get_queryset(self):
        if ('q' in self.request.GET):
            res= self.request.query_params['q']
            return Banks.objects.filter(name__icontains=res)
        else:
            return Banks.objects.all()
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer
    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(BanksListAPIView, self).dispatch(*args, **kwargs)

class BranchesCityAPIView(ListAPIView):
    def get_queryset(self):
        if ('city' in self.request.GET):
            res= self.request.query_params['city']
            return Branches.objects.filter(city__icontains=res)
        else:
            return Branches.objects.all()
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(BranchesCityAPIView, self).dispatch(*args, **kwargs)
