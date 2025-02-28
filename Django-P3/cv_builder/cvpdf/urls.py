from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'), 
    path('add_cv/', views.submit_cv, name='sbumit_cv'), 
    path('cv/<int:id>/', views.CV, name = 'cv_page'),
    path('cv/<int:id>/download/', views.download_CV, name = 'download_CV'),
    path('cv_list/', views.CV_list, name='cv_list'), 

    path('delete_cv/<int:id>/', views.delete_cv, name='delete_cv'), 
    

]



from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




