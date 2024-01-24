from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class CreateInvoice(APIView):
    def get(self,request):
        queryset=Invoice.objects.all()
        serializer=InvoiceSerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            details=request.data.get('details',[])
            for detail in details:
                detail['invoice']=serializer.instance.id
                detail_serializer=InvoiceDetailSerializer(data=detail)
                if detail_serializer.is_valid():
                    detail_serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        