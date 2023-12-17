from django import forms

class ProductForm(forms.Form):
    titulo = forms.CharField()
    descripcion = forms.CharField()
    caracteristicas = forms.CharField()
    sku = forms.CharField()
    stock_bloqueado = forms.IntegerField()
    stock_disponible = forms.IntegerField()
 

class SearchProduct(forms.Form):
    titulo = forms.CharField()

    
