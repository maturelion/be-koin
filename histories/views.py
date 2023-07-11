from rest_framework.viewsets import ModelViewSet
from .serializers import HistorySerializer
from .models import History


class HistoryViewSet(ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    lookup_field = "id"
    filterset_fields = ('user', 'currency')
