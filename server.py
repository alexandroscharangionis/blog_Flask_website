from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

# Get all posts from endpoint, turn them into objects and add them to list:
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


# Render template with post objects inserted as argument
# to loop through them inside html file with Jinja templating:
@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


# Route gets blog id from post.html
# and inserts it into function as argument
# to identify and render post based on id:
@app.route("/post/<int:blog_id>")
def get_post(blog_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == blog_id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
