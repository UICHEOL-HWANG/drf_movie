from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=30)
    opening_date = models.DateField()
    running_time = models.IntegerField()
    overview = models.TextField()
    actors = models.ManyToManyField('Actor', related_name='movies')
    
    def __str__(self):
        return self.name
    

class Actor(models.Model):
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()
    
    def __str__(self):
        return self.name
    
    
class Review(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE, related_name='reviews')
    username = models.CharField(max_length=30)
    star = models.IntegerField()
    comment = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.comment
    # 리뷰 객체를 출력하면 코멘트가 먼저 나온다