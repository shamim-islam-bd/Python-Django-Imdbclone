from watch_list.api.serializers import WatchListSerializer, StreamingPlatformSerializer
from watch_list.models import WatchList, StreamingPlatform
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from watch_list.api.serializers import ReviewSerializer
from watch_list.models import Review
from watch_list.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

# class ReviewDetails(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all() 
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    

# Review geting, and create a new using mixins and generics views
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all() 
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)




class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all() 
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  #authenticated user can see the review list.

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
       return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        
        # filtering login user who can create the review ------------
        review_user = self.request.user 
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError('You have already reviewed this movie')
        
        
        # calculating the average rating ----------------
        if watchlist.num_of_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating'] 
        else:
            watchlist.avg_rating = (watchlist.avg_rating  + serializer.validated_data['rating']) / 2
        
        watchlist.num_of_rating = watchlist.num_of_rating + 1
        watchlist.save()
        
        serializer.save(watchlist=watchlist, review_user=review_user)
        
        
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all() 
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly] #only admin can delete the review.


class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        seriliazer = WatchListSerializer(movies, many=True) #when we have many objects we need to pass many=True
        return Response(seriliazer.data)
    
    def post(self, request):
        seriliazer = WatchListSerializer(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        return Response(seriliazer.errors)
    
    
class WatchDetailAV(APIView):
    def get(self, request, pk):
      try: 
        movie = WatchList.objects.get(id=pk)
      except WatchList.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=404)
      
      seriliazer = WatchListSerializer(movie)
      return Response(seriliazer.data)
    
    def put(self, request, pk):
        movie = WatchList.objects.get(id=pk)
        seriliazer = WatchListSerializer(instance=movie, data=request.data)

        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        return Response(seriliazer.errors)
    
    def delete(self, request, pk):
        movie = WatchList.objects.get(id=pk)
        movie.delete()
        return Response('Item Deleted')


class StreamingPlatformAV(APIView):
    def get(self, request):
        platform = StreamingPlatform.objects.all()
        # context is used for HyperlinkedRelatedField
        serializer = StreamingPlatformSerializer(platform, many=True) 
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class StreamingPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamingPlatform.objects.get(id=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({'error': 'Streaming Platform not found'}, status=404)
        serializer = StreamingPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = StreamingPlatform.objects.get(id=pk)
        serializer = StreamingPlatformSerializer(instance=platform, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        platform = StreamingPlatform.objects.get(id=pk)
        platform.delete()
        return Response('Item Deleted')