# which data structures are best suited to corpus of information
# write code using icebreakers 

ice_break = [ {'name': 'Joseph Foley', 'Best Tacos': ['Tacos Gomez', 'Çafe Andrade'], 'Fav Drink': 'Sanpellegrino Limonata'}, 
              {'name': 'Cherrie Kwok', 'Best Tacos': 'Awaiting response', 'Fav Drink': 'unknown'},
              {'name': 'Tarushi Sonthalia', 'Best Tacos': 'Brazos Tacos', 'Fav Drink': 'Cuba Libre'},
              {'name': 'Jennifer Marine', 'Best Tacos': ['Tacos Gomez', 'Barbies Burrito Barn'], 'Fav Drink': 'G&T'},
              {'name': 'Jacqui Sahagian', 'Best Tacos': 'Cactus for Pupusas', 'Fav Drink': 'Greyfrut'},
              {'name': 'Susan Abraham', 'Best Tacos': 'Taco Nako', 'Fav Drink': 'WF Ginger Seltzer'}]

fellows = [joseph,cherrie,tarushi,jennifer,jacqui,susan]

for fellow in fellows: 
    print(fellow["name"])

    exit()
zodiac = {"Dynamic Aries":cherrie, "Warm-hearted Taurus":jacqui, "Patient Taurus":jennifer, "Generous Leo":joseph, "Meticulous Virgo":tarushi, "Loyal Aquarius":susan}

print(zodiac["Patient Taurus"])

#good if you want to use this information in a way that is associasted w/ Zodiac epithet; could also place as key in their dictionary 

for key, value in praxis_fellows.items():
    print('Key', key)
    print('Value', value)