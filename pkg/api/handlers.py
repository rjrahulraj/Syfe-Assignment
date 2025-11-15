from flask import Flask, request, jsonify

app = Flask(__name__)

def health_check_handler():
    return "OK", 200

def get_user_handler():
    return "", 200

def create_user_handler():
    return "", 200

def update_user_handler():
    return "", 200

def delete_user_handler():
    return "", 200

