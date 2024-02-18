from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import BookSerializer

from book.models import Books


class BookViewSetView(viewsets.ViewSet):

    def create(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def list(sels,reuest,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,requets,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        serializer=BookSerializer(qs)
        return Response(data=serializer.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        print(qs)
        serializer=BookSerializer(data=request.POST,instance=qs)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.get(id=id).delete()
        return Response(data={"message":"deleted !!"})  
        