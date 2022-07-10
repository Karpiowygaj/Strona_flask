from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Note

views = Blueprint('views',__name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        new_note = Note()
    return render_template("home.html", user=current_user)
