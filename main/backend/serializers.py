from rest_framework import serializers
from .models import *


from django.core.validators import MaxLengthValidator, MinLengthValidator # 유효성 검증 
from rest_framework.validators import UniqueValidator # 유일성 검증 

def overview_validator(value):
    if value > 300 :
        raise ValueError('소개 문구는 최대 300자 이내로 작성해야 함')
    elif value < 10 :
        raise ValueError('소개 문구는 최소 10자 이상으로 작성해야 함')
    return value 


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) #필드 조회할 때만 사용 수정/생성/삭제는 불필요하므로 read_only 직관적 
    name = serializers.CharField()
    opening_date = serializers.DateField()
    running_time = serializers.IntegerField()
    overview = serializers.CharField(validators=[overview_validator])
    
    # 직접 데이터 생성 
    def create(self,validated_data):
        return Movie.objects.create(**validated_data) # 언패킹시킨 movie 데이터들 ** 언패킹
    
    # 데이터 수정
    def update(self,instance,validated_data):
        # instance란 수정할 데이터를 받는 변수 / 즉 Movie모델의 객체를 의미한다 
        instance.name = validated_data.get('name',instance.name) # validated를 통해 유효한지 안한지를 검증한 후 수정된 데이터를 집어넣어준다 
        instance.opening_date = validated_data.get('opening_date',instance.opening_date)
        instance.running_time = validated_data.get('running_time', instance.running_time)
        instance.overview = validated_data.get('overview', instance.overview)
        instance.save()
        
        return instance





# 관계가 담긴 시리얼라이저 생성 

class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()
    class Meta:
        model = Review 
        
        fields = ['id','movie','username','star','comment','created']
        
        extra_kwargs = {
            'movie' : {'read_only' : True } 
        }






# 상기에 정의한 내용들을 이 내용으로도 간단하게 표현이 가능하다
class MovieSerializer(serializers.ModelSerializer):

    name = serializers.CharField(validators=[UniqueValidator(
        queryset=Movie.objects.all(),
        message='이미 존재하는 영화임',
    )])
    
    actors = serializers.StringRelatedField(many=True, read_only=True)
    
    
    # 만약 reviews라고 지은 related_name을 쓰기 어려운 상황이 왔다면 하기 내용으로 바꿔주면 된다.
    movie_reviews = serializers.PrimaryKeyRelatedField(source='reviews', many=True, read_only=True)
    
    reviews = ReviewSerializer(many=True, read_only=True) # 리뷰어가 남긴 모든 정보를 끌고 오고 싶을때 
    # Nested Serializer를 사용해주면 된다
    # 뜻이 그냥 다 갖고 온다는 뜻임ㅋ 
    
    
    # reviews = serializers.StringRelatedField(many=True)
    # model에서 __str__ 메소드로 사용된 comment를 StringRelatedField로 사용해서 비춰주게한다 
    
    class Meta:
        model = Movie
        fields = ['id', 'name', 'movie_reviews', 'opening_date', 'running_time', 'overview','reviews','actors'] #reviews로 보여줌
        read_only_fields = ['movie_reviews'] # 역관계 직렬화 
        
        # 모델 내에서 외래키로 related_name을 reviews로 바꿔줬기 때문에 그에 맞춰 올려주면 된다 .
        


    
class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    gender = serializers.CharField()
    birth_date = serializers.DateField()
    
    def create(self, validated_data):
        return Actor.objects.create(**validated_data)
    
    # 데이터 수정 
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.gender = validated_data.get('gender',instance.gender)
        instance.birth_date = validated_data.get('birth_date',instance.birth_date)
        
        instance.save()
        
        return instance
    

class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = ['id', 'name', 'gender', 'birth_date', 'movies']
        
        

