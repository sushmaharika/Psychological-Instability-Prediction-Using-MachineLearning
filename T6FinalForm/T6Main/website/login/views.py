
from django.http import HttpResponse
from django.shortcuts import render, redirect
import mysql.connector as sql
import subprocess
import requests  # Import requests to make HTTP calls

def loginaction(request):
    if request.method == "POST":
        connection = sql.connect(host="localhost", user="root", passwd="456admin", database='website')
        cursor = connection.cursor()
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        query = "SELECT * FROM register WHERE email=%s AND password=%s"
        cursor.execute(query, (email, password))
        user = cursor.fetchone()
        try:
            subprocess.Popen(['python', 'app.py'], cwd='../') 
        except Exception as e:
            print(f"Error starting Flask app: {e}")
        if user is None:
            return render(request, "error.html")
        else:
            # Here you make a POST request to Flask app's login endpoint
            # flask_response = requests.post('http://localhost:5000/', data={'username': email, 'password': password})
            # return HttpResponse(flask_response.text)  # Display Flask's response directly or handle as needed
            return redirect('http://localhost:5000/')

    return render(request, 'login_page.html')
    