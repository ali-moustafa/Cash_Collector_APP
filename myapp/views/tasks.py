from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from ..models.models import Task, Employee
from ..models.serializers import TaskSerializer


from datetime import datetime
import os


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.employee.role == 'MG'


class IsCollector(BasePermission):
    def has_permission(self, request, view):
        return request.user.employee.role == 'CC'


class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsManager, IsCollector]

    def get_permissions(self):
        if self.action == 'get_all_tasks' and self.request.method == 'GET':
            return [permissions.IsAuthenticated(), IsManager()]
        elif (self.action in ['get_collector_done_tasks', 'get_collector_next_task'] and self.request.method == 'GET')\
                or (self.action in ['patch_collect', 'patch_deliver'] and self.request.method == 'PATCH'):
            return [permissions.IsAuthenticated(), IsCollector()]
        return [permissions.IsAuthenticated()]

    @action(detail=True, methods=['get'])
    def get_all_tasks(self, request):
        result = Task.objects.all()
        serializers = TaskSerializer(result, many=True)
        return Response({'status': 'success', "tasks": serializers.data}, status=200)

    def get_collector_done_tasks(self, request):
        user_id = Employee.objects.get(user=request.user)
        result = Task.objects.filter(collector=user_id.id, delivered=True)
        serializers = TaskSerializer(result, many=True)
        return Response({'status': 'success', "tasks": serializers.data}, status=200)

    def get_collector_next_task(self, request):
        user_id = Employee.objects.get(user=request.user)
        result = Task.objects.filter(collector=user_id.id, collected=False).order_by('amount_due_at').first()
        serializers = TaskSerializer(result, many=False)
        return Response({'status': 'success', "tasks": serializers.data}, status=200)

    def get_collector_status(self, request):
        cash_collector_id = request.GET.get("cash_collector", None)
        try:
            employee_obj = Employee.objects.get(id=cash_collector_id)
            user_obj = employee_obj.user
        except Exception:
            return Response({'status': 'Failed', "data": f"NO User found with ID '{cash_collector_id}'"}, status=404)

        result = Task.objects.filter(collector=cash_collector_id, collected=True, delivered=False).order_by('amount_due_at')
        if not result:
            return Response({'status': 'Failed', "data": f"NO tasks found for user '{user_obj.username}'"}, status=404)

        serializers = TaskSerializer(result, many=True)
        collected_tasks = serializers.data
        collected_amount = 0
        first_due_time = None
        collector_status = 'Not Frozen'
        for t in collected_tasks:
            collected_amount = collected_amount + float(t['amount_due'])
            if collected_amount >= float(os.environ.get('AMOUNT_THRESHOLD', 5000)):
                current_time = datetime.now()
                if first_due_time is None:
                    first_due_time = datetime.strptime(t['amount_due_at'], '%Y-%m-%dT%H:%M:%SZ')

                time_diff = current_time - first_due_time
                time_diff_seconds = time_diff.total_seconds()
                time_diff_hours = int(time_diff_seconds / (60 * 60))
                hours_threshold = int(os.environ.get('DELIVERY_THRESHOLD', 2)) * 24

                if time_diff_hours >= hours_threshold:
                    collector_status = 'Frozen'
                    break

        resp = {
            'collector': user_obj.username,
            'status': collector_status
        }
        return Response({'status': 'success', "tasks": resp}, status=200)

    @action(detail=True, methods=['patch'])
    def patch_collect(self, request, pk=None):
        user_id = Employee.objects.get(user=request.user)
        task = self.get_object()
        if task.collector != user_id:
            return Response({"status": "Failed", "data": "Not Authorized to edit this task"},
                            status=status.HTTP_403_FORBIDDEN)
        task.collected = request.data['collected']
        task.save()
        serializers = TaskSerializer(task)
        return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)

    def patch_deliver(self, request, pk=None):
        user_id = Employee.objects.get(user=request.user)
        task = self.get_object()
        if task.collector != user_id:
            return Response({"status": "Failed", "data": "Not Authorized to edit this task"},
                            status=status.HTTP_403_FORBIDDEN)
        task = self.get_object()
        task.delivered = request.data['delivered']
        task.save()
        serializers = TaskSerializer(task)
        return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)
