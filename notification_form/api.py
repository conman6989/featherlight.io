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

def get_manager_JSON():
    data = []
    response = requests.get("https://609aae2c0f5a13001721bb02.mockapi.io/lightfeather/managers")
    for i in response.json():
        if i['jurisdiction'].isdigit():
            continue
        else:
            data.append(i['jurisdiction']+" - "+i['lastName']+", "+i['firstName'])
    return sorted(data)

@bp.route("/api/supervisors", methods=("GET",))
def api_supervisors():
    """Get JSON and sort / format"""
    data = get_manager_JSON()
    # response = requests.get("https://609aae2c0f5a13001721bb02.mockapi.io/lightfeather/managers")
    # for i in response.json():
    #     if i['jurisdiction'].isdigit():
    #         continue
    #     else:
    #         data.append(i['jurisdiction']+" - "+i['lastName']+", "+i['firstName'])
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

        db = get_db()
        error = None

        if not firstName or firstName.isdigit():
            error = "First Name is required."
        elif not lastName:
            error = "Last Name is required."
        elif not email:
            error = "Email address is required."
        elif not phone:
            error = "Phone Number is required."
        elif not supervisor:
            error = "Supervisor is required."


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


# response = requests.get("https://609aae2c0f5a13001721bb02.mockapi.io/lightfeather/managers")
# df = pd.DataFrame.from_dict(response.json())
# df = df.drop(['id', 'phone', 'identificationNumber',], axis=1)
# df = df[df.jurisdiction.str.match('[a-z]')]
# df = df.sort_values(by=['jurisdiction', 'lastName', 'firstName'])
# print(df.to_json(orient="records"))

# data = []
# response = requests.get("https://609aae2c0f5a13001721bb02.mockapi.io/lightfeather/managers")
# for i in response.json():
#     if i['jurisdiction'].isdigit():
#         continue
#     else:
#         # data.append({"jurisdiction": i['jurisdiction'], "lastName":i['lastName'], "firstName":i['firstName']})
#         data.append(i['jurisdiction']+" - "+i['lastName']+", "+i['firstName'])
#     # print(i['jurisdiction']+" - "+i['lastName']+", "+i['firstName'])
# print(sorted(data))

