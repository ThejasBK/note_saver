from rest_framework import serializers
from . import models

#Converting data to json
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        fields = '__all__'