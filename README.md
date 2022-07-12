# ocpWeb
A web UI of our ocp ML model

## Installation
Create and activate a virtual environment
```
$ python3 -m venv env
$ source env/bin/activate
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
## Reference
- https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/#flask-setup
