from django.urls import path

from . import views



urlpatterns = [
    path('', views.ProductCreateApiView.as_view()),
    path('<int:pk>', views.ProductDetailApiView.as_view())
]