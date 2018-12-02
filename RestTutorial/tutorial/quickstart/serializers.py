from rest_framework import serializers
from quickstart.models import Quickstart, LANGUAGE_CHOICES, STYLE_CHOICES


class QuickstartSerializer(serializers.Serializer):
   class Meta:
        model = Quickstart
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')           