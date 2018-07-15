from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
import csv
from rest_framework.renderers import JSONRenderer
from .serializers import PlayerSerializer, DetailsSerializer

class players(APIView):

    def get(self, request):
        players = {'players':[]}
        with open('players.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[32]!="name":
                    players['players'].append(row[32])
                else:
                    pass
        players=PlayerSerializer(players)
        return Response(players.data)

class details(APIView):

    def get(self, request, pk):
        
        with open('players.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[9]+" "+row[10]==pk:
                    #details['details'].append(row)
                    details ={'details':row}
                    details = DetailsSerializer(details)
                    
        return Response(details.data)

def index(request):

    return render(request, 'index.html')
