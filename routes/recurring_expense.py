from flask_openapi3 import APIBlueprint
from src.models.recurring_expense import RecurringExpense, db
from src.schemas.recurring_expense_schemas import RecurringExpenseCreateSchema, RecurringExpenseUpdateSchema, RecurringExpenseResponseSchema

recurring_expense_bp = APIBlueprint('recurring_expense', __name__)

@recurring_expense_bp.get('/recurring-expenses', responses={200: RecurringExpenseResponseSchema})
def get_recurring_expenses():
    """Buscar todos os gastos recorrentes"""
    expenses = RecurringExpense.query.all()
    return [expense.to_dict() for expense in expenses]

@recurring_expense_bp.post('/recurring-expenses', responses={201: RecurringExpenseResponseSchema})
def create_recurring_expense(body: RecurringExpenseCreateSchema):
    """Cadastrar um novo gasto recorrente"""
    expense = RecurringExpense(
        name=body.name,
        description=body.description,
        amount=body.amount,
        frequency=body.frequency,
        next_due_date=body.next_due_date,
        category=body.category,
        user_id=body.user_id
    )
    db.session.add(expense)
    db.session.commit()
    return expense.to_dict(), 201

@recurring_expense_bp.get('/recurring-expenses/<int:expense_id>', responses={200: RecurringExpenseResponseSchema})
def get_recurring_expense(expense_id: int):
    """Buscar gasto recorrente por ID"""
    expense = RecurringExpense.query.get_or_404(expense_id)
    return expense.to_dict()

@recurring_expense_bp.put('/recurring-expenses/<int:expense_id>', responses={200: RecurringExpenseResponseSchema})
def update_recurring_expense(expense_id: int, body: RecurringExpenseUpdateSchema):
    """Atualizar gasto recorrente"""
    expense = RecurringExpense.query.get_or_404(expense_id)
    
    if body.name is not None:
        expense.name = body.name
    if body.description is not None:
        expense.description = body.description
    if body.amount is not None:
        expense.amount = body.amount
    if body.frequency is not None:
        expense.frequency = body.frequency
    if body.next_due_date is not None:
        expense.next_due_date = body.next_due_date
    if body.category is not None:
        expense.category = body.category
    if body.is_active is not None:
        expense.is_active = body.is_active
    
    db.session.commit()
    return expense.to_dict()

@recurring_expense_bp.delete('/recurring-expenses/<int:expense_id>', responses={204: None})
def delete_recurring_expense(expense_id: int):
    """Deletar gasto recorrente"""
    expense = RecurringExpense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    return '', 204

@recurring_expense_bp.get('/users/<int:user_id>/recurring-expenses', responses={200: RecurringExpenseResponseSchema})
def get_user_recurring_expenses(user_id: int):
    """Buscar gastos recorrentes de um usuário específico"""
    expenses = RecurringExpense.query.filter_by(user_id=user_id).all()
    return [expense.to_dict() for expense in expenses]

