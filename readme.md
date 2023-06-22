from project_name import app, db
from flaskblog import User, Post
app.app_context().push()
db.create_all()

user_1 = User(username='Halil', email='halil@flask.com', password='halil')
db.session.add(user_1)
user_2 = User(username='Cemal', email='cemal@flask.com', password='cemal')
db.session.add(user_2)
db.session.commit()

User.query.all()
User.query.first()
User.query.filter_by(username='Halil').all()
User.query.get(id)

post_1 = Post(title='Blog 1', content='First Post Content', user_id=user.id)
post_2 = Post(title='Blog 2', content='Second Post Content', user_id=user.id)
db.session.add(post_1)
db.session.add(post_2)
db.session.commit()
user.posts
