from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-overwatch'),
    path('update/<int:overwatch_id>', views.update_overwatch),
    path('delete/<int:overwatch_id>', views.delete_overwatch)
]

