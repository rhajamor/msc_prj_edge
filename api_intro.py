#lire https://realpython.com/api-integration-in-python/#rest-and-python-tools-of-the-trade

import requests
def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post)
            #print(f"Post {post['id']}: {post['title']}")
    else:
        print(f"Error fetching data. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_posts()
