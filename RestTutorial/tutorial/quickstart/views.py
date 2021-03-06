# from django.shortcuts import render

# # Create your views here.
# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from quickstart.serializers import UserSerializer, GroupSerializer


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from quickstart.models import Quickstart
from quickstart.serializers import QuickstartSerializer


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        quickstart = Quickstart.objects.all()
        serializer = QuickstartSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuickstartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Quickstart.objects.get(pk=pk)
    except Quickstart.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuickstartSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuickstartSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        quickstart.delete()
        return HttpResponse(status=204)        