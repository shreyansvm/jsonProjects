import requests , json

# CLIENT_ID = "MY_CLIENT_ID"
# CLIENT_SECRET = "MY_CLIENT_SECRET"
# MEDIUM = "https://medium.com"

def clean_json_response(response):
    return json.loads(response.text.split('])}while(1);</x>')[1])

def latestPostsFromMyFollowingAuthors(usernames):
    # sample output : https://medium.com/@shreyans.mulkutkar/latest?format=json
    print('Retrieving the latest posts...')
    post_ids = []
    for username in usernames:
        url = MEDIUM + '/@' + username + '/latest?format=json'
        print url
        response = requests.get(url)
        response_dict = clean_json_response(response)
        print response_dict
        try:
            posts = response_dict['payload']['references']['Post']
        except:
            posts = []
        if posts:
            print posts
            for key in posts.keys():
                post_ids.append(posts[key]['id'])
    return post_ids

print latestPostsFromMyFollowingAuthors(["shreyans.mulkutkar"])