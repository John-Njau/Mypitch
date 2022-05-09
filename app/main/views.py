from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
from app.models import User, Pitch, Comment
from .forms import PitchForm, CommentsForm
from . import main


@main.route('/')
def index():
    # title = 'My Pitch -- Home page'
    # allpitches = Pitch.query.all()
    # business = Pitch.query.filter_by(category='Business').all()
    # technology = Pitch.query.filter_by(category='Technology').all()
    # science = Pitch.query.filter_by(category='Science').all()
    # health = Pitch.query.filter_by(category='Health').all()
    # return render_template('index.html', science=science, business=business, technology=technology, allpitches=allpitches, title=title, health=health)
    allpitches = Pitch.query.all()
    print(allpitches)
    user = current_user
    return render_template('index.html', allpitches=allpitches, user=user)


@main.route('/pitches')
@login_required
def pitches():
    allpitches = Pitch.query.all()
    # user = current_user
    return render_template('pitches.html', allpitches=allpitches, user=current_user)

@main.route('/new_pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    pitchform = PitchForm()
    if pitchform.validate_on_submit():
        addpitch = Pitch(title=pitchform.title.data, pitchtext=pitchform.pitchtext.data, category=pitchform.category.data)
        addpitch.save_pitch()
        return redirect(url_for('main.index'))
    return render_template('new_pitch.html', form=pitchform)


@main.route('/comments/<int:id>', methods=['GET', 'POST'])
@login_required
def comments(pitch_id):
    form = CommentsForm()
    pitch = Pitch.query.get(pitch_id)
    user = User.query.get()
    comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    if form.validate_on_submit():
        new_comment = Comment(comment=form.comment.data, pitch_id=pitch_id, user_id=current_user.id)
        new_comment.save_comment()
        return redirect('/comments/{pitch_id}'.format(pitch_id=pitch_id))
    return render_template('comments.html', form=form, comments=comments, pitch=pitch, user=user)

@main.route('/health')
@login_required
def health():
    return render_template('health.html')


@main.route('/science')
@login_required
def science():
    return render_template('science.html')
