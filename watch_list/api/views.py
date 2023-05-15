from watch_list.api.serializers import WatchListSerializer, StreamingPlatformSerializer
from watch_list.models import WatchList, StreamingPlatform
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from watch_list.api.serializers import ReviewSerializer
from watch_list.models import Review

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

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=watchlist)




class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all() 
    serializer_class = ReviewSerializer



   
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
        serializer = StreamingPlatformSerializer(platform, many=True, context={'request': request}) 
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