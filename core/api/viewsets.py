from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class  PontoTuristicoViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    serializer_class = PontoTuristicoSerializer


    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    #def list(self, request, *args, **kwargs):
   #     return Response({'teste': 123})

    #def create(self, request, *args, **kwargs):
      #  return Response({'Hello': request.data['nome']})

      #def destroy(self, request, *args, **kwargs):

    #  def retrieve(self, request, *args, **kwargs): tipo o get mas para no item

    # def update(self, request, *args, **kwargs): método put

    # def partial_update(self, request, *args, **kwargs): metodo path

    @action(methods=['post'], detail=True)
    def denunciar(self, request, pk=None):
        pass

