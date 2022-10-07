
from django.contrib import admin
from django.urls import path
from invista_me import views
from usuarios import views as user_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', user_views.novo_user, name='novo_user'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('', views.investimentos, name='investimentos'),
    path('novo_investimento/', views.criar_investimento, name='novo_investimento'),
    path('novo_investimento/<int:id_investimento>', views.editar, name='editar'),
    path('excluir_investimento/<int:id_investimento>',views.excluir, name='excluir'),
    path('/<int:id_investimento>', views.detalhe, name='detalhe'),
]
