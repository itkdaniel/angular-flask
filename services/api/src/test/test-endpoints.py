# curl -X POST -H 'Content-Type: application/json' -d '{"title": "TypeScript Advanced Exam","description": "Tricky questions about TypeScript."}' http://localhost:5000/exams

# curl -X POST -H 'Content-Type: application/json' -d '{\"title\": \"TypeScript Advanced Exam\",\"description\": \"Tricky questions about TypeScript.\"}' http://localhost:5000/exams

# curl -X POST http://localhost:5000/exams -H 'Content-Type: application/json' -j {"title": "TypeScript Advanced Exam","description": "Tricky questions about TypeScript."}

# curl -v -H "Content-Type: application/json" -X POST -d "{ \"title\": \"TypeScript Advanced Exam\",\"description\": \"Tricky questions about TypeScript\" }" http://localhost:5000/exams

# curl http://localhost:5000


# from src.entities.post import Post,PostSchema,PostManager; from manage import app; manager = PostManager(); from datetime import datetime, timedelta, timezone; from geopy.geocoders import Nominatim; from pprint import pprint; import requests; import random; json_data = {'title':'test ' + str(random.randrange(10000,999999)),'caption':'test caption ' + str(random.randrange(100000,99999999))}; geolocator = Nominatim(user_agent="angular-flask-api"); import os