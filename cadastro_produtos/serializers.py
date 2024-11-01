from rest_framework import serializers
from .models import Produto
# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
 

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        # fields = ['id', 'nome', 'categoria', 'preco']

    # def create(self, validated_data):
    #     return Produto.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)
    #     instance.save()
    #     return instance

    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
