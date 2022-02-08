#import necessary modules
from flask import Flask, render_template
import json


# set up flask webserver
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def load_selectors():
    with open("selectors.json", 'r') as f:
        return json.load(f)

body {
    padding: 0px;
    margin: 0px;
}
.navbar {
    position: fixed;
    width: 180px;
    background: rgb(34, 139, 130);
    height: 100%;
    margin: 0px;
}
.nav-item {
    list-style: None;
    margin: 20px 10px;
}
.nav-link {
    text-decoration: None;
    color: white;
    font-size: 1.4rem;
    transition: all 400ms;
}
.nav-link:hover {
    font-size: 1.6rem;
}
h1 {
    width: 100%;
    background: rgb(34, 135, 139);
    color: white;
    margin: 0px;
    padding: 15px 20px;
}
#content {
    margin-left: 220px;
    padding: 30px 20px;
}

.question {
    margin: 50px auto;
    width: 70%;
    border: 5px dashed rgb(34, 114, 139);
    border-radius: 15px;
    padding: 40px 70px;
}

.question h3 {
    font-size: 3rem;
}

.question p {
    margin: 30px 50px;
}

.answer-list {
    margin: 0px;
    padding: 0px;
    width: 100%;
    display: flex;
    flex-direction: row;
}

.answer-item {
    list-style: None;
    margin: 0px auto;
    padding: 0px;
    width: 300px;
    text-align: center;
}

.answer-item a {
    text-decoration: None;
    color: white;
    border: 3px solid forestgreen;
    background: forestgreen;
    border-radius: 5px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60px;
    transition: all 600ms;
}

.answer-item a:hover {
    background: darkgreen;
    font-size: 2rem;
}body {
    padding: 0px;
    margin: 0px;
}
.navbar {
    position: fixed;
    width: 180px;
    background: rgb(34, 139, 130);
    height: 100%;
    margin: 0px;
}
.nav-item {
    list-style: None;
    margin: 20px 10px;
}
.nav-link {
    text-decoration: None;
    color: white;
    font-size: 1.4rem;
    transition: all 400ms;
}
.nav-link:hover {
    font-size: 1.6rem;
}
h1 {
    width: 100%;
    background: rgb(34, 135, 139);
    color: white;
    margin: 0px;
    padding: 15px 20px;
}
#content {
    margin-left: 220px;
    padding: 30px 20px;
}

.question {
    margin: 50px auto;
    width: 70%;
    border: 5px dashed rgb(34, 114, 139);
    border-radius: 15px;
    padding: 40px 70px;
}

.question h3 {
    font-size: 3rem;
}

.question p {
    margin: 30px 50px;
}

.answer-list {
    margin: 0px;
    padding: 0px;
    width: 100%;
    display: flex;
    flex-direction: row;
}

.answer-item {
    list-style: None;
    margin: 0px auto;
    padding: 0px;
    width: 300px;
    text-align: center;
}

.answer-item a {
    text-decoration: None;
    color: white;
    border: 3px solid forestgreen;
    background: forestgreen;
    border-radius: 5px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60px;
    transition: all 600ms;
}

.answer-item a:hover {
    background: darkgreen;
    font-size: 2rem;
}body {
    padding: 0px;
    margin: 0px;
}
.navbar {
    position: fixed;
    width: 180px;
    background: rgb(34, 139, 130);
    height: 100%;
    margin: 0px;
}
.nav-item {
    list-style: None;
    margin: 20px 10px;
}
.nav-link {
    text-decoration: None;
    color: white;
    font-size: 1.4rem;
    transition: all 400ms;
}
.nav-link:hover {
    font-size: 1.6rem;
}
h1 {
    width: 100%;
    background: rgb(34, 135, 139);
    color: white;
    margin: 0px;
    padding: 15px 20px;
}
#content {
    margin-left: 220px;
    padding: 30px 20px;
}

.question {
    margin: 50px auto;
    width: 70%;
    border: 5px dashed rgb(34, 114, 139);
    border-radius: 15px;
    padding: 40px 70px;
}

.question h3 {
    font-size: 3rem;
}

.question p {
    margin: 30px 50px;
}

.answer-list {
    margin: 0px;
    padding: 0px;
    width: 100%;
    display: flex;
    flex-direction: row;
}

.answer-item {
    list-style: None;
    margin: 0px auto;
    padding: 0px;
    width: 300px;
    text-align: center;
}

.answer-item a {
    text-decoration: None;
    color: white;
    border: 3px solid forestgreen;
    background: forestgreen;
    border-radius: 5px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60px;
    transition: all 600ms;
}

.answer-item a:hover {
    background: darkgreen;
    font-size: 2rem;
}body {
    padding: 0px;
    margin: 0px;
}
.navbar {
    position: fixed;
    width: 180px;
    background: rgb(34, 139, 130);
    height: 100%;
    margin: 0px;
}
.nav-item {
    list-style: None;
    margin: 20px 10px;
}
.nav-link {
    text-decoration: None;
    color: white;
    font-size: 1.4rem;
    transition: all 400ms;
}
.nav-link:hover {
    font-size: 1.6rem;
}
h1 {
    width: 100%;
    background: rgb(34, 135, 139);
    color: white;
    margin: 0px;
    padding: 15px 20px;
}
#content {
    margin-left: 220px;
    padding: 30px 20px;
}

.question {
    margin: 50px auto;
    width: 70%;
    border: 5px dashed rgb(34, 114, 139);
    border-radius: 15px;
    padding: 40px 70px;
}

.question h3 {
    font-size: 3rem;
}

.question p {
    margin: 30px 50px;
}

.answer-list {
    margin: 0px;
    padding: 0px;
    width: 100%;
    display: flex;
    flex-direction: row;
}

.answer-item {
    list-style: None;
    margin: 0px auto;
    padding: 0px;
    width: 300px;
    text-align: center;
}

.answer-item a {
    text-decoration: None;
    color: white;
    border: 3px solid forestgreen;
    background: forestgreen;
    border-radius: 5px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60px;
    transition: all 600ms;
}

.answer-item a:hover {
    background: darkgreen;
    font-size: 2rem;
}body {
    padding: 0px;
    margin: 0px;
}
.navbar {
    position: fixed;
    width: 180px;
    background: rgb(34, 139, 130);
    height: 100%;
    margin: 0px;
}
.nav-item {
    list-style: None;
    margin: 20px 10px;
}
.nav-link {
    text-decoration: None;
    color: white;
    font-size: 1.4rem;
    transition: all 400ms;
}
.nav-link:hover {
    font-size: 1.6rem;
}
h1 {
    width: 100%;
    background: rgb(34, 135, 139);
    color: white;
    margin: 0px;
    padding: 15px 20px;
}
#content {
    margin-left: 220px;
    padding: 30px 20px;
}

.question {
    margin: 50px auto;
    width: 70%;
    border: 5px dashed rgb(34, 114, 139);
    border-radius: 15px;
    padding: 40px 70px;
}

.question h3 {
    font-size: 3rem;
}

.question p {
    margin: 30px 50px;
}

.answer-list {
    margin: 0px;
    padding: 0px;
    width: 100%;
    display: flex;
    flex-direction: row;
}

.answer-item {
    list-style: None;
    margin: 0px auto;
    padding: 0px;
    width: 300px;
    text-align: center;
}

.answer-item a {
    text-decoration: None;
    color: white;
    border: 3px solid forestgreen;
    background: forestgreen;
    border-radius: 5px;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 60px;
    transition: all 600ms;
}

.answer-item a:hover {
    background: darkgreen;
    font-size: 2rem;
}
# webscraping function
def my_scraper():
    # YOUR CODE GOES HERE
    pass


# filter function
def my_filter():
    # YOUR CODE GOES HERE
    pass

# output to json
def write_json():
    # YOUR CODE GOES HERE
    pass


# define route(s)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/css-selectors")
def css_selectors():
    return render_template("css-selectors.html", selectors=load_selectors())


# starts the webserver
if __name__ == "__main__":
    app.run()
