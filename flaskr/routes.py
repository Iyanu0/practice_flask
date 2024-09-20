from flask import render_template, url_for, redirect, request, flash
from flaskr import app
from flaskr.models import db, User
from flaskr.forms import UserForm

@app.route('/')
@app.route('/home')
def home(): 
    return render_template('home.html',title='Home Page')

@app.route('/list')
def user_list():
    error=None
    users=db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template('user_list.html',title='User List',users=users)

@app.route('/create_user',methods=['GET','POST'])
def create_user():  
    error=None
    form = UserForm()
    if form.validate_on_submit():
        user=User(
            username=form.username.data,
            email=form.email.data
        )
        existing_user=User.query.filter_by(username=user.username).first()
        if existing_user:
            error='This username is Taken'
            flash(error)
            db.session.rollback()
            return redirect(url_for('create_user'))
        else:
            db.session.add(user)
            db.session.commit()
            flash('You have successfully added a User')
            return redirect(url_for('user_list',id=user.id))
    return render_template('create_user.html',title='Create User',form=form)

@app.route('/list/<int:id>/delete',methods=['GET','POST'])#This is to get the id of the user to be deleted
def delete(id):
    user=db.get_or_404(User,id)
    if request.method == 'POST':   
        db.session.delete(user)
        db.session.commit()
        flash('You deleted a User')
        return redirect(url_for('user_list'))


with app.app_context():
    db.create_all()