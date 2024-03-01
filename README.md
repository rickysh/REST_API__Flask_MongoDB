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

GET:  
`curl http://<server>:5000/users`

DELETE:  
`curl -X DELETE http://<server>/users/<user_id>`
