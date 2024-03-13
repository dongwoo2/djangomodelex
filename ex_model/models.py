from django.db import models

# Create your models here.

class Info(models.Model): # models의 Model 클래스를 상속받는다
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    intro = models.TextField()
    regdate = models.DateTimeField(auto_now_add=True) # 자동으로 현재시간 추가해서 진행