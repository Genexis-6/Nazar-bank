from flask import Blueprint,request,session,render_template,flash,redirect,url_for,session
from .model import LoginDataBase,Balance,Utility,Savings,Current,Dollar,Track_Deposite
from werkzeug.security import check_password_hash,generate_password_hash
from . import db
from .accountNum import AccNum
from flask_login import login_user, logout_user,login_required,current_user
auth = Blueprint('auth',__name__)
import socket

# AZUDONI VICTORY CHUWKUNEKU WORK

@auth.route('/register',methods = ['POST','GET'])
def register():
    num = AccNum()
    acc = num.accnum
    check_name = LoginDataBase.query.all()
    registered_name = [name.name for name in check_name]
    if request.method == 'POST':
        session['num'] = acc
        session['name'] = name = request.form['name']
        session['email'] = email = request.form['email']
        session['username'] = username = request.form['username']
        session['phone'] = phone = request.form['phone']
        session['password'] = password = request.form['password']
        session['confirm_pass'] = confirm_pass = request.form['confirm_pass']
        # AZUDONI VICTORY CHUWKUNEKU WORK
        
        if len(name) <3:
            flash('Name length must be greater than 3')
        elif len(username) < 3:
            flash('Username length must be greater than 3')
        elif len(password)<6 :
            flash('password length too short')     
        elif len(phone) != 11:
            flash('Phone number must be atleast 11 digit ')
        elif password != confirm_pass:
            flash('password must be same as "Confirm password"!!!')
        elif name in registered_name:
            flash('Name already exist')
        else:
            user = LoginDataBase.query.filter_by(email = email).first()
            if user == None:
                password = generate_password_hash(password=password)
                user = LoginDataBase(name = name,username = username, email = email,phone = phone, password = password, accnum = session['num'])
                db.session.add(user)
                db.session.commit()
                login_user(user)
                
                balance = Balance(money = 0.0, user_id = user.id, name = name)
                db.session.add(balance)
                db.session.commit()
                
                current = Current(amount = 0.0, user_id = balance.id, name = name)
                db.session.add(current)
                db.session.commit()
                
                utility = Utility(amount = 0.0, user_id = balance.id, name = name)
                db.session.add(utility)
                db.session.commit()
                
                dollar = Dollar(amount = 0.0, user_id = balance.id, name = name)
                db.session.add(dollar)
                db.session.commit()
                
                savings = Savings(amount = 0.0, user_id = balance.id, name = name)
                db.session.add(savings)
                db.session.commit()
            
                flash('registration successful')
                return redirect(url_for('view.accountNum')) 
            else:
                flash('User already exist')
    try:
        return render_template('register.html',name = session['name'],email = session['email'],username = session['username'],password = session['password'],phone = session['phone'])
    except KeyError:
        return render_template('register.html',name = '',email = '',username = '',password = '',phone = '')
    
    
    
@auth.route('/login', methods = ['POST','GET'])
def login():
    # AZUDONI VICTORY CHUWKUNEKU WORK
    if request.method == 'POST':
        session['EA'] = useremail = request.form['EA']
        session['PD'] = userPASSWORD = request.form['PD']
        user = LoginDataBase.query.filter_by(email = useremail).first()
        if user != None:
            check_user_pass = check_password_hash(user.password, password= userPASSWORD)
            if check_user_pass:
                login_user(user)
                session['user_id'] = user.id
                return redirect(url_for('view.userDash'))
            else:
                
                flash('wrong pass')
        else:
            flash('user not found!!... check your email spelling and try again')
    try:        
        return render_template('login.html',email = session['EA'])
    except KeyError:
        return render_template('login.html',email = '')

    
    
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout was successful')
    return redirect(url_for('auth.login'))
    
    
@auth.route('/forgotPass',methods = ['POST','GET'])
def forgotPass():
    from fg_pass import Otp,ForgottenPassword
    if request.method == 'POST':
        useremail = request.form['email']
        user = LoginDataBase.query.filter_by(email = useremail).first()
        if user == None:
            flash('user not found')
        else:
            try:# AZUDONI VICTORY CHUWKUNEKU WORK
                login_user(user)
                num = Otp()
                session['otp'] = num.code
                ForgottenPassword(useremail=useremail,code=session['otp'])
                flash(f'an otp was sent to {useremail}')
                return redirect(url_for('auth.confirmOTP'))
            except socket.gaierror as e:
                flash(f'not successfull {e}...check your internet connection')
                return redirect(url_for('auth.forgotPass'))
    return render_template('forgetten_password.html')
        
        
        
@auth.route('/confirm-otp',methods = ['POST','GET'])
def confirmOTP():
    if request.method == 'POST':# AZUDONI VICTORY CHUWKUNEKU WORK
        otp = request.form['otp']
        if session['otp'] == otp:
            return redirect(url_for('auth.updatePass'))
        else:
            flash('fail')
    return render_template('confirmotp.html')


@auth.route('/update-password',methods = ['POST','GET'])
@login_required
def updatePass():
    user = LoginDataBase.query.get_or_404(current_user.id)
    if request.method == 'POST':
        password = request.form['password']
        confimPass = request.form['confirm_pass']
        
        if password != confimPass:
            flash('password must match with confirm password')
        else:
            flash('updated successfully')
            user.password = generate_password_hash(password)
            db.session.commit()
            return redirect(url_for('view.userDash'))
    return render_template('updatePass.html',name = user.name, email = user.email, phone = user.phone,username = user.username)# AZUDONI VICTORY CHUWKUNEKU WORK


@auth.route('/check')
def hmm():

    return registered_name