# DRF를 이용한 영화 LIST 만들기 
1. DRF GET / POST / PUT / PATCH를 이용 
2. class 형 view를 이용하여 GET / POST / PUT / PATCH를 간단하게 표현 
3. 제네릭 API뷰를 통해 간결하고 빠르게 내용을 적용 시킴 


```python 
 @api_view(['GET','POST']) #GET 메소드만 허용 시키는 명령 
 def movie_list(request):
     if request.method == 'GET':
         movies = Movie.objects.all() 
         serializer = MovieSerializer(movies, many=True) # movie라는 모델에서 받아오는 데이터가 여러개이니 many값을 True 시켜주면 된다  
         return Response(serializer.data,status=status.HTTP_200_OK)
     # Response는 레스트프레임워크의 응답 클래스임 
     # MovieSerializer를 통해 딕셔너리 형태로 변환된 데이터는 최종적으로 Json으로 변형됨 
   
     # 직접 영화 데이터 생성 
     elif request.method == 'POST':
         data = request.data
         serializer = MovieSerializer(data=data)
       
         # 영화 데이터의 유효성 검사 
         if serializer.is_valid():
             serializer.save() # 적절하면 생성 반납
             return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) # 니 데이터 좆됐다를 보여줘야지 
```
기본 함수형 DRF VIEW 

---
```python
# class형 view 

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
```
---

```python
class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
```

> RetrieveUpdateDestroyAPIView 를 이용해서 더 간단하게 만들 수 있는데 
> RetrieveUpdateDestroyAPIView란?


>  RetrieveUpdateDestroyAPIView는 특정한 데이터를 조회·수정·삭제할 수 있는 제네릭 뷰입니다
>RetrieveUpdateDestroyAPIView에서도 queryset과 serializer_class는 필수 옵션인데요. 

> queryset은 특정 데이터를 가져올 때 사용하는 쿼리셋을 뜻합니다. 해당 값은 Movie.objects.all()로 설정하고, serializer_class는 MovieSerializer로 설정했습니다. 
