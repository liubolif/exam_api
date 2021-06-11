# -*- coding: utf-8 -*-
from flask import render_template
from flask import current_app as app


@app.route("/")
def about():
    return render_template('about.html')



