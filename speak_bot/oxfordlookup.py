# import requests
# import json



# app_id= "45490f99"
# app_key = "6faa149a98e2951d6905a8dad62deea5"

# language = "en-gb"
# word = "fruit"
# fields = "pronunciations"
# strictMatch = "false"

# def getDefinations(word):
#     url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch
    
    
#     r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key}) #auth - acces


# print("code {}\n".format(r.status_code))
# print("text \n" + r.text)
# print("json \n" + json.dumps(r.json()))


import requests
import json


# TODO: replace with your own app_id and app_key
app_id= "45490f99"
app_key = "6faa149a98e2951d6905a8dad62deea5"

language = 'en-gb'

fields = 'pronunciations'
strictMatch = 'false'

def getDefinations(word):

    url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

    response = r.json()

    if 'error' in response.keys():
        return False

    output = []
    # print(response['results'][0])
    # senses = response['results'][0]['lexicalEntries'][0]['entries'][0]
    # print(response['results'][0]['lexicalEntries'][0]['entries'][0]['senses'])

    # definition = [] 
    # for sense in senses:
    #     print("++++++++++++++++++++++++")
    #     definition.append(f"{sense['definitions'][0]}")
    
    # output['definitions'] = "\n".join(definitions)
    
    audio = response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile')

    # if response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
    #     output['audio'] = response['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile')

    return audio