from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.models import Employee
from ..models.serializers import EmployeeSerializer


class EmployeeView(APIView):

    def get(self, request, *args, **kwargs):
        result = Employee.objects.all()
        serializers = EmployeeSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        pass
