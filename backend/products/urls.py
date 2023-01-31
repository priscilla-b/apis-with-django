from django.urls import path

from . import views


# /api/products/
urlpatterns = [
    path('', views.ProductListCreateApiView.as_view()),
    path('<int:pk>/', views.ProductDetailApiView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateApiView.as_view()),
    path('<int:pk>/delete/', views.ProductUpdateApiView.as_view()),
]

# urlpatterns = [
#     path('', views.product_alt_view),
#     path('<int:pk>', views.product_alt_view),
# ]