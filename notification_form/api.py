import requests, json, sys
import logging
import pandas as pd
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify
from werkzeug.exceptions import abort


from notification_form.auth import login_required
from notification_form.db import get_db

bp = Blueprint("api", __name__)

def get_manager_JSON(last_name=None):
    # last_name='Dere'
    data = []
    response = requests.get("https://609aae2c0f5a13001721bb02.mockapi.io/lightfeather/managers")
    for i in response.json():
        if i['jurisdiction'].isdigit():
            continue
        elif last_name == None:
            data.append(i['jurisdiction']+" - "+i['lastName']+", "+i['firstName'])
        elif i['lastName'].lower()[0] == last_name[0].lower():
            data.append(i['jurisdiction']+" - "+i['lastName']+", "+i['firstName'])
    return sorted(data)

@bp.route("/api/supervisors", methods=("GET",))
def api_supervisors():
    """Get JSON and sort / format"""
    last_name = request.args.get("lastname")
    data = get_manager_JSON()
    return jsonify(sorted(data))

@bp.route("/api/submit", methods=("POST",))
def api_submit():
    """Notification Form endpoint.
    Validates inputs and prints to console.
    """
    if request.method == "POST":
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        email = request.form["email"]
        phone = request.form["phone"]
        supervisor = request.form["supervisor"]
        email_checkbox = False
        if request.form.get("email_checkbox"):
            email_checkbox = request.form.get("email_checkbox")
        phone_checkbox = False
        if request.form.get("phone_checkbox"):
            phone_checkbox = request.form.get("phone_checkbox")

        db = get_db()
        error = None

        if not firstName or firstName.isdigit():
            error = "First Name is required and cannot be a number"
        elif not lastName or lastName.isdigit():
            error = "Last Name is required and cannot be a number"
        elif not email:
            error = "Email address is required."
        elif not phone:
            error = "Phone Number is required."
        elif not supervisor:
            error = "Supervisor is required."
        elif email_checkbox == False and phone_checkbox == False:
            error = "Checkbox is required."


        if error is not None:
            flash(error)
        else:
            print(request, file=sys.stdout)
            print(request.form, file=sys.stdout)
            # db.execute(
            #     "INSERT INTO notification_post (firstName, lastName, email, phone, supervisor) VALUES (?,?,?,?,?)",
            #     (firstName, lastName, email, phone, supervisor),
            # )
            # db.commit()
    return redirect(url_for("blog.index"))

# print(get_manager_JSON())
