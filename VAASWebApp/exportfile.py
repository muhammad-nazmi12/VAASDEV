from rest_framework import serializers
from django.db import models
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Document
        fields=('filename','document')
        