# cadastro_produtos/urls.py

from django.urls import path
from . import views
from .views import ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),   
    path('<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('produtos/', ProductCreate.as_view(), name='product-create'),
    path('produtos/<int:pk>/editar/', ProductUpdate.as_view(), name='product-update'),
    path('produtos/<int:pk>/excluir/', ProductDelete.as_view(), name='product-delete'),
    # path('produtos/', views.ProductListCreate.as_view(), name='product-list-create'),
]

# urlpatterns = [
#     path('produtos/', views.ProductListCreate.as_view(), name='product-list-create'),
#     path('produtos/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
# ]









# urlpatterns = [
#     path('produtos/', ProdutoList.as_view(), name='produto-list'),
#     path('produtos/<int:pk>/', ProdutoDetail.as_view(), name='produto-detail'),
#     # path('cadastro_produtos/schema/', SpectacularAPIView.as_view(), name='schema'),
#     # path('cadastro_produtos/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
#     # path('cadastro_produtos/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
# ]

