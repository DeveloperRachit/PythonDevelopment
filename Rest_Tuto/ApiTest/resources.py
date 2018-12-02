from tastypie.resources import ModelResource
from ApiTest.models import Note
from tastypie.authorization import Authorization
class NoteResource(ModelResource):
    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authorization=Authorization()
        fields = ['title','created_at', 'body']