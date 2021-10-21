# which data structures are best suited to corpus of information
# write code using icebreakers 

joseph = {'name': 'Joseph Foley', 'Fav Tacos': ['Tacos Gomez', 'Çafe Andrade'], 'Fav Drink': 'Sanpellegrino Limonata'}
cherrie = {'name': 'Cherrie Kwok', 'Fav Tacos': 'Awaiting response', 'Fav Drink': 'unknown'}
tarushi = {'name': 'Tarushi Sonthalia', 'Fav Tacos': 'Brazos Tacos', 'Fav Drink': 'Cuba Libre'} 
jennifer = {'name': 'Jennifer Marine', 'Fav Tacos': ['Tacos Gomez', 'Barbies Burrito Barn'], 'Fav Drink': 'G&T'}
jacqui = {'name': 'Jacqui Sahagian', 'Fav Tacos': 'Cactus for Pupusas', 'Fav Drink': 'Greyfrut'}
susan = {'name': 'Susan Abraham', 'Fav Tacos': 'Taco Nako', 'Fav Drink': 'WF Ginger Seltzer'}

praxis_fellows = {"Dynamic Aries":cherrie, "Warm-hearted Taurus":jacqui, "Patient Taurus":jennifer, "Generous Leo":joseph, "Meticulous Virgo":tarushi, "Loyal Aquarius":susan}


for key, value in praxis_fellows.items():
    print(key)
    print('Value', value)