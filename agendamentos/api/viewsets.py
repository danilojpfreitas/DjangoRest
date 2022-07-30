from rest_framework import viewsets

from agendamentos.models import Agendamentos
from agendamentos.api.serializers import AgendamentosSerializer

class AgendamentosViewSet(viewsets.ModelViewSet):
    # order_by é utilizado para gerar um ordenamento do JSON
    queryset = Agendamentos.objects.all().order_by('data_hora')
    serializer_class = AgendamentosSerializer