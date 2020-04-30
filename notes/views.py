from rest_framework import generics
from . import models
from . import serializers

#APIs using django rest_framework
class NoteList(generics.ListCreateAPIView):   #ListAPIView
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Note.objects.all()
    serializer_class = serializers.NoteSerializer