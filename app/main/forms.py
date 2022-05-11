from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    pitchtext = TextAreaField('Pitch', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Business', 'Business'),('Technology','Technology'), ('Science','Science'), ('Health','Health')] ,validators=[DataRequired()])
    submit = SubmitField('Post')
    
class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post')
        
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio', validators=[DataRequired()])
    submit = SubmitField('Save')