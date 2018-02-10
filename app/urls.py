from django.urls import path
from . import views
urlpatterns = [
    # /app/
    path('', views.index, name='index'),
    # /app/712/
    path('<int:album_id>/', views.detail, name="detail"),
]
