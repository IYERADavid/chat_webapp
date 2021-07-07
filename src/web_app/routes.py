from web_app.app import app
from flask import render_template, redirect, url_for, flash, session, request

@app.route('/', methods=['GET'])
def index():
    return "hey fellow engineers"
