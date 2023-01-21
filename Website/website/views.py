from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
import datetime
'''
import pyrebase

# Firebase Database (Online)
firebaseConfig = {
    "apiKey": "AIzaSyAkD-Ehz2IOwx4iA3jL_dZPpzog3vaaY94",
    "authDomain": "home-automation-794c1.firebaseapp.com",
    "databaseURL": "https://home-automation-794c1-default-rtdb.firebaseio.com",
    "projectId": "home-automation-794c1",
    "storageBucket": "home-automation-794c1.appspot.com",
    "messagingSenderId": "204270994860",
    "appId": "1:204270994860:web:2372c400f7c7f0cd272609"
}

firebase = pyrebase.initialize_app(firebaseConfig)
fb_db = firebase.database()
'''

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html', user=current_user)


@views.route('/features')
def features():
    return render_template('features.html', user=current_user)


@views.route('/pricing')
def pricing():
    return render_template('pricing.html', user=current_user)


@views.route('/faq')
def faq():
    return render_template('faq.html', user=current_user)


@views.route('/about-us')
def about_us():
    return render_template('about-us.html', user=current_user)


@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)
