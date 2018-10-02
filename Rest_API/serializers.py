import json
from rest_framework import serializers
from jsonschema import validate  # validates incoming data against JSONSchema
from jsonschema.exceptions import ValidationError as JSONSchemaValidationError
from .models import Lesson

from .jsonschema import (
    notes_schema,
)


class JSONSchemaField(serializers.JSONField):
# Custom field that validates incoming data against JSONSchema, 
# Then, if successful, will store it as a string.

    def __init__(self, schema, *args, **kwargs):
        super(JSONSchemaField, self).__init__(*args, **kwargs)
        self.schema = schema

    def to_representation(self, obj):
        return json.loads(obj)

    def to_internal_value(self, data):
        try:
            validate(data, self.schema)
        except JSONSchemaValidationError as e:
            raise serializers.ValidationError(e.message)

        return super(JSONSchemaField, self).to_internal_value(json.dumps(data))


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    notes = JSONSchemaField(notes_schema)

    class Meta:
        model = Lesson
        fields = ('url', 'title', 'bpm', 'notes')
