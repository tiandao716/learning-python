# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2023-09-28 21:36
"""
from rest_framework import serializers

from . import models
from .models import Goods


class GoodsCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()


class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    # category = serializers.CharField(required=True, max_length=100)
    category = GoodsCategorySerializer(required=False, read_only=True)
    market_price = serializers.DecimalField(max_digits=8, decimal_places=2)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def create(self, validated_data):
        print(type(validated_data), validated_data)
        return Goods.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(type(validated_data), validated_data)
        instance.name = validated_data.get("name")
        instance.market_price = validated_data.get('market_price')
        instance.price = validated_data.get('price')
        instance.save()
        return instance


class GoodsModelSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()

    class Meta:
        model = models.Goods  # 关联模型类
        fields = "__all__"  # 显示所有的字段
