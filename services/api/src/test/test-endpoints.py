# curl -X POST -H 'Content-Type: application/json' -d '{"title": "TypeScript Advanced Exam","description": "Tricky questions about TypeScript."}' http://localhost:5000/exams

# curl -X POST -H 'Content-Type: application/json' -d '{\"title\": \"TypeScript Advanced Exam\",\"description\": \"Tricky questions about TypeScript.\"}' http://localhost:5000/exams

# curl -X POST http://localhost:5000/exams -H 'Content-Type: application/json' -j {"title": "TypeScript Advanced Exam","description": "Tricky questions about TypeScript."}

# curl -v -H "Content-Type: application/json" -X POST -d "{ \"title\": \"TypeScript Advanced Exam\",\"description\": \"Tricky questions about TypeScript\" }" http://localhost:5000/exams

# curl http://localhost:5000