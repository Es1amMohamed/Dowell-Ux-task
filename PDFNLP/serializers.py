from rest_framework import serializers
from .models import ExtractedData


class ExtractedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedData
        fields = ["username", "email", "pdf_file", "nouns", "verbs"]
        read_only_fields = ["nouns", "verbs"]
