from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<int:post_id>/details', views.post_details, name='post_details')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
