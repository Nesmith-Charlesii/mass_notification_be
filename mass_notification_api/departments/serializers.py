from rest_framework import serializers
from models import Department

class DepartmentSerializer(serializers.Serializer):
    class Meta:
        model = Department
        fields = [
            "id",
            "department_name",
            "head_of_department",
            "phone_number",
            "created_at",
            "last_modified",
            "users"
        ]