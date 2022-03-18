from urllib import response
from supers.models import Supers
from supers.serializers import SuperSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class SupersList(APIView):
    #Get all
    def get(self,request, format = None):
        supers = Supers.objects.all()
        serializer = SuperSerializer(supers, many = True)
        return Response(serializer.data)
    #Create 
    def post(self, request, format = None):
        serializer = SuperSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class SupersDetail(APIView):

    #Get Obj given a primary key and store it 
    def get_object(self, pk):
        try:
            return  Supers.objects.get(pk=pk)
        except:
            return Http404

    #Get a single object
    def get(self, request, pk, format = None):
        supers = self.get_object(pk)
        serializer = SuperSerializer(supers)
        return Response(serializer.data)

    #Update an object
    def put(self, request, pk, format=None):
        supers = self.get_object(pk)
        serializer = SuperSerializer(supers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self, request, pk, format=None):
        sup = self.get_object(pk)
        sup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

