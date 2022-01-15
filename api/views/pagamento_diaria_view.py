from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import pagamento_diaria_serializer
from ..service import diaria_service
from rest_framework  import status as status_http
from ..service.pagamento_diaria_service import realizar_pagamento
class PagamentoDiaria(APIView):
   def post(self, request, diaria_id, format=None):
       diaria=diaria_service.listar_diaria_id(diaria_id)
       serializer_pagamento = pagamento_diaria_serializer.PagamentoDiariaSerializer(data=request.data)
       
       if serializer_pagamento.is_valid():
           card_hash=serializer_pagamento.validated_data["card_hash"]
           
           if diaria.status ==1:
               realizar_pagamento(diaria, card_hash)
               return Response({"Diária paga com sucess"},status=status_http.HTTP_200_OK)
           
           return Response({'Não é possível pagar essa diária'}, status=status_http.HTTP_400_BAD_REQUEST)
       
       return Response(serializer_pagamento.errors,status=status_http.HTTP_400_BAD_REQUEST)
