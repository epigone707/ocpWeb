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

ssh to your aws ec2 instance, git clone this repo and switch to branch aws.

Open `/etc/nginx/sites-available/default` to edit the file.
```
$ sudo nano /etc/nginx/sites-available/default
```
Modify `/etc/nginx/sites-available/default`. Replace the entire default server settings with the settings specified below. Replace the server address with your ec2 ipv4 address, for example, mine is `ec2-3-84-249-197.compute-1.amazonaws.com`. Save and exit.
```
server {
  listen 80;
  server_name <Your EC2 IPV4 ADDRESS>;
  location / {
    proxy_pass http://localhost:8080;
  }
  location /api/ {
    proxy_pass http://localhost:5000/api/;
  }
  location /uploads/ {
    proxy_pass http://localhost:5000/uploads/;
  }
}

```

Restart the nginx server.
```
$ sudo systemctl restart nginx
```
## Reference
- https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/#flask-setup
