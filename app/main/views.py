from flask import render_template

from . import main


@main.route('/')
def index():
    title = 'My Pitch -- Home page'
    return render_template('index.html', title=title)


@main.route('/pitches')
def pitch():
    return render_template('pitches.html')


@main.route('/health')
def health():
    return render_template('health.html')


@main.route('/sports')
def sports():
    return render_template('sports.html')
