from django.urls import path 
from accounts.views import editar_request, login_request, register_request, editar_avatar_request
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', register_request),
    path('editar/', editar_request),
    path('avatar/', editar_avatar_request),
    path('login/', login_request),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="Logout",),
] 
