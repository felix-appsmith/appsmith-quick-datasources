db.createUser({ user: "appsmith", pwd: "appsmith", roles: [ { role: "readWrite", db: "test" } ] });


db.createCollection('users');

for (let i = 0; i < 1000; i++) {
  db.users.insertOne({
    name: 'User ' + i,
    age: Math.floor(Math.random() * 100),
    email: 'user' + i + '@example.com',
    is_active: Math.random() < 0.5,
    created_at: new Date(),
    address: {
      street: 'Street ' + i,
      city: 'City ' + i,
      country: 'Country ' + i,
    },
    interests: ['Interest 1', 'Interest 2', 'Interest 3'],
  });
}

