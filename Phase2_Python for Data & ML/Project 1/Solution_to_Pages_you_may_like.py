import json
def load_file(file):
    with open(file, "r") as f:
        data =json.load(f)
    return data
#This function will load the json data
def pages_you_might_like(user_id, data):
    # Build a dictionary of user_id -> set of liked pages
    user_page = {user['id']: set(user['liked_pages']) for user in data['users']}
    # Build a dictionary of user_id -> set of friends
    user_friends = {user['id']: set(user['friends']) for user in data['users']}
    user_pages = user_page[user_id]
    friends = user_friends[user_id]
    suggestions = {}
    for friend_id in friends:
        for page in user_page[friend_id]:
            if page not in user_pages:
                if page not in suggestions:
                    suggestions[page] = 0
                suggestions[page] += 1
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[0])
    return [page for page, count in sorted_suggestions]
#Load data
data=load_file("data_3.json")
user_id=input("Enter user id to get suggestions: ")
user_id=int(user_id)
#Get suggestions
suggestions=pages_you_might_like(user_id, data)
print(f"Pages You Might Like for User {user_id}:")
for page_id in suggestions:
    # Find the page name by ID
    page_name = next((page['name'] for page in data['pages'] if page['id'] == page_id), None)
    if page_name:
        print(f"[{page_id}] {page_name}")