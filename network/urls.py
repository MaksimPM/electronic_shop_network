from django.urls import path
from rest_framework import routers

from network.apps import NetworkConfig
from network.views import ProductViewSet, ContactViewSet, LinkRetrieveAPIView, LinkListAPIView, LinkCreateAPIView, \
    LinkUpdateAPIView, LinkDestroyAPIView

app_name = NetworkConfig.name

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, basename='products')
router.register(r'contact', ContactViewSet, basename='contact')

urlpatterns = [
    path('link/<int:pk>/', LinkRetrieveAPIView.as_view(), name='link'),
    path('link/', LinkListAPIView.as_view(), name='link_list'),
    path('link/create/', LinkCreateAPIView.as_view(), name='link_create'),
    path('link/<int:pk>/update/', LinkUpdateAPIView.as_view(), name='link_update'),
    path('link/<int:pk>/delete/', LinkDestroyAPIView.as_view(), name='link_delete'),
] + router.urls
