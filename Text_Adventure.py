# Area Descriptions  x_z_y format  n denotes negative
# This are displayed when an area is entered by being printed to the console
des0_0_0 = """Path
    It is a cool and sunny day in autumn.
    The breeze is gentle, but fiere in the same way, the clouds scarce.
    You find yourself in a small Village.
    The village is surrounded by grassland,
    leading to a castle in ruins, far off in the distance.
    You are on a path in the center of the village.
    The path extends to your West, and to your East.
    To your north is a small, run-down tavern.
    To your south is a general store. """
des0_0_1 = """Tavern
    As you enter, the conversation stops,
    and the few customers turn to stare at you.
    After a few seconds, they resume conversation,
    albeit more quiet, and muffled.
    Along the west edge of the room is a door.
    To your south is the exit you came in.
    To the North and East, there are no exits,
    just the brick walls of the tavern. """
des1_0_0 = """Path Junction
    This is the junction of two ancient dirt paths.
    They led north/south and east/west.
    The east path leads into the grassland, to the castle beyond.
    The west path leads back to the town.
    The north and south paths led along the edge of the grassland,
    through cleared farmland beyond. """
des0_0_1n = """General Store
    You find yourself in an old general store.
    Oil lanterns are burning,
    and the smell of cedar rises from the creaky floorboards.
    To the North is the door you came in."""
des1n_0_0 = """Path
    To your north is the wall of the tavern.
    To your south is a post office.
    To your east and west, the path continues """


# Move Mechanics [x, z, y]
# These define the directions into an [x, z, y] system
# Movement definitions
northmove = [0, 0, 1]
eastmove = [1, 0, 0]
southmove = [0, 0, -1]
westmove = [-1, 0, 0]
upmove = [0, 1, 0]
downmove = [0, -1, 0]
location = [0, 0, 0]

# function for changing current location
# Reads user input to change coordiats according to Move Mechanics
def move(direction, location):
    print(direction)
    if direction == "N" or direction == "n" or direction == "north" or direction == "North":
        location = [x + y for x, y in zip(location, northmove)]
    elif direction == "E" or direction == "e" or direction == "east" or direction == "East":
        location = [x + y for x, y in zip(location, eastmove)]
    elif direction == "S" or direction == "s" or direction == "south" or direction == "South":
        location = [x + y for x, y in zip(location, southmove)]
    elif direction == "W" or direction == "w" or direction == "west" or direction == "West":
        location = [x + y for x, y in zip(location, westmove)]
    elif direction == "U" or direction == "u" or direction == "up" or direction == "Up":
        location = [x + y for x, y in zip(location, upmove)]
    elif direction == "D" or direction == "d" or direction == "down" or direction == "Down":
        location = [x + y for x, y in zip(location, downmove)]
    else:
        print("I don't know the direction: " + direction + """.
        Try using a cardinal direction such as N,
        or using a direction word, such as west""")
    print(location)
    return location


# Location Description defining
# This part is very unpolished, and need complete renovation
# Infinite loop which asks for user input, 
# changes coordinate to new location,
# and prints description for that area
# except is for areas without a description
# Line 81 is completly made-up, and very incorrect
def des(location):
    result = ""
    try:
        result = (x + "_" + y + "_" + z for x, y, z in location).tostring()
    except:
        result = """This area is currently unavaliable.
        Sorry for the inconvinience."""
    return result

# Location testing

def moving(location):
    print(location)
    print(des(location))
    location = move(raw_input("What direction would you like to move?"), location)
    print(location)
    print(des(location))
    return location

# Moving gameplay
#This is the infinite loop that runs the above defined moving function

win = False
while(win is False):
    print("in the loop")
    location = moving(location)
