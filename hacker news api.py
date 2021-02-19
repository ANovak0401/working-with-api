import requests
import json

# make an api call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty' # store the url
r = requests.get(url) # store response
print(f"Status code: {r.status_code}") # print status code to terminal

#explore data structure
response_dict = r.json() # variable for dictionary read with json
readable_file = 'data/readable_hn_data.json' # create file to store data
with open(readable_file, 'w') as f: # open file in write mode
    json.dump(response_dict, f, indent=4) # save response dictionary in json format on local pc

# display the top story
top_story = f"https://hacker-news.firebaseio.com/v0/item/{response_dict[1]}.json?print=pretty"
story_data = requests.get(top_story)
response = story_data.json()
top_story_file = 'data/top_story.json'
with open(top_story_file, 'w',) as f:
    json.dump(response, f, indent=4)

with open(top_story_file) as f:
    print(f.read())