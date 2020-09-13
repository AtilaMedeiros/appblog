from rest_framework import viewsets, permissions
from .serializers import ListSerializer
from .models import List


class ListViewSet(viewsets.ModelViewSet):

    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
