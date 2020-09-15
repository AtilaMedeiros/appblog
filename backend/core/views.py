from logging import Filter

from rest_framework import authentication, permissions, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)

from .models import Item, List
from .serializers import ItemSerializer, ListSerializer


class ListViewSet(viewsets.ModelViewSet):

    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_queryset(self):
        user = self.request.user
        return List.objects.filter(owner=user)


class ItemViewSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
