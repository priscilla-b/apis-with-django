from django.urls import path

from . import views



urlpatterns = [
    path('<int:pk>', views.ProductDetailApiView.as_view())
]