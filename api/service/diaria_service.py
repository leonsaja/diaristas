from ..models import Diaria
from ..service import usuario_servico
def listar_diaria_id(diaria_id):
    return Diaria.objects.get(id=diaria_id)


def atualizar_status_diaria(diaria_id,status):
    diaria=listar_diaria_id(diaria_id)
    diaria.status=status
    diaria.save()
    
    
def listar_diaria_usuario(usuario_id):
    usuario=usuario_servico.listar_usuario_id(usuario_id)
    if usuario.tipo_usuario==1:
        return Diaria.objects.filter(cliente=usuario.id).all()
    return Diaria.objects.filter(diarista=usuario.id).all()