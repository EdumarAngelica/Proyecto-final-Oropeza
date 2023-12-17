from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Product
from AppCoder.forms import SearchProduct, ProductForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.
class ProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = "AppCoder/Products_1.html"


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "AppCoder/producto_detalle.html"
# modificar en el HTML

class ProductCreacion(CreateView):
    model = Product
    success_url = "/app/productos/listas"
    template_name = "AppCoder/crear_producto.html"
    fields = ["nombre", "camada"]


class ProductActualizacion(UpdateView):
    model = Product
    success_url = "/app/productos/listas"
    template_name = "AppCoder/crear_producto.html"
    fields = ["nombre", "camada"]

class ProductEliminar(DeleteView):
    model = Product
    template_name = "AppCoder/eliminar_producto.html"
    success_url = "/app/productos/listas"


def show_products(request):
    products = Product.objects.all()
    contexto = {
        "products": products,
        "form": SearchProduct(),
    }
    return render(request, "AppCoder/productos.html", contexto)

@login_required 
def create_product_form(request):
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            data_product = product_form.cleaned_data
            create_product = Product(
                title=data_product["titulo"],
                description=data_product["descripcion"], 
                characteristics=data_product["caracteristicas"],
                sku=data_product["sku"],
                locked_stock=data_product["stock_bloqueado"],
                available_stock=data_product["stock_disponible"]
                )
            create_product.save()
            return redirect("/app/productos/")

    
    product_form = ProductForm()
    contexto = {
        "form": product_form
    }
    return render(request, "AppCoder/crear_producto.html", contexto)

def search_product(request):
    title = request.GET["titulo"]
    products = Product.objects.filter(title__icontains=title)
    contexto = {
        "products": products,
        "form": SearchProduct(),
    }
    return render(request, "AppCoder/productos.html", contexto)



def show_html(request):
    product = Product.objects.first()
    contexto = {"producto": product, "nombre":"Juan" }
    return render(request, "index.html", contexto)