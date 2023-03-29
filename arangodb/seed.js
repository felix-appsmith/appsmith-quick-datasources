if (db._createDatabase("develop")) {
  console.log("Database 'develop' created.");
  db._useDatabase("develop")
}

// Crea la colección "users"
if (db._createDocumentCollection("users")) {
  console.log("Collection user created.")
}else{
  console.log("error collection")
}



// Itera 1000 veces para agregar documentos a la colección
for (let i = 1; i <= 1000; i++) {
// Crea un documento con los valores aleatorios
let user = {
  "username": "user" + i,
  "email": "user" + i + "@example.com",
  "age": Math.floor(Math.random() * 50) + 20,
  "bio": "I am a " + (Math.random() < 0.5 ? "software developer" : "teacher") +
         " from " + (Math.random() < 0.5 ? "New York" : "Los Angeles"),
  "avatar": null,
  "is_active": Math.random() < 0.5,
  "created_at": new Date(),
  "data": { "key1": "value1", "key2": "value2" },
  "salary": (Math.random() * 50000 + 5000).toFixed(2)
};

// Agrega el documento a la colección "users"
db.users.save(user);
}
