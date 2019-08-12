from django.contrib import admin
from .models import Item   # 현재 폴더에 있는 models로 부터 Item 임포트

admin.site.register(Item)  # Item 앞뒤에 따옴표 없음!