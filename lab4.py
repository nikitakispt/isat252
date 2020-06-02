#3.1 Create a dictionary variable
my_dict = {
    'name':'Tom',
    'id': 123
          }
print(my_dict)

#3.2 Change the value
print(my_dict.items())


#3.3 Chgane the value of the ID key
my_dict['id']=321
print(my_dict)

#3.4 Delete the name key in my_dic
del my_dict['name']
print(my_dict)

#3.5 Create a dictionary variable
my_tweet = {
    "tweet_id":1138,
    "coordinates":(-75,40),
    "visited countries":["GR","HK","MY"]
          }
print(my_tweet)

#3.6 Print the number of visited countries
print(len(my_tweet["visited countries"]))

#3.7 Add "CH" into visited countires
(my_tweet["visited countries"].append('CH'))
print(my_tweet)


#3.8 check if "US" is in visited countries
print('US' in my_tweet['visited countries'])

#3.9 change coordinates (-81,45)
my_tweet['coordinates']=(-81,45)
print(my_tweet['coordinates'])