from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.usuario_serializer import UsuarioSerializer
from rest_framework import status
from rest_framework import  permissions
class Me(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self,request,format=None):
        serializer_usuario=UsuarioSerializer(request.user,context={"request": request})
        return Response(serializer_usuario.data, status=status.HTTP_200_OK)