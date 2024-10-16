from django.shortcuts import render, redirect
import mysql.connector as sql
import subprocess  # Import subprocess to run the Flask app

def loginaction(request):
    global em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="456admin", database='website')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "select * from register where email='{}' and password='{}'".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, "error.html")
        else:
            # Redirect to a URL that triggers execution of Flask app using subprocess
            print("ready to redirect")
            return redirect('/run_flask_app/')
            print("reirected already")
    return render(request, 'login_page.html')

import subprocess

# def run_flask_app(request):
#     # Use subprocess to run your Flask app
#     print("flask ready to start")
#     subprocess.run(['py', '../app.py']) 
#     print("flask run successfully") # Replace 'path/to/your/flask_app.py' with the actual path to your Flask app
#     # return render(request, "welcome.html")  # You can render a template or redirect as needed after executing the Flask app
#     return HttpResponse("Flask application executed successfully.")
from django.http import HttpResponse

def run_flask_app(request):
    # Use subprocess to run your Flask app
    try:
        print("Flask ready to start")
        # Note: Ensure the path to your Flask app is correct and accessible
        subprocess.run(['py', '../app.py'])  # Adjust this command as needed
        print("Flask run successfully")
    except Exception as e:
        print(f"Failed to start Flask app: {e}")
        return HttpResponse("Failed to start Flask application.", status=500)

    # After running the Flask app, return an appropriate response
    # For example, redirecting to another Django-handled page or just showing a success message
    return HttpResponse("Flask application executed successfully.")
