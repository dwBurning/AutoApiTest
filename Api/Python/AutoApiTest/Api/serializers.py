# 序列化
from rest_framework import serializers

from .models import Person


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person     #指定的模型类
        fields = '__all__'  #('pk', 'name', 'sex', 'sid',)   #需要序列化的属性
