#Importing the csv file of the data of UFO sighting in all 50 states.The user would be presented a tab that has all 50 states and they would select the state they are in after they hit submit an 8 bit version of the omnitirx from the show Ben 10
#would display they percentage of people who have seen aliens out of 100,000 people. The objective of this dictionary is to iterate through the set of information from the csv file that came from sateillitaeinternet.com
# When you get to the home screen ask them if they belive in aliens if yes then they go to the next page if they pressed yes then it would say select a state.
#print "Do you belive in aliens"
#if yes then proceed to next page if no then exit page
#print "Welcome to the Mother Ship"
S = raw_input("Do you belive in aliens type Yes or No: ")
print S
#Introduces the person to the program
if type (S)!= str:
    raise TypeError("Only answer yes or no")
#Raises type error if they type in something else.
if S is == "No":
return "Ok have a nice day"
# If they replay no give them this statement
if S is == "Yes":
return "Welcome to the Mother Ship"
#if they reply yes then give them this staetment and have them procaed

W = raw_input("Which State do you live in : ")
print W
# Whichever state they live in they say I can read on my end and give them the correct numbers for said state.
import csv
#above I imported the csv of the data for the amount of alien sisghting per 100,000 in each state.
with csv open('Sheet1.csv') as csvfile:
    #
    readCSV = csv.reader(csvfile)
    for row in reader:
        print (row['State'], row['Sightings'], row['Rank'])

Q = raw_input ("With this new information you a great power and a great responsiblity to live your life accordingly .... in a galxay near you.")
print Q
# I'm not to sure if I would do  a dictionary to easily iterate through the code to return the amount of people that have had an alien incounter.
