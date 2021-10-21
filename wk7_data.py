# which data structures are best suited to corpus of information
# write code using icebreakers 

import json

joseph = {'name': 'Joseph Foley', 'Fav Tacos': ['Tacos Gomez', 'Çafe Andrade'], 'Fav Drink': 'Sanpellegrino Limonata'}
cherrie = {'name': 'Cherrie Kwok', 'Fav Tacos': 'Awaiting response', 'Fav Drink': 'unknown'}
tarushi = {'name': 'Tarushi Sonthalia', 'Fav Tacos': 'Brazos Tacos', 'Fav Drink': 'Cuba Libre'} 
jennifer = {'name': 'Jennifer Marine', 'Fav Tacos': ['Tacos Gomez', 'Barbies Burrito Barn'], 'Fav Drink': 'G&T'}
jacqui = {'name': 'Jacqui Sahagian', 'Fav Tacos': 'Cactus for Pupusas', 'Fav Drink': 'Greyfrut'}
susan = {'name': 'Susan Abraham', 'Fav Tacos': 'Taco Nako', 'Fav Drink': 'WF Ginger Seltzer'}

cohort = [joseph, cherrie, susan, tarushi, jacqui, jennifer]

# open a file called cohort.json, and write into it

#          finder                     variable we're going in python
with open('cohort.json', mode="w") as jsonfile:
    # in that file we've made, dump the cohort list as JSON.
    jsonfile.write(json.dumps(cohort))

with open('cohort.json', mode="r") as the_file_we_loaded:
    the_data_we_pulled_from_it = json.loads(the_file_we_loaded.read())

for person in the_data_we_pulled_from_it:
    print(person["name"],"likes",person["Fav Tacos"])

# praxis_fellows = {"Dynamic Aries":cherrie, "Warm-hearted Taurus":jacqui, "Patient Taurus":jennifer, "Generous Leo":joseph, "Meticulous Virgo":tarushi, "Loyal Aquarius":susan}


# for key, value in praxis_fellows.items():
#     print(key)
#     print('Value', value)