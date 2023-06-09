db.createUser({
  user: "myuser",
  pwd: "mypassword",
  roles: [{ role: "readWrite", db: "mydatabase" }]
});

db.myCollection.insertOne({ name: "John Doe", age: 30 });
