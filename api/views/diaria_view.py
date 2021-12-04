from rest_framework.views import APIView
from ..serializers.diaria_serializer import DiariaSerializer
from rest_framework import status as status_http
from rest_framework.response import Response


class Diaria(APIView):
    def post(self,request,format=None):
        serializer_diaria = DiariaSerializer(data=request.data, context={'request': request})
        
        if serializer_diaria.is_valid():
            serializer_diaria.save()
            return Response(serializer_diaria,status=status_http.HTTP_201_CREATED)
        return ResourceWarning(serializer_diaria.erros,status=status_http.HTTP_400_BAD_REQUEST)
        
            
        