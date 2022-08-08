from flask import current_app
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from . import forms
from . import models


def index():
    return render_template('private/index.html')
