from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.models import translation

translations = Blueprint('translations', __name__, url_prefix='/translations')

@translations.route('/<status>')
def index(status):
    translations = translation.get_by_status(status)
    return render_template('translations/index.html', type = status, translations = translations)
