import secrets, os
from flask import Blueprint, abort, render_template, url_for, flash, redirect, request, session
from app import bcrypt
from app.forms import RegistrationForm, LoginForm, ImageUploadForm
from app.models import User, Image
from app.extensions import db
from flask_login import login_user, current_user, logout_user, login_required

bp = Blueprint('main', __name__)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(os.getcwd(), 'app/static/images', picture_fn)
    form_picture.save(picture_path)
    return picture_fn

@bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check Username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@bp.route("/", methods=["GET", "POST"])
def home():
    search = request.args.get('search')
    if search:
        images = Image.query.join(User).filter(User.username.like(f"%{search}%")).order_by(Image.date_posted.desc()).all()
    else:
        images = Image.query.join(User).order_by(Image.date_posted.desc()).all()
    image_ids = [image.id for image in images]
    session['image_ids'] = image_ids
    return render_template("home.html", images=images, search=search)

@bp.route("/upload_image", methods=['GET', 'POST'])
@login_required
def upload_image():
    images = Image.query.filter_by(user_id=current_user.id).order_by(Image.date_posted.desc()).all()
    image_ids = [image.id for image in images]
    session['image_ids'] = image_ids
    form = ImageUploadForm()
    if form.validate_on_submit():
        if form.image.data:
            picture_file = save_picture(form.image.data)
            image = Image(image_url=picture_file, description=form.description.data, user_id=current_user.id)
            db.session.add(image)
            db.session.commit()
            flash('Your image has been uploaded!', 'success')
            return redirect(url_for('main.upload_image'))
    return render_template('upload_image.html', title='Upload Image', form=form, images=images)


@bp.route('/image/<int:image_id>')
def view_image(image_id):
    image_ids = session.get('image_ids', [])
    image = Image.query.get_or_404(image_id)
    
    if image_id not in image_ids:
        next_image = None
        prev_image = None
    
    current_index = image_ids.index(image.id)
    next_image_id = image_ids[current_index + 1] if current_index < len(image_ids) - 1 else None
    prev_image_id = image_ids[current_index - 1] if current_index > 0 else None
    
    next_image = Image.query.get(next_image_id) if next_image_id else None
    prev_image = Image.query.get(prev_image_id) if prev_image_id else None

    return render_template('view_image.html', image=image, next_image=next_image, prev_image=prev_image) 


@bp.route('/delete_image/<int:image_id>', methods=['POST'])
@login_required
def delete_image(image_id):
    image = Image.query.get_or_404(image_id)
    if image.user_id != current_user.id:
        abort(403)  # Forbidden

    db.session.delete(image)
    db.session.commit()
    flash('Image has been deleted!', 'success')
    return redirect(url_for('main.home'))
