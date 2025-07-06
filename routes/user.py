from flask_openapi3 import APIBlueprint
from src.models.user import User, db
from src.schemas.user_schemas import UserCreateSchema, UserUpdateSchema, UserResponseSchema

user_bp = APIBlueprint('user', __name__, url_prefix='/api/users')

@user_bp.get('/users', responses={200: UserResponseSchema})
def get_users():
    """Buscar todos os usuários"""
    users = User.query.all()
    return [user.to_dict() for user in users]

@user_bp.post('/users', responses={201: UserResponseSchema})
def create_user(body: UserCreateSchema):
    """Cadastrar um novo usuário"""
    user = User(username=body.username, email=body.email)
    db.session.add(user)
    db.session.commit()
    return user.to_dict(), 201

@user_bp.get('/users/<int:user_id>', responses={200: UserResponseSchema})
def get_user(user_id: int):
    """Buscar usuário por ID"""
    user = User.query.get_or_404(user_id)
    return user.to_dict()

@user_bp.put('/users/<int:user_id>', responses={200: UserResponseSchema})
def update_user(user_id: int, body: UserUpdateSchema):
    """Atualizar usuário"""
    user = User.query.get_or_404(user_id)
    if body.username is not None:
        user.username = body.username
    if body.email is not None:
        user.email = body.email
    db.session.commit()
    return user.to_dict()

@user_bp.delete('/users/<int:user_id>', responses={204: None})
def delete_user(user_id: int):
    """Deletar usuário"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

