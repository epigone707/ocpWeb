# ocpWeb
A web UI of our ocp ML model

## Installation
Create and activate a virtual environment:
```
$ python3 -m venv env
$ source env/bin/activate
```

Install required packages to the viertual enviroment:
```
$ pip install flask flask-cors jinja2
$ pip install ase
```


Run the flask app to start the server. 
```
(env)$ python server/app.py
```
To test the back end, point your browser at http://localhost:5000/ping. You should see: "pong!".

If you want to kill the server, press Ctrl+C.

Then, open a new terminal and fire up the development server:
```
$ cd client
$ npm run serve
```
To test, navigate to http://localhost:8080 in the browser. You should see the home page.



## deploy to AWS

```
server {
  listen 80;
  server_name ec2-3-84-249-197.compute-1.amazonaws.com;
  location / {
    proxy_pass http://localhost:8080;
  }
  location /api/ {
    proxy_pass http://localhost:5000/api/;
  }
  location /uplouds/ {
    proxy_pass http://localhost:5000/uploads/;
  }
}

```
## Reference
- https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/#flask-setup
