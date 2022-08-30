from rest_framework import serializers
from accounts.models import Staff


class StaffSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Staff
        fields=('departmentId','name','age','gender','department','dob')