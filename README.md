# REST API (Flask + MongoDB)

## Server: Python Flask
** _server.py_

## DB: MongoDB
** Collection's document format:
```
{
  name: <String>
  age: <Int32>
  email: <String>
}
```

*** REST requests (GET, POST, PUT, DELETE) can be sent via terminal using `curl` command.

For example:

GET (all users):  
`curl http://<server>:5000/users`

GET (one user):
`curl http://<server>:5000/users/<user_id>`

DELETE:  
`curl -X DELETE http://<server>:5000/users/<user_id>`

POST (note: `application/json` format recommended):
`curl -d '{"name": "<name>", "age": <age>, "email": "<email>"}' -H 'Content-Type: application/json' -X POST http://<server>:5000/users`

PUT:
`curl -d '{"name": "<name>", "age": <age>, "email": "<email>"}' -H 'Content-Type: application/json' -X PUT http://<server>:5000/users/<user_id>`
