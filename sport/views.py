from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Sport
from .serializers import SportSerializer
from .permissions import IsOwnerOrReadOnly
# Create your views here.


class SportList(ListCreateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class SportDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
