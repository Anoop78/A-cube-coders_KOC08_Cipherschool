import random
print("Hello Reader! This is your story generator.")
readername = input("Enter your name here:")
print('Hello ' + readername)

names = ['Anoop','Abhishek ','David','Amit','Roy']
places = ['Mumbai','Delhi','Jalandhar','Shimla','Varanasi','Nagpur','Kanpur','Jaipur']
quests = ['arrive to a grand building and take photograph ','eat pizza at the most lavish restaurant ','buy 20 expensive things in the most extrivagant shop they see along the street','Go to the most visiting place ']
friends = ['Arjun','Albert','Rajkumar','Aryan','Karthik','Prince']
roles = ['young man','smart boy','college student ','student',' boy','secondary student']

weather = ['a suuny day','a hot day','a cold night','a very  humid and hot day','a cloudy day','a rainy day']
trip = ['Taj mahal','Manali','Shimla','Dalhousie','Golden temple','Rishikesh']
cars = ['car']

randomname = random.choice(names)
randomplace =  random.choice(places)
randomquests = random.choice(quests)
randomroles = random.choice(roles)
randomweather = random.choice(weather)
randomfriends = random.choice(friends)

randomtrip = random.choice(trip)
randomcars = random.choice(cars)

story = 'Once upon a time a ' + randomroles + ' called ' + randomname + ' lived in a beautiful area called ' + randomplace + ' . It was ' + randomweather + ' and at this place ' + randomname + ' will have to ' + randomquests + ' after, that they meet with ' + randomfriends + ' and had a long  conversation . After  they decided to have a trip to ' + randomtrip + ' by the  ' + randomcars + ' .They enjoy and have a lot fun during the  whole trip.  ' 


print(story)