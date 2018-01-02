from .models import Document
from .serializers import DocumentSerializer
from rest_framework import viewsets

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
