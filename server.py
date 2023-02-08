from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_all_posts():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return all_posts


@app.route('/')
def home():
    all_posts = get_all_posts()
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:blog_id>")
def get_post(blog_id):
    all_posts = get_all_posts()
    for post in all_posts:
        if post["id"] == blog_id:
            post_title = post["title"]
            post_body = post["body"]
            return render_template("post.html", title=post_title, body=post_body)


if __name__ == "__main__":
    app.run(debug=True)
