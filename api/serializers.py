from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    profession = serializers.CharField(max_length=100)
    mobile_no = serializers.IntegerField()
    roll_number = serializers.IntegerField()
    degree = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)

    # TODO For Posting Data
    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    # TODO For Updating Data
    # Instance is our old data, validated_data is our new data coming from client
    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.profession = validated_data.get('profession', instance.profession)
        instance.mobile_no = validated_data.get('mobile_no', instance.mobile_no)
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)
        instance.degree = validated_data.get('degree', instance.degree)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
