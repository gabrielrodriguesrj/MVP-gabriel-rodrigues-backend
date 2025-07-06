from flask_openapi3 import APIBlueprint
from src.models.subscription import Subscription, db
from src.schemas.subscription_schemas import SubscriptionCreateSchema, SubscriptionUpdateSchema, SubscriptionResponseSchema

subscription_bp = APIBlueprint('subscription', __name__)

@subscription_bp.get('/subscriptions', responses={200: SubscriptionResponseSchema})
def get_subscriptions():
    """Buscar todas as assinaturas"""
    subscriptions = Subscription.query.all()
    return [subscription.to_dict() for subscription in subscriptions]

@subscription_bp.post('/subscriptions', responses={201: SubscriptionResponseSchema})
def create_subscription(body: SubscriptionCreateSchema):
    """Cadastrar uma nova assinatura"""
    subscription = Subscription(
        name=body.name,
        description=body.description,
        price=body.price,
        billing_cycle=body.billing_cycle,
        next_billing_date=body.next_billing_date,
        category=body.category,
        user_id=body.user_id
    )
    db.session.add(subscription)
    db.session.commit()
    return subscription.to_dict(), 201

@subscription_bp.get('/subscriptions/<int:subscription_id>', responses={200: SubscriptionResponseSchema})
def get_subscription(subscription_id: int):
    """Buscar assinatura por ID"""
    subscription = Subscription.query.get_or_404(subscription_id)
    return subscription.to_dict()

@subscription_bp.put('/subscriptions/<int:subscription_id>', responses={200: SubscriptionResponseSchema})
def update_subscription(subscription_id: int, body: SubscriptionUpdateSchema):
    """Atualizar assinatura"""
    subscription = Subscription.query.get_or_404(subscription_id)
    
    if body.name is not None:
        subscription.name = body.name
    if body.description is not None:
        subscription.description = body.description
    if body.price is not None:
        subscription.price = body.price
    if body.billing_cycle is not None:
        subscription.billing_cycle = body.billing_cycle
    if body.next_billing_date is not None:
        subscription.next_billing_date = body.next_billing_date
    if body.category is not None:
        subscription.category = body.category
    if body.is_active is not None:
        subscription.is_active = body.is_active
    
    db.session.commit()
    return subscription.to_dict()

@subscription_bp.delete('/subscriptions/<int:subscription_id>', responses={204: None})
def delete_subscription(subscription_id: int):
    """Deletar assinatura"""
    subscription = Subscription.query.get_or_404(subscription_id)
    db.session.delete(subscription)
    db.session.commit()
    return '', 204

@subscription_bp.get('/users/<int:user_id>/subscriptions', responses={200: SubscriptionResponseSchema})
def get_user_subscriptions(user_id: int):
    """Buscar assinaturas de um usuário específico"""
    subscriptions = Subscription.query.filter_by(user_id=user_id).all()
    return [subscription.to_dict() for subscription in subscriptions]

