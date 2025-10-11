import json
def load_file(file):
    with open(file, "r") as f:
        data =json.load(f)
    return data
#This function will load the json data
def people_you_may_know(user_id, data):
    user_friend={}
    for user in data['users']:
        user_friend[user['id']]=set(user['friends']) #This line uses, user id as key and stores values with user friends from data_3.json file 
    user_friends=user_friend[user_id]
    #This part of the function cleans data and stores all the people that are friends with the user
    suggestions={} # This is where we will store our potential friends
    for friend in user_friends:
        for friends_friend in user_friend[friend]:
            if friends_friend!=user_id and friends_friend not in user_friends:# This line checks if the friend we are suggesting is not the user itself and if the friend is already friends with the user
                if friends_friend not in suggestions:
                    suggestions[friends_friend]=0 #This line is executed only if a friends_friend is encountered for the first time as a potential suggestion 
                    #(meaning they are a friend of one of the current user's friends, are not the current user, and are not already a friend of the current user)
                suggestions[friends_friend]+=1
    sorted_suggestions=sorted(suggestions.items(), key=lambda x: x[0])
    return [user for user, count in sorted_suggestions]
#Load data
data=load_file("data_3.json")
user_id=input("Enter user id to get suggestions: ")
user_id=int(user_id)
#Get suggestions
suggestions=people_you_may_know(user_id, data)
print(f"People You May know:\n")
for suggestion in suggestions:
    print(f"The user with id {suggestion} and name {data['users'][suggestion-1]['name']} is suggested to you.")
#This function will suggest people you may know based on mutual friends