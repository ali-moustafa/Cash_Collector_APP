from rest_framework import serializers
from .models import Employee, Task


class EmployeeSerializer(serializers.ModelSerializer):
    role = serializers.CharField(max_length=255, required=True)

    def create(self, validated_data):
        """
        Create and return a new `Employee` instance, given the validated data.
        """
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Employee` instance, given the validated data.
        """
        instance.role = validated_data.get('address', instance.role)

        instance.save()
        return instance

    class Meta:
        model = Employee
        fields = ('__all__')


class TaskSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, required=True)
    address = serializers.CharField(max_length=255, required=True)
    amount_due = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    amount_due_at = serializers.DateTimeField()
    collected = serializers.BooleanField(default=False)
    delivered = serializers.BooleanField(default=False)

    def create(self, validated_data):
        """
        Create and return a new `Task` instance, given the validated data.
        """
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Task` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.amount_due = validated_data.get('amount_due', instance.amount_due)
        instance.amount_due_at = validated_data.get('amount_due_at', instance.amount_due_at)
        instance.collected = validated_data.get('collected', instance.collected)
        instance.delivered = validated_data.get('delivered', instance.delivered)

        instance.save()
        return instance

    class Meta:
        model = Task
        fields = ('__all__')
