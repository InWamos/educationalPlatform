from rest_framework import serializers
from courses.models import Subject

class SubjectSerializer(serializers.ModelField):
    class Meta:
        model = Subject
        fields = ["id", "title", "slug"]