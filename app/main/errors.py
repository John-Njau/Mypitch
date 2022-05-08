from flask import render_template
from . import main

@main.errorhandler(404)
def errors(error):
    """To render the 404 error page"""
    return render_template('errorpage.html'), 404
    