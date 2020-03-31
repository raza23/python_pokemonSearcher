from django.shortcuts import render
from rest_framework import viewsets
from .models import Pokemon
from .serializers import PokemonSerializer


class PokemonView(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

# Create your views here.
