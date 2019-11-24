#Importing the csv file of the data of UFO sighting in all 50 states.The user would be presented a tab that has all 50 states and they would select the state they are in after they hit submit an 8 bit version of the omnitirx from the show Ben 10
#would display they percentage of people who have seen aliens out of 100,000 people. The objective of this dictionary is to iterate through the set of information from the csv file that came from sateillitaeinternet.com

Belive = raw_input("Do you belive in aliens type Yes or No: ")
print ("\033[1;32;40m Bright Green  \n")
print Belive
# Introduces the person to the program asking them if they belive in aliens.
if type (Belive)!= "Yes"or "No":
    raise TypeError("Only answer yes or no")
# Raises type error if they type in something other than yes or no.
if Belive == "No":
    print"Ok have a nice day"
# If they replay no give them this statement.
if Belive == "Yes":
    print("\033[1;32;40m Bright Green  \n")
    print "Welcome to the Mother Ship"
# If they reply yes then give them this staetment and have them procead.
State_Livedin = raw_input("Which State do you live in : ")
print State_Livedin
# Whichever state they live in they say I can read on my end and give them the correct numbers for said state.
import csv
# Above I imported the csv of the data for the amount of alien sighting per 100,000 in each state.
with open('Sheet1.csv') as csvfile:
    #This opens the csv of the alien information that I got from the website.
    readCSV = csv.reader(csvfile)
    #This reads the csv into atom and gives me acess to take things from the csv.
    for row in reader:
            if row in reader == State_Livedin:
            # This if statement is here to read the state that the user choose and will match and pull it from the csv.
                print (row['State'], row['Sightings'], row['Rank'])
# This will print the information about the state that the user needs.
Power = raw_input ("With this new information you a great power and a great responsiblity to live your life accordingly .... in a galxay near you.")
print Power

# This will print the last question to the screen as an conclusion to my program.
