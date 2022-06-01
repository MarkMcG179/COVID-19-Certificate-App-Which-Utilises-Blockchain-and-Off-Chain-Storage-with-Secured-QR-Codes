from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User, Cert
from werkzeug.security import check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from blockchain import *
from . import storeHash

auth = Blueprint('auth', __name__)
db_file = "database.db"


@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        accountNum = request.form.get('accountNum')
        password = request.form.get('password')

        user = User.query.filter_by(accountNum=accountNum).first()
        if user:
            if check_password_hash(user.password, password):
                if 1 <= user.accountNum <= 4999:
                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('auth.vaccineDetails'))

                elif 5000 <= user.accountNum <= 9999:
                    flash('Logged in successfully!', category='success')
                    login_user(user, remember=True)
                    return redirect(url_for('auth.adminMenu'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Account does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/adminMenu', methods=['GET', 'POST'])
@login_required
def adminMenu():
    return render_template("admin_menu.html", user=current_user)

@auth.route('/vaccineDetails')
def vaccineDetails():
    id = current_user.get_id()
    certs = Cert.query.filter_by(user_id=id).first()
    return render_template("vaccineDetails.html", user=current_user, certs=certs)

@auth.route('/certRecords',  methods=['GET', 'POST'])
def certRecords():
    certs = Cert.query.all()
    length = len(certs)   

    if request.method == 'POST':
        password = request.form.get('password')
        user_id = request.form.get("action") 
        session['user_id'] = user_id
        user = User.query.filter_by(id=user_id).first()

        if user:            
            if check_password_hash(user.password, password):
                flash('Record Unlocked', category='success')
                return redirect(url_for('auth.verify'))
    return render_template("certRecords.html", user=current_user, length=length, certs=certs)

@auth.route('/chain')
@login_required
def chain():
    block = B
    return render_template("blockchain.html", user=current_user, block=block)

@auth.route('/verify', methods=['GET', 'POST'])
@login_required
def verify():
    user_id = session.get('user_id')
    certs = Cert.query.filter_by(user_id=user_id).first()
    users = User.query.filter_by(id=user_id).first()
    people = [Individual_1, Individual_2, Individual_3, Individual_4, Individual_5, Individual_6]
    index = int(user_id) - 1
    block_hash = people[index]['data_hash']
    store_hash = storeHash.main()

    if block_hash != store_hash:
        flash('Records in Storage Have Been Altered!', 'error')
    
    return render_template("verify.html", user=current_user, certs=certs, users=users, block_hash=block_hash, store_hash=store_hash)