from flask import render_template, redirect, url_for, request, abort
from flask_login import current_user, login_required
from app.models import User, Pitch, Comment, Upvote, Downvote
from .forms import PitchForm, CommentsForm, UpdateProfile
from . import main
from .. import db, photos


@main.route('/')
def index():
    allpitches = Pitch.query.all()
    users =current_user
    return render_template('index.html', allpitches=allpitches, users=users)

@main.route('/pitches')
@login_required
def pitches(id):
    allpitches = Pitch.query.all()
    user = User.query.get(id)
    return render_template('pitches.html', allpitches=allpitches, user=user)

@main.route('/new_pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    pitchform = PitchForm()
    if pitchform.validate_on_submit():
        addpitch = Pitch(title=pitchform.title.data, pitchtext=pitchform.pitchtext.data, category=pitchform.category.data, user_id=current_user.id)
        addpitch.save_pitch()
        return redirect(url_for('main.index'))
    return render_template('new_pitch.html', form=pitchform)


@main.route('/comments/<int:id>', methods=['GET', 'POST'])
@login_required
def comments(id):
    allcomments =Comment.query.all()
    # allcomments = Comment.query.filter_by(pitch_id=id).all()
    form = CommentsForm()
    pitch = Pitch.query.get(id)
    user = User.query.get(id)
    comments = Comment.query.filter_by(pitch_id=id).all()
    if form.validate_on_submit():
        new_comment = Comment(commenttext=form.comment.data, pitch_id=id, user_id=current_user.id)
        new_comment.save_comment()
        return redirect('/comments/{pitch_id}'.format(pitch_id=id))
    return render_template('comments.html', form=form, comments=comments, allcomments=allcomments, pitch=pitch, user=user)

@main.route('/upvote/<int:id>', methods=['GET', 'POST'])
@login_required
def upvote(id):
    pitch = Pitch.query.get(id)
    new_vote = Upvote(pitch = pitch, upvote = 1, user_id = current_user.id)
    new_vote.save_upvote()
    return redirect(url_for('main.index'))

@main.route('/downvote/<int:id>', methods=['GET', 'POST'])
@login_required
def downvote(id):
    pitch = Pitch.query.get(id)
    new_downvote = Downvote(pitch = pitch,downvote = 1, user_id=current_user.id)
    new_downvote.save_downvote()
    return redirect(url_for('main.index'))
    

@main.route('/health')
@login_required
def health():
    allpitches = Pitch.query.filter_by(category='Health').all()
    return render_template('health.html', allpitches=allpitches)


@main.route('/science')
@login_required
def science():
    allpitches = Pitch.query.filter_by(category='Science').all()
    return render_template('science.html', allpitches=allpitches)

@main.route('/technology')
@login_required
def technology():
    allpitches = Pitch.query.filter_by(category='Technology').all()
    return render_template('technology.html', allpitches=allpitches)

@main.route('/business')
@login_required
def business():
    allpitches = Pitch.query.filter_by(category='Business').all()
    return render_template('business.html', allpitches=allpitches)


# UPDATE REQUESTS
@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
        
    form = UpdateProfile()
    
    if form.validate_on_submit():
        user.bio = form.bio.data
        
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.profile', uname=user.username))
    
    return render_template('profile/update.html', form=form)

# views
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    
    if user is None:
        abort(404)
        
    return render_template("profile/profile.html", user=user)

@main.route('/user/<pitches>', methods=['GET', 'POST'])
def mypitches():
    allpitches = User.query.filter_by(pitches=pitches).all()
    return render_template('my_pitches.html', allpitches=allpitches)
