from urllib import response
from super_types.models import SuperType
from super_types.serializers import SuperTypeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class SuperTypeList(APIView):
    
    def get(self,request, format = None):
        super_type = SuperType.objects.all()
        serializer = SuperTypeSerializer(super_type, many = True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = SuperTypeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class SuperTypeDetail(APIView):

    def get_object(self, pk):
        try:
            return  SuperType.object.get(pk=pk)
        except:
            return Http404

    def get(self, request, pk, format = None):
        super_type = self.get_object(pk)
        serializer = SuperTypeSerializer(super_type)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        super_type = self.get_object(pk)
        serializer = SuperTypeSerializer(super_type, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk, format=None):
        super_type = self.get_object(pk)
        super_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)