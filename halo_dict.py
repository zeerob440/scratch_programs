# place function above dict.

def spartan_id(who, roster_num):
    print(f"I'm {who['name']} {roster_num}")

#spartan_id(master_chief, "Finish this fight.")



master_chief: dict = {
    'name': 'John',
    'op_id': 117,
    'ai': 'Cortana',
    'ship': 'UNSC Pillar of Autumn',
    'spartan_id': spartan_id
}

master_chief['spartan_id'](master_chief, 'Here I am.')
