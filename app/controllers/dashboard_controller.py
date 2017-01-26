from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.models import translation

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard.route('/')
def show():
    completed_translations = translation.get_by_status('completed').count()
    failed_translations = translation.get_by_status('failed').count()
    pending_translations = translation.get_by_status('in_progress').count()
    return render_template('dashboard/show.html',
        completed = completed_translations,
        failed = failed_translations,
        in_progress = pending_translations
    )
