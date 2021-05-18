# from flask import Blueprint, redirect


# auth = Blueprint('auth', __name__)


# @auth.route('/sign_up', methods=['POST', 'GET'])
# def sign_up():
#     return 'sign up'


# @auth.route('/login', methods=['POST', 'GET'])
# def sign_up():
#     return 'login'


# @auth.route('/logout')
# def sign_up():
#     return 'sign up


from flask import Blueprint, redirect auth = Blueprint('auth', __name__)


@auth.route('sign_up', methods=['POST', 'GET'])
def sign_up():
    return 'sign up'


@auth.route('login', methods=['POST', 'GET'])
def login():
    return 'login'
