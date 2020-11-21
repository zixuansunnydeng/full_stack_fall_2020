from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

class BlogPost:
    def __init__(self, id, title, subtitle, author, date_posted, content):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.date_posted = date_posted
        self.content = content

blog_posts = [BlogPost(id=0, title="How to use", subtitle="Read me", 
    author="Sheldon", date_posted=datetime.now(), content="Click 'Add' button at the top right corner to add new blog post.")]

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = blog_posts[post_id]
    return render_template('post.html', post=post)


@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = BlogPost(id=len(blog_posts), title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())
    blog_posts.append(post)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)