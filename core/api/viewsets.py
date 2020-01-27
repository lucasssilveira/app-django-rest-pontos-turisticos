from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


class PontoTuristicoViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """

    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter]
    #permission_classes = (IsAuthenticated,)
    #permission_classes = (IsAuthenticatedOrReadyOnly,)
    #permission_classes = (DjangoModelPermissions, )
    #authentication_classes = (TokenAuthentication,)
    search_fields = ['nome', 'descricao', 'endereco__linha1']
    lookup_field = 'id'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome__iexact=nome)
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    #
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)

    # @action(methods=['post'], detail=True)
    # def denunciar(self, request, pk=None):
    #  pass
