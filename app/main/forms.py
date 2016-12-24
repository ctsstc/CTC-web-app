from flask_wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, SubmitField, DateField, SelectField, PasswordField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Role, User

class LoginForm(Form):
	username = StringField('username', validators=[Required()])
	password = PasswordField('password', validators=[Required()])
	remember_me = BooleanField('remember_me', default=False)


class EditProfileForm(Form):
	name = StringField('Name', validators=[Length(0, 64)])
	location = StringField('Location', validators=[Length(0, 64)])
	about_me = TextAreaField('About Me')
	grad_date = DateField('Graduation Date', format='%m/%d/%Y')
	submit = SubmitField('Submit')


class EditProfileAdminForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	username = StringField('Username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
													0, 'Usernames must have only letters, numbers, dots, or underscores')])
	confirmed = BooleanField('Confirmed')
	role = SelectField('Role', coerce=int)
	name = StringField('Name', validators=[Length(0, 64)])
	location = StringField('Location', validators=[Length(0, 64)])
	about_me = TextAreaField('About Me')
	submit = SubmitField('Submit')

	def __init__(self, user, *args, **kwargs):
		super(EditProfileAdminForm, self).__init__(*args, **kwargs)
		self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
		self.user = user

	def validate_email(self, field):
		if field.data != self.user.email and User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')

	def validate_username(self, field):
		if field.data != self.user.username and User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')


class PostForm(Form):
	title = StringField('Title', validators=[Required()])
	body = PageDownField('Body', validators=[Required()])
	submit = SubmitField('Submit')