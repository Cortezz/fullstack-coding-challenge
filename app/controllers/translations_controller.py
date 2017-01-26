from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.models import translation

translations = Blueprint('translations', __name__, url_prefix='/translations')

@translations.route('/')
def index():
    completed_translations = translation.get_by_status('completed')
    failed_translations = translation.get_by_status('failed')
    pending_translations = translation.get_by_status('in_progress')
    return render_template('translations/index.html',
        completed=completed_translations,
        failed = failed_translations,
        in_progress = pending_translations
    )
