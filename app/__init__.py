import app.tools.mongo_tools as at
from flask_wtf.csrf import CsrfProtect


from flask import Flask

cat = at.Catalog()
cat.load_collection()

app = Flask(__name__)
app.config.update(
    CSRF_ENABLED = True,
    DEBUG=True,
    SECRET_KEY='Tiglatpolosar'
)
CsrfProtect(app)
from app import views