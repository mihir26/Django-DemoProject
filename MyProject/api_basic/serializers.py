from rest_framework import serializers
from .models import Detail

# class DetailSerializer(serializers.Serializer):
#     name : serializers.CharField(max_length = 100)
#     email : serializers.EmailField(max_length = 100)
#     phone : serializers.CharField(max_length = 20)
#     comments : serializers.CharField(max_length = 100)
#     date : serializers.DateTimeField()

# def create (self,validated_data):
#      return Detail.objects.create(validated_data)

# def update (self,instance,validated_data):
#     instance.name = validated_data.get('name',instance.name)
#     instance.email = validated_data.get('email',instance.email)
#     instance.phone = validated_data.get('phone',instance.phone)
#     instance.comments = validated_data.get('comments',instance.comments)
#     instance.date = validated_data.get('date',instance.date)
#     instance.save()
#     return instance

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        # fields = ['id','title','author']
        fields = '__all__'