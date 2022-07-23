from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    note = request.form.get('note')
    user = str(current_user)
    user = user.replace(">", "")
    user = user.split()
    rows = db.session.query(Note).filter(Note.user_id == user[1]).count()
    if request.method == 'POST':

        if len(note) < 1:
            flash('Note is too short', category='error')

        else:
            new_note = Note(notatka=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            return redirect(url_for("views.home"))

    return render_template("home.html", user=current_user, rows=rows)


@views.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_post(id):
    post_to_delete = Note.query.get_or_404(id)
    try:
        db.session.delete(post_to_delete)
        db.session.commit()
        flash("Post successfully deleted", category="error")
        return redirect(url_for('views.home'))
    except:
        flash('Something goes wrong', category="error")


@views.route('/edit_post/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    post_to_edit = Note.query.get_or_404(id)

    if request.method == 'POST':
        note = request.form.get('note')
        post_to_edit.notatka = note
        db.session.commit()
        flash('Note edited!', category='success')
        return redirect(url_for('views.home'))
    else:
        pass

    return render_template("edit_post.html", user=current_user, post_to_edit=post_to_edit)
