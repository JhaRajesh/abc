from django.urls import path, re_path
from rango import views

urlpatterns = [
	path('', views.index, name='index'),
	path('rango/about/', views.about, name='about'),
	path('rango/add_category/', views.add_category, name='add_category'),
	path('rango/category/<str:category_name_url>', views.category, name='category'),
	path('rango/register/', views.register, name='register'),
	path('rango/login/',views.user_login, name='login'),
	path('rango/restricted/', views.restricted, name='restricted'),
	path('rango/logout/', views.user_logout, name='logout')
]