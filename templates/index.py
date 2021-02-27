{% extends 'base.html' %} {% block content %}
<h1>{% block title %} Welcome to FlaskBlog {% endblock %}</h1>
{% for post in posts %}
<a href="{{ url_for('post', post_id=post['id']) }}">
    <h2>{{ post['title'] }}</h2>
</a>
<span class="badge badge-primary">{{ post['created'] }}</span>

<a href="{{ url_for('edit', id=post['id']) }}">
    <span class="badge badge-warning">Edit</span>
</a>

<hr> {% endfor %} {% endblock %}

def __init__(self, web_dir, title, reflesh=0):
    