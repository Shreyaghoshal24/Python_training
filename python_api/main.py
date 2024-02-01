import requests

# GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print('GET Response:', response.json())

# POST request
new_post = {'title': 'New Post', 'body': 'This is a new post', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
print('POST Response:', response.json())

# PUT request
updated_post = {'title': 'Updated Post', 'body': 'This post has been updated'}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=updated_post)
print('PUT Response:', response.json())

# DELETE request
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print('DELETE Response:', response.status_code)


