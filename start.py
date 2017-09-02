import time
import random

def main_menu():
    print("Welcome to reincarnation! What would you like to do?")
    main_menu_input = input("")
    if main_menu_input == 'begin':
        filler_code = True
        #The code continues
    elif main_menu_input == 'options':
        time.sleep(1)
        print('begin - start the game')
        print('no other options')
        time.sleep(1)
        main_menu()
    else:
        time.sleep(1)
        print('type \"options\" for options')
        time.sleep(1)
        main_menu()

main_menu()

    #world_generation()
    #character_generation()
    #first_inputs()

#-World Generation-

#Naming

capital_consonants = ['B','C','D','F','G','H','J','K','L','M','N','P','R','S','T','V','W','Y','Z']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','x','y','z']
vowels = ['a','e','i','o','u']

def three_letter_name():
    letter1 = random.choice(capital_consonants)
    letter2 = random.choice(vowels)
    letter3 = random.choice(consonants)
    return

def five_letter_name():
    first_letter = random.choice(capital_consonants)
    second_letter = random.choice(vowels)
    third_letter = random.choice(consonants)
    fourth_letter = random.choice(vowels)
    fifth_letter = random.choice(consonants)
    return first_letter + second_letter + third_letter + fourth_letter + fifth_letter
country_name = five_letter_name()

def seven_letter_name():
    first_letter = random.choice(capital_consonants)
    second_letter = random.choice(vowels)
    third_letter = random.choice(consonants)
    fourth_letter = random.choice(vowels)
    fifth_letter = random.choice(consonants)
    sixth_letter = random.choice(vowels)
    seventh_letter = random.choice(consonants)
    return first_letter + second_letter + third_letter + fourth_letter + fifth_letter + sixth_letter + seventh_letter
capital_name = seven_letter_name()

print('You were born in the country of', country_name + ", whose capital is", capital_name)

#Location Placement and NPC population

city_count = random.randint(2,3)
village_count = random.randint(7,10)
dungeon_count = 2
cave_count = random.randint(3,5)

def location_maker():
    return [random.randint(0,1000),random.randint(0,1000)]

capital = {'name': capital_name, 'location': location_maker(), 'blacksmiths': {'count': random.randint(3,5)}, 'chefs': {'count': random.randint(3,5)}, 'civilians': {'count': random.randint(100,150)}}
dungeon1 = {'location': location_maker(), 'floorcount': random.randint(20,30)}
dungeon2 = {'location': location_maker(), 'floorcount': random.randint(20,30)}
world_dragon = {'location': location_maker()}
giant_plant = {'location': location_maker()}
yggdrasil = {'location': location_maker()}

cities = {}
for x in range(city_count):
    cities['city'+str(x)] = {'name': five_letter_name(), 'location': [location_maker()], 'blacksmiths': {'count': random.randint(2,3)}, 'chefs': {'count': random.randint(2,3)}, 'civilians': {'count': random.randint(40,60)}}

villages = {}
for x in range(village_count):
    villages['village'+str(x)] = {'name': five_letter_name(), 'location': [location_maker()], 'blacksmiths': {'count': random.randint(1,2)}, 'chefs': {'count': random.randint(1,2)}, 'civilians': {'count':random.randint(15,20)}}

caves = {}
for x in range(cave_count):
    caves['cave'+str(x)] = {'location': [location_maker()], 'level': random.randint(1,100)}

#-Character Generation-

#Social class

social_class_number = random.randint(1,100)

last_name_list = ['Lacerda', 'Nasca', 'Monzac', 'Akiba', 'Wentworth', 'Alix', 'Howells', 'Priest', 'Chang', 'Field-daly', 'Budrene', 'Dininny', 'Kirscht', 'Taborsky', 'Fung', 'Oliva', 'Deland', 'Barcus', 'Vanheeckeren',
'Dorfman', 'Genetti', 'Birnbaum', 'Schutjer', 'Shiro', 'Karplus', 'Belisle', 'Branscomb', 'Badot', 'Boothby', 'Kyle', 'Condon', 'Lacy', 'Petrarch', 'Botfield', 'Shynk', 'Lefkopoulou', 'Vidakovic', 'Housum', 'Munter',
'Bruzzone', 'Bender', 'Nordstroem', 'Miletus', 'Foladare', 'Pabrezis', 'Hoermann', 'Boehrer', 'Pantilla', 'Phelps', 'Lucretius', 'Byerly', 'Todorovic', 'Brugnara', 'Sutter', 'Fuentes', 'Borsellino', 'Scapini', 'Van allen',
'Fitchett', 'Luca', 'Wessling-resnick', 'Bremner', 'Leyman', 'Pilbeam', 'Ferrera', 'Holzgrefe', 'Stevenson', 'Robertson', 'Rowan', 'Urdang', 'Burley', 'Signer', 'Sollors', 'Slive', 'Tolman', 'Keiding', 'Muller', 'Berdiaeff',
'Brunet', 'Pories', 'Puche', 'Montessori', 'Southern', 'Reece', 'Gaskill', 'Knuttunen', 'Whately', 'Mackie', 'Comtois', 'Luebke', 'Nicholas', 'Figueredo', 'Arber', 'Renick', 'Mcclean', 'Mcgahan']
last_name_list_temp = last_name_list

if social_class_number <= 25:
    social_class = 'orphan'
    birthplace = random.choice(['openland', 'village', 'city', 'capital'])
    last_name = ''
elif social_class_number <= 60:
    social_class = 'peasant'
    birthplace = random.choice(['openland', 'village'])
    last_name = ''
elif social_class_number <= 80:
    social_class = 'merchant'
    birthplace = random.choice(['village', 'city', 'capital', 'travelling'])
    last_name = random.choice(last_name_list)
    last_name_list_temp.remove(last_name)
elif social_class_number <= 95:
    social_class = 'noble'
    birthplace = random.choice(['city', 'capital'])
    last_name = random.choice(last_name_list)
    last_name_list_temp.remove(last_name)
else:
    social_class = 'royalty'
    birthplace = 'capital'
    last_name = random.choice(last_name_list)
    last_name_list_temp.remove(last_name)

age = 5
age_string = str(age) + ' year old'
print('What is your name?')
first_name = input('')
time.sleep(1)
print()

titles = [social_class, age_string]

warm_touch = {'mana cost': 20, 'damage': 20, 'scaling': 0.6, 'effect': False}
ember_toss = {'mana cost': 15, 'damage': 15, 'scaling': 0.8, 'effect': False}
fireball = {'mana cost': 25, 'damage': 30, 'scaling': 1, 'effect': False}
firefist = {'mana cost': 20, 'damage': 25, 'scaling': 1.2, 'effect': False}
firebolt = {'mana cost': 30, 'damage': 50, 'scaling': 1, 'effect': False}
flame_wall = {'mana cost': 50, 'damage': 50, 'scaling': 1.5, 'effect': False}
flame_whip = {'mana cost': 20, 'damage': 25, 'scaling': 1.8, 'effect': False}
inferno = {'mana cost': 25, 'damage': False, 'scaling': 1.5, 'effect': 'does random damage, 0-100'}
fire_dual_cast = {'mana cost': 30, 'damage': False, 'scaling': -0.25, 'effect': 'cast two fire type magic spells in one turn'}
fire_blast = {'mana cost': 100, 'damage': 120, 'scaling': 2, 'effect': False}
blue_fire = {'mana cost': 0, 'damage': 70, 'scaling': 1, 'effect': False}
heatmosphere = {'mana cost': 80, 'damage': False, 'scaling': 1, 'effect': 'deal 100 damage per turn'}
blitz = {'mana cost': 150, 'damage': 250, 'scaling': 2, 'effect': False}
hellfire = {'mana cost': 0, 'damage': 100, 'scaling': 1.5, 'effect': False}
fire_gods_wrath = {'mana cost': False, 'damage': False, 'scaling': False, 'effect': 'deal double mana cost'}
unlearned_fire_magic = [warm_touch, ember_toss, fireball, firefist, firebolt, flame_wall, flame_whip, inferno, fire_dual_cast, fire_blast, blue_fire, heatmosphere, blitz, hellfire, fire_gods_wrath]
learned_fire_magic = []

make_water = {'mana cost': 50, 'damage': False, 'scaling': -0.25, 'effect': "creates water"}
humidify = {'mana cost': 25, 'damage': 30, 'scaling': 1, 'effect': False}
slip = {'mana cost': 25, 'damage': 35, 'scaling': 1, 'effect': False}
wetten = {'mana cost': 50, 'damage': False, 'scaling': -0.25, 'effect': 'slip does 2x damage'}
waterbolt = {'mana cost': 30, 'damage': 50, 'scaling': 1, 'effect': False}
overhydrate = {'mana cost': 50, 'damage': 50, 'scaling': 1.5, 'effect': False}
water_whip = {'mana cost': 20, 'damage': 25, 'scaling': 1.4, 'effect': False}
wave = {'mana cost': 10, 'damage': 40, 'scaling': 1.5, 'effect': False}
water_dual_cast = {'mana cost': 30, 'damage': False, 'scaling': -0.25, 'effect': 'cast two water type magic spells in one turn'}
bubble_burst = {'mana cost': 100, 'damage': 150, 'scaling': 1.5, 'effect': False}
water_suspension = {'mana cost': 10, 'damage': 70, 'scaling': 1.2, 'effect': False}
flood = {'mana cost': 60, 'damage': False, 'scaling': 1, 'effect': 'deal 80 damage per turn'}
waterfall = {'mana cost': 150, 'damage': 250, 'scaling': 2, 'effect': False}
water_gods_serenity = {'mana cost': 0, 'damage': 0, 'scaling': 5, 'effect': False}
unlearned_water_magic = [make_water, humidify, slip, wetten, waterbolt, overhydrate, water_whip, wave, water_dual_cast, bubble_burst, water_suspension, flood, waterfall, water_gods_serenity]
learned_water_magic = []

rock_throw = {'mana cost': 20, 'damage': 20, 'scaling': 0.8, 'effect': False}
pebble_bullet = {'mana cost': 15, 'damage': 30, 'scaling': 0.5, 'effect': False}
fortify = {'mana cost': 50, 'damage': False, 'scaling': 0.1, 'effect': 'armor + 10'}
rockbolt = {'mana cost': 30, 'damage': 50, 'scaling': 1.5, 'effect': False}
hill_trap = {'mana cost': 50, 'damage': 50, 'scaling': 1.5, 'effect': False}
boulder = {'mana cost': 20, 'damage': 25, 'scaling': 1.4, 'effect': False}
fissure = {'mana cost': 50, 'damage': random.randint(0,150), 'scaling': 1.5, 'effect': False}
earth_dual_cast = {'mana cost': 30, 'damage': False, 'scaling': -0.25, 'effect': 'cast two earth type magic spells in one turn'}
ground_pound = {'mana cost': 100, 'damage': 100, 'scaling': 2.5, 'effect': False}
bump_launch = {'mana cost': 10, 'damage': 70, 'scaling': 1.2, 'effect': False}
rough_terrain = {}
towerfall = {}
collapse = {}
earth_gods_solitude = {}
unlearned_earth_magic = [rock_throw, pebble_bullet, fortify, rockbolt, hill_trap, boulder, fissure, earth_dual_cast, ground_pound, bump_launch, rough_terrain, towerfall, collapse, earth_gods_solitude]
learned_earth_magic = []

unlearned_air_magic = []
learned_air_magic = []

unlearned_swordskills = []
learned_swordskills = []

unlearned_martialarts = []
learned_martialarts = []

unlearned_smithing = []
learned_smithing = []

unlearned_cooking = []
learned_cooking = []

unlearned_farming = []
learned_farming = []

a = "test"