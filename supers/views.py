from urllib import response
from super_types.models import SuperType
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
        super_types = request.query_params.get('type')
        supers = Supers.objects.all()
        if super_types: 
            supers = supers.filter(super_type__type=super_types)
            serializer = SuperSerializer(supers, many = True)
            return Response(serializer.data)
        else:
            all_supers = {}
            super_types = SuperType.objects.all()
            for superr in super_types:
                supers = Supers.objects.filter(super_type_id=superr.id)
                super_serializer = SuperSerializer(supers, many=True)
                all_supers[superr.type] = super_serializer.data
            return Response(all_supers)

    #Create 
    def post(self, request, format = None):
        serializer = SuperSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class SupersDetail(APIView):

    #Query supers given a primary key and return values 
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
        supers = self.get_object(pk)
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

