from rest_framework.views import APIView
from ..serializers.diaria_serializer import DiariaSerializer
from rest_framework import status as status_http
from rest_framework.response import Response
from rest_framework import permissions,serializers
class Diaria(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    
    def post(self,request,format=None):
        serializer_diaria = DiariaSerializer(data=request.data, 
        context={'request': request})
        if request.user.tipo_usuario==2:
            raise serializers.ValidationError('Apenas clientes podem solicitar diárias')
       
        if serializer_diaria.is_valid():
            serializer_diaria.save()
            return Response(serializer_diaria.data,status=status_http.HTTP_201_CREATED)
        return Response(serializer_diaria.errors,status=status_http.HTTP_400_BAD_REQUEST)
        
            
        
