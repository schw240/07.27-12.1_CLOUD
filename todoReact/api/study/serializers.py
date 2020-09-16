from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import Students, Scores
from django.contrib.auth import get_user_model




class StudentBasicSerializer(Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    email = serializers.CharField()
    def create(self, validated_data):
        Students.objects.create()
        return Students.objects.create(**validated_data)
        #return Students.objects.create(name=validated_data['name'], address=validated_data['address'])
    #student, data=request.data
    #inctance 원래데이터 (student)
    #validated_data 사람이 보내준 데이터 (data=request.data)
    #(원래데이터 <- 사람이 보내준 데이터) -> SAVE 
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.name)
        instance.email = validated_data.get('email', instance.name)
        instance.save()
        return instance


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    #reg_user = UserSerializer(read_only=True) #등록때 사용하지않겠다.
    reg_user_username = serializers.ReadOnlyField(source='reg_user.username')
    reg_user_email = serializers.ReadOnlyField(source='reg_user.email')
    test = serializers.SerializerMethodField()

    def get_test(self, obj):
        return obj.address + " (" + obj.name + ")"

    class Meta:
        model = Students
        fields = ['name', 'address', 'email', 'memo', 'reg_user', 'reg_user_username', 'reg_user_email', 'reg_user', 'test']




class ScoreSerializer(ModelSerializer):

    username = serializers.ReadOnlyField(source='reg_user.username')
    email = serializers.ReadOnlyField(source='reg_user.email')
    phone_number = serializers.ReadOnlyField(source='reg_user.phone_number')


    class Meta:
        model = Scores
        fields = '__all__'