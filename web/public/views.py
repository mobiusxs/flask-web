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
    form = forms.LogbookForm()
    if form.validate_on_submit():
        first = form.data['first']
        last = form.data['last']
        record = models.LogbookModel(first=first, last=last)
        models.db.session.add(record)
        models.db.session.commit()
        flash('You signed! View the database table in the Admin site.')
    return render_template('public/index.html', form=form)
