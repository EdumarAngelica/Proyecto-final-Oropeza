from django.urls import path
from AppCoder.views import create_product_form, search_product, show_html, show_products, ProductList, ProductDetail, ProductCreacion, ProductActualizacion, ProductEliminar

urlpatterns = [
    path('crear-producto/', create_product_form),
    path('buscar/', search_product),
    path('show/', show_html),
    path('productos/', show_products),
    path('productos/lista', ProductList.as_view(), name="ProductList"),
    path('productos/<int:pk>', ProductDetail.as_view()),
    path('crear', ProductCreacion.as_view()),
    path('editar/<int:pk>', ProductActualizacion.as_view()),
    path('eliminar/<int:pk>', ProductEliminar.as_view()),
]
