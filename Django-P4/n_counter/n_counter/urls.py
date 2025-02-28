# from django.contrib import admin  # type: ignore
# from django.urls import path  # type: ignore
# from app import views
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('delete/<int:id>/', views.delete_consume, name="delete"),
#     path('nutrient-data/', views.nutrient_data, name="nutrient-data"),  # Changed to "nutrient-data/"
#     path("chart-data/", views.chart_data, name="chart-data"),
#     path("register/", views.register, name="register"),
#     # path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
#     path("login/", views.login_view, name="login"),
#     # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
#     path('logout/', views.logout_view, name='logout' ), 
#     path("add-food/", views.add_food, name="add-food"),
#     path("update-goals/", views.update_goals, name="update-goals"),
# ]



from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.page_view, name='home'), 
    path('index/', views.index, name='index'),
    path('delete/<int:id>/', views.delete_consume, name="delete"),
    path('nutrient-data/', views.nutrient_data, name="nutrient-data"),  # Changed to "nutrient-data/"
    path("chart-data/", views.chart_data, name="chart-data"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.logout_view, name='logout' ), 
    path("add-food/", views.add_food, name="add-food"),
    path("update-goals/", views.update_goals, name="update-goals"),
]
