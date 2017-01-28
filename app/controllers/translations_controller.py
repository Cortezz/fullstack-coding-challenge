from flask import Blueprint, render_template
from app.models import translation

translations = Blueprint('translations', __name__, url_prefix='/translations')

@translations.route('/<status>')
def index(status):
    translations = translation.get_by_status(status)
    return render_template('translations/index.html', type = status, translations = translations)
