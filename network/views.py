from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from network.models import Product, Link, Contact
from network.serializers import ProductSerializer, LinkSerializer, LinkReadSerializer, ContactSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class LinkCreateAPIView(generics.CreateAPIView):
    serializer_class = LinkSerializer


class LinkUpdateAPIView(generics.UpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LinkListAPIView(generics.ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkReadSerializer


class LinkRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkReadSerializer


class LinkDestroyAPIView(generics.DestroyAPIView):
    queryset = Link.objects.all()
    permission_classes = [IsAdminUser]


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
