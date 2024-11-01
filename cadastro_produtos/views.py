from itertools import product
from rest_framework.pagination import PageNumberPagination
from .serializers import ProdutoSerializer
from .models import Produto
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pag_size'
    max_page_size = 100


@api_view(['GET'])
def get_products(request):
    products = product.objects.all()
    paginator = ProductPagination()
    result_page = paginator.paginate_queryset(products, request)
    serializer = ProdutoSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

class ProductListCreate(generics.ListCreateAPIView):
     queryset = Produto.objects.all()
     serializer_class = ProdutoSerializer

class ProductList(ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome', None)
        categoria = self.request.query_params.get('categoria', None)
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        if categoria:
            queryset = queryset.filter(categoria__icontains=categoria)
        return queryset

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProductCreate(generics.CreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProductUpdate(UpdateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProductDelete(DestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer








# class ProdutoViewSet(viewsets.ModelViewSet):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer
    
    
# class ProductListCreate(generics.ListCreateAPIView):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer
    
# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Produto.objects.all()
#     serializer_class = ProdutoSerializer
    






    

