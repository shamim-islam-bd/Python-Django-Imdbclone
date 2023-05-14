from rest_framework import serializers
from watch_list.models import WatchList, StreamingPlatform

# Create your models here.

#Serializer
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()


#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)

#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Title and Description should be different')
#         return data
    
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short')
#         return value
    
#     def validate_description(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Description is too short')
#         return value
    
#model serializers
class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id', 'name', 'description', 'active']
        # exclude = ['active']
    

class StreamingPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamingPlatform
        fields = '__all__'
        # fields = ['id', 'name', 'description', 'active']
        # exclude = ['active']

