from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.usuario_serializer import UsuarioSerializer
from rest_framework import permissions


class Usuario(APIView):
    
    permission_classes = [permissions.IsAuthenticated,]

    def post(self,request,format=None):
        serializer_usuario=UsuarioSerializer(data=request.data,context={"request"   :request})

        if serializer_usuario.is_valid():
            usuario_criado=serializer_usuario.save()
            serializer_usuario=UsuarioSerializer(usuario_criado)
            return Response(serializer_usuario.data,status=status.HTTP_200_OK)

        return Response(serializer_usuario.errors)
