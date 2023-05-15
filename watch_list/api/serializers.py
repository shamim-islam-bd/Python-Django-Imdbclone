from rest_framework import serializers
from watch_list.models import WatchList, StreamingPlatform, Review

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
    

# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Review
        exclude = ['watchlist']
        # fields = '__all__'



#model serializers
class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id', 'name', 'description', 'active']
        # exclude = ['active']
    


# class StreamingPlatformSerializer(serializers.HyperlinkedModelSerializer):
class StreamingPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)  # watchlist movies will store in streaming 
                                                                # watchlist name has to be same as watchlist foreignkey related_name
    # watchlist = serializers.StringRelatedField(many=True)       # stringRelatedField used for showing only string related fields.
   
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="watch_detail"
    )
   
    class Meta:
        model = StreamingPlatform
        fields = '__all__'


