from my_app import app
from flask import render_template, request, redirect
import requests
from my_app.models import Fact, Post

name = "bobby"
facts = {"Birthday": "April 10th 2000", "Favorite color": "blue"}
posts = [{"title": "this is my title", "description": "hey bitches"}]

@app.route("/")
def index():
    db_facts = Fact.query.all()
    fact_dict = {fact.name: fact.value for fact in db_facts}

    db_posts = Post.query.all()
    post_list = [{"title": post.title, "description": post.description}]
    return render_template("index.html", name = name, facts=facts, posts=posts)

@app.route("/change name")
def change_name(): 
    global name 
    new_name = request.args.get("name")
    name = new_name
    return redirect("/")

@app.route("/post", methods=["POST"])
def make_post(): 
    global posts
    post_info = request.get_json()
    new_post = Post(title=post_info["title"], description = post_info["description"])
    posts.append({"title": post_info["title"], "description": post_info["description"]})
    return redirect("/")

@app.route("/change_facts", methods=["POST"])
def change_facts():
    if request.method == "POST":
        change_facts = request.get_json()
        for key, value in change_facts.items():
            if Fact.query.filter(Fact.name == key).first() is None:
                new_fact = Fact(name=key, value=value)
                db.session.add(new_fact)
            db.session.commit()
    return redirect("/")


