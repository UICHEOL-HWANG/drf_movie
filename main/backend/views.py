from django.shortcuts import render


# REST API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import *

from rest_framework.generics import get_object_or_404


# MODEL,SERIALIZER
from .models import * 
from .serializers import *






# class형 뷰로 바꿔보기 


# @api_view(['GET','POST']) #GET 메소드만 허용 시키는 명령 
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all() 
#         serializer = MovieSerializer(movies, many=True) # movie라는 모델에서 받아오는 데이터가 여러개이니 many값을 True 시켜주면 된다  
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     # Response는 레스트프레임워크의 응답 클래스임 
#     # MovieSerializer를 통해 딕셔너리 형태로 변환된 데이터는 최종적으로 Json으로 변형됨 
    
#     # 직접 영화 데이터 생성 
#     elif request.method == 'POST':
#         data = request.data
#         serializer = MovieSerializer(data=data)
        
#         # 영화 데이터의 유효성 검사 
#         if serializer.is_valid():
#             serializer.save() # 적절하면 생성 반납
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) # 니 데이터 좆됐다를 보여줘야지 


# 이번엔 class 형 view를 통해 move_list를 보여준다 

class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
            
# @api_view(['GET','POST'])
# def actor_list(request):
#     if request.method == 'GET':
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         data = request.data 
#         serializer = ActorSerializer(data=data)
        
#         if serializer.is_valid():
#             serializer.save() 
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class형 actor_list 
class ActorList(APIView):
    def get(self,request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ActorList(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    

# @api_view(['GET', 'PATCH', 'DELETE'])
# def movie_detail(request, pk):
#     movie = get_object_or_404(Movie,pk=pk) # pk 그러니까 고유 값이 같지 않으면 404 에러를 발생시키는 옵션 
#     if request.method == "GET" :
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     elif request.method == 'PATCH': # 대부분 데이터의 수정을 요청 받기 때문에, partical옵션 True를 넣어줌 
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)        


# class형 view 조회 / 삭제 

# class MovieDetail(APIView):
#     def get_object(self, pk):
#         movie = get_object_or_404(Movie, pk=pk)
#         return movie

#     def get(self, request, pk):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     def patch(self, request, pk):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         movie = self.get_object(pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# RetrieveUpdateDestroyAPIView 
# 데이터 조회 수정 삭제 가능 

class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    

# @api_view(['GET', 'PATCH', 'DELETE'])
# def actor_detail(request, pk):
#     actor = get_object_or_404(Actor,pk=pk)
#     if request.method == 'GET':
#         serializer = ActorSerializer(actor)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     elif request.method == 'PATCH':
#         serializer = ActorSerializer(actor,data=request.data,partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         actor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ActorDetail(APIView):
    def get_object(self, pk):
        actor = get_object_or_404(Actor, pk=pk)
        return actor

    def get(self, request, pk):
        actor = self.get_object(pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    def patch(self, request, pk):
        actor = self.get_object(pk)
        serializer = ActorSerializer(actor, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ActorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

# @api_view(['GET', 'POST'])
# def review_list(request,pk):
#     movie = get_object_or_404(Movie,pk=pk)
    
#     if request.method == 'GET': 
#         reviews = Review.objects.filter(movie=movie) # filter 함수에 파라미터로 특정한 영화에 속하는 리뷰 데이터를 가져오게 한다 , 
#         serializer = ReviewSerializer(reviews,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(movie=movie)
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
# Review List를 class형으로 변환 

class ReviewList(ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        return Review.objects.filter(movie=movie)

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        serializer.save(movie=movie)