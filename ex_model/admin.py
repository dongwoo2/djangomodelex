from django.contrib import admin

# Register your models here.

from .models import Info

admin.site.register(Info) # 관리자 사이트에 모델을 등록한 것