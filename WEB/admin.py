from flask import Blueprint, request, render_template, redirect, url_for, flash,session, jsonify
from .model import Admin, LoginDataBase
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user

admin = Blueprint('admin', __name__)

@admin.route('/admin15541778@@')
def AdminLogin():
    return redirect(url_for('admin.check_admin'))

# code = 1554%%
# pass = nazar





@admin.route('/add', methods =['POST', 'GET'])
def check_admin():
    session['login'] = False
    if request.method == 'POST':
        code = request.form['code']
        password = request.form['password']
        admin_user = Admin.query.filter_by(code = code).first()
        if admin_user != None:
            if code != admin_user.code:
                flash('not admin')
            elif code == admin_user.code:
                password = check_password_hash(admin_user.password, password=password)
                if not password:
                    flash('wrong password')
                    return redirect(url_for('auth.login'))
                else:
                    session['login'] = True
                    return redirect(url_for('admin.adminPage'))
        else:
            flash('login not successful')
            session['login'] = False
            return redirect(url_for('auth.login'))
    return render_template('add.html')




@admin.route('/admin', methods = ['POST','GET'])
def adminPage():
    users = LoginDataBase.query.all()
    try:
        if session['login'] == False:
            return redirect(url_for('auth.login'))
    except KeyError:
        return redirect(url_for('admin.check_admin'))
    if request.method == 'POST':
        session['userID'] = userID = request.form['userID']
        return redirect(url_for('admin.view_user'))
    return render_template('adminDashbord.html', user = users)


@admin.route('/view-user', methods=['POST','GET'])
def view_user():
    getUser = LoginDataBase.query.get_or_404(int(session['userID']))
    return getUser.username
    # try:
    #     if session['login'] == False:
    #         return redirect(url_for('auth.login'))
    # except KeyError:
    #     return redirect(url_for('admin.check_admin'))
    # getUser = LoginDataBase.query.get_or_404(session['userID'])
    # return getUser
    