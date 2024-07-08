from flask import Blueprint,render_template,session,request,redirect,url_for,flash
from flask_login import current_user,login_required
from .model import Balance,Current,Utility,Savings,Dollar,LoginDataBase,Track_Deposite, Track_Transaction, Debit
from . import db
from datetime import datetime
from werkzeug.security import check_password_hash,generate_password_hash

view = Blueprint('view',__name__)

@view.route('/')
def home():
    return render_template('bank.html')



@view.route('/account_number', methods = ['POST','GET'])
@login_required
def accountNum():
    if request.method == 'POST':
        user_acc = request.form['acc']
        
        return redirect(url_for('view.userDash'))
    try:
        return render_template('generate_accNum.html', value = session['num'])
    except:
        return render_template('generate_accNum.html', value = current_user.accnum)
    
@view.route('/dashBoard', methods=['GET','POST'])
@login_required
def userDash():
    if request.method == 'POST':
        session['amt'] = amount  =request.form['amount']
        return redirect(url_for('view.Transac'))
    return render_template('userpage.html',
                           name = current_user.username.capitalize(),
                           balance = format( current_user.balance.money, ','),
                           utility =format( current_user.balance.utility.amount, ','),
                           current = format( current_user.balance.current.amount, ','),
                           savings = format( current_user.balance.savings.amount, ','),
                           dollar = format( current_user.balance.dollar.amount, ','),
                           message =Track_Deposite.query.filter_by(user_id=current_user.id).all(),
                           message2 =Track_Transaction.query.filter_by(user_id=current_user.id).all(),
                           message3 = Debit.query.filter_by(user_id = current_user.id).all(),
                           )

@view.route('/deposite', methods = ['POST','GET'])
@login_required
def deposite():# AZUDONI VICTORY CHUWKUNEKU WORK
    if request.method == 'POST':
        options = request.form['depositeType']
        session['amount'] = amount = float(request.form['amount'])
        if options == 'Dollar':
            current_user.balance.dollar.amount += amount
            db.session.commit()

            current_user.balance.money += current_user.balance.dollar.amount
            db.session.commit()# AZUDONI VICTORY CHUWKUNEKU WORK

            deposite_tracker = Track_Deposite(text =f" Deposited to {options} Account",deposite_amount  = format(amount,',') ,user_id = current_user.id )
            db.session.add(deposite_tracker)
            db.session.commit()
            return redirect(url_for('view.userDash'))
        elif options == 'Current':
            current_user.balance.current.amount += amount
            db.session.commit()
            current_user.balance.money += current_user.balance.current.amount
            db.session.commit()
                        
            deposite_tracker = Track_Deposite(text =f" Deposited to {options} Account",deposite_amount  = format(amount,',') ,user_id = current_user.id)
            db.session.add(deposite_tracker)
            db.session.commit()
            return redirect(url_for('view.userDash'))
        elif options == "Utility":
            current_user.balance.utility.amount += amount
            db.session.commit()
            current_user.balance.money += current_user.balance.utility.amount
            db.session.commit()

            deposite_tracker = Track_Deposite(text =f" Deposited to {options} Account",deposite_amount  = format(amount,','),user_id = current_user.id )
            db.session.add(deposite_tracker)
            db.session.commit()
            return redirect(url_for('view.userDash'))
        elif options == 'Savings':
            current_user.balance.savings.amount += amount
            db.session.commit()
            current_user.balance.money += current_user.balance.savings.amount
            db.session.commit()

            deposite_tracker = Track_Deposite(text =f" Deposited to {options} Account",deposite_amount  = format(amount,',') ,user_id = current_user.id )
            db.session.add(deposite_tracker)
            db.session.commit()
            return redirect(url_for('view.userDash'))

    return render_template('deposite.html', accnum = current_user.accnum )

    
    
@view.route('/transfer')
@login_required
def transfer():
    return render_template('maketransaction.html')



@view.route('/transaction', methods = ['GET', 'POST'])
@login_required
def Transac():
    user = LoginDataBase.query.all()
    
    if request.method == 'POST':
        options = request.form['transacType']
        option2 = request.form['people_name']
        amount = float(request.form['transfer-amount'])
        if options == "Dollar":
            username = LoginDataBase.query.filter_by(name = option2).first()
            
            if current_user.balance.dollar.amount< amount:
                flash('low funds')
            else:
                username.balance.money += amount
                db.session.commit()
                
                transaction_tracker = Track_Transaction(text = f"Transfer From {current_user.name}", transfer_amount = format(amount, ','), user_id = username.id)
                db.session.add(transaction_tracker)
                db.session.commit()
                
                current_user.balance.dollar.amount -= amount
                db.session.commit()
                
                current_user.balance.money -= amount
                db.session.commit()
                
                debit = Debit(text = f"Debited", debit_amount = format(amount, ','), user_id = current_user.id)
                db.session.add(debit)# AZUDONI VICTORY CHUWKUNEKU WORK
                db.session.commit()
                return redirect(url_for('view.userDash'))
            
        elif options == "Savings":
            username = LoginDataBase.query.filter_by(name = option2).first()
            
            if current_user.balance.savings.amount< amount:
                flash('low funds')
            else:
                username.balance.money += amount
                db.session.commit()
                
                transaction_tracker = Track_Transaction(text = f"Transfer From {current_user.name}", transfer_amount = format(amount, ','), user_id = username.id)
                db.session.add(transaction_tracker)
                db.session.commit()
                
                current_user.balance.savings.amount -= amount
                db.session.commit()
                
                current_user.balance.money -= amount
                db.session.commit()
                
                debit = Debit(text = f"Debited", debit_amount = format(amount, ','), user_id = current_user.id)
                db.session.add(debit)
                db.session.commit()
                return redirect(url_for('view.userDash'))
            
        elif options == "Current":
            username = LoginDataBase.query.filter_by(name = option2).first()
            
            if current_user.balance.current.amount< amount:
                flash('low funds')
            else:
                username.balance.money += amount
                db.session.commit()
                
                transaction_tracker = Track_Transaction(text = f"Transfer From {current_user.name}", transfer_amount = format(amount, ','), user_id = username.id)
                db.session.add(transaction_tracker)
                db.session.commit()
                
                current_user.balance.current.amount -= amount
                db.session.commit()
                
                current_user.balance.money -= amount
                db.session.commit()
                
                debit = Debit(text = f"Debited", debit_amount = format(amount, ','), user_id = current_user.id)
                db.session.add(debit)
                db.session.commit()
                return redirect(url_for('view.userDash'))
            
        elif options == "Utility":
            username = LoginDataBase.query.filter_by(name = option2).first()
            
            if current_user.balance.utility.amount< amount:
                flash('low funds')
            else:
                username.balance.money += amount
                db.session.commit()
                
                transaction_tracker = Track_Transaction(text = f"Transfer From {current_user.name}", transfer_amount = format(amount, ','), user_id = username.id)
                db.session.add(transaction_tracker)
                db.session.commit()
                
                current_user.balance.utility.amount -= amount
                db.session.commit()
                
                current_user.balance.money -= amount
                db.session.commit()
                
                debit = Debit(text = f"Debited", debit_amount = format(amount, ','), user_id = current_user.id)
                db.session.add(debit)
                db.session.commit()
                return redirect(url_for('view.userDash'))
    try:
        return render_template('indextrans.html',amount = session['amt'], user = user)
    except KeyError:
        return render_template('indextrans.html',amount = 0, user = user)# AZUDONI VICTORY CHUWKUNEKU WORK


@view.route('/settings')
@login_required
def setting():
    return render_template('security.html')


@view.route('/editProfile')
@login_required# AZUDONI VICTORY CHUWKUNEKU WORK
def profile():
    return render_template('profile.html')

@view.route('/username', methods= ['POST', 'GET'])
@login_required
def username():
    user = LoginDataBase.query.get_or_404(current_user.id)
    if request.method == 'POST':
        usernm = request.form['username']
        user.username = usernm
        db.session.commit()
        return redirect(url_for('view.userDash'))
    return render_template('username.html', username = user.username)

@view.route('/password', methods =['POST','GET'])
@login_required
def password():
    user = LoginDataBase.query.get_or_404(current_user.id)
    if request.method =='POST':
        userpass = request.form['password']
        confirmPass = request.form['confirm-password']
        if userpass != confirmPass:
            flash('not correct')
            return redirect(url_for('view.password'))
        user.password = generate_password_hash(userpass)
        db.session.commit()
        return redirect(url_for('view.userDash'))
    return render_template('password.html')

@view.route('/transaction-pin')
@login_required
def transaction_pin():
    return render_template('transaction pin.html')

@view.route('/account-number')
@login_required
def displayAcc():
    num = current_user.accnum
    return render_template('displayAcc.html', accountNum = num)


@view.route('/card')
@login_required
def displayCard():
    user = current_user.name
    num = current_user.accnum
    return render_template('card.html', name =user, account =num )