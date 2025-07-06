import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import redirect, send_from_directory
from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS
from src.models.user import db
from src.models.subscription import Subscription
from src.models.recurring_expense import RecurringExpense
from src.routes.user import user_bp
from src.routes.subscription import subscription_bp
from src.routes.recurring_expense import recurring_expense_bp

info = Info(title="Sistema de Gestão de Assinaturas e Gastos Recorrentes", version="1.0.0")
app = OpenAPI(__name__, info=info, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Configurar banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar banco de dados
db.init_app(app)

# Habilitar CORS para permitir requisições do frontend
CORS(app)

# Registrar blueprints
app.register_api(user_bp)
app.register_api(subscription_bp)
app.register_api(recurring_expense_bp)

@app.route('/')
def home():
    return redirect('/openapi/swagger')

# Criar tabelas do banco de dados
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

