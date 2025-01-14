from random import randint

db = {
  "posts": [
    {
      "id": "1",
      "title": "HTMX is awesome!",
      "content": "I just learned about HTMX and it's awesome!",
    },
    {
      "id": "2",
      "title": "This post is generated by ChatGPT",
      "content": "I'm a robot. I'm writing this post using ChatGPT.",
    },
    {
      "id": "3",
      "title": "I'm tired...",
      "content": "It's 3am and I want to sleep.",
    }, 
    {
      "id": "4",
      "title": "Hello world!",
      "content": "It's 3pm and I want to sleep.",
    }
  ]
}

def get_posts():
	global db
	return db['posts']

def get_post(post_id):
    global db
    for post in db['posts']:
        if post['id'] == post_id:
            return post
    return None

def update_post(post_id, title, content):
  global db
  for post in db['posts']:
    if post['id'] == post_id:
      post['title'] = title
      post['content'] = content
      return post
  return None

def add_post(title, content):
	global db
	post = {
		'id': str(randint(1000, 9999)),
		'title': title,
		'content': content,
	}
	db['posts'].insert(0, post)
	return post

def set_post(id, title, content):
	global db
	for post in db['posts']:
		if post['id'] == id:
			post['title'] = title
			post['content'] = content
			return post
	return None

def delete_post(id):
	global db
	db['posts'] = [ post for post in db['posts'] if post['id'] != id ]