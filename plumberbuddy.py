#needs error handling.
import json
data= json.load(open("plumbinglibrary.json"))
search=""
import difflib
seq =""
print("Hi, I'm the plumber buddy how can I help you? ")
offset_Fittings=[22,45,]
objects = ["rectangle","cylinder","elliptical","spheres","Frostu"]
choices_function=["offset","volume","dictionary",]
#measurments
diameter = 0
volume = 0
length = 0
height = 0
width = 0
gallons = 0
inches = ""
feet = ""
cylinder_constant = 0
#divide
gallons_inches = 231
#multiply
gallons_feet = 7.48

constant_45 = 1.414
constant_22 = 2.613

### computex offsets.''
def offset_to_travel():
    solve = 1
    while solve == 1:
        print("What is you fitting?")
        fitting = input ("please enter 22 or 45.")
        if int(fitting) not in offset_Fittings:
            print("I dont know that fitting.")
        if int(fitting)  in offset_Fittings:
            solve = 2
    while solve == 2:
        if int(fitting) == 45:
            offset_45 = input("To find your travel distance first  give your offset measurment.")
            travel = constant_45 * float(offset_45)
            print (travel)
            choose_function()
        if int(fitting) == 22:
            offset_22 = input("To find your travel distance first  give your offset measurment.")
            travel = constant_22 * float(offset_22)
            print (travel)
            choose_function()
#get the volume of a volume_rectangle
def volume_rectangle():
    length = input ("input length inches or feet ")
    height = input ("input heigh inches or feet ")
    width  = input ("input width inches of feet ")
    volume = float(length) * float(width) * float(height)
    print("Is this in feet or inches?")
    print("inches or feet? ")
    inches_or_feet = input("")
    if inches_or_feet == ("feet"):
        feet = volume * gallons_feet
        print (feet )
        print(" gallons")
        choose_function()
    if  inches_or_feet == ("inches"):
        inches = volume / gallons_inches
        print (inches)
        print ("gallons")
        choose_function()
#get the volume of a cylinderself.
def volume_cylinder():
    diameter =input("Diameter")
    length = input("Length")
    volume = float(diameter) * float(diameter) * float(cylinder_constant) * float(length)
    print("Is this in feet or inches?")
    print("inches or feet? ")
    inches_or_feet = input("")
    if inches_or_feet == ("feet"):
        feet = volume * gallons_feet
        print (feet )
        print(" gallons")
        choose_function()
    if  inches_or_feet == ("inches"):
        inches = volume / gallons_inches
        print (inches)
        print ("gallons")
        choose_function()

def volume_eliptical():
    length = input ("input length inches or feet ")
    height = input ("input heigh inches or feet ")
    width  = input ("input width inches of feet ")
    volume = float(height) * float(width) * float(cylinder_constant) * float(length)
    print("Is this in feet or inches?")
    print("inches or feet? ")
    inches_or_feet = input("")
    if inches_or_feet == ("feet"):
        feet = volume * gallons_feet
        print (feet )
        print(" gallons")
        choose_function()
    if  inches_or_feet == ("inches"):
        inches = volume / gallons_inches
        print (inches)
        print ("gallons")
        choose_function()




#function to find shape volumes
def volume_shape_of():
    solve_volume = 1
    while solve_volume == 1:
        print ("what is the shape you want to find the volume of? ")
        print (objects)
        object = input("")
        if object not in objects :
            print ("Please select another object.")
        if object == "rectangle":
            volume_rectangle()
        if object == "cylinder":
            volume_cylinder()
        if object ==  "elliptical":
            volume_eliptical()



def dictionary():
    search = input ("what definition do want?")
    if search in data:
        print (data[search])
    else:
        alt= difflib.get_close_matches(search,data)

        print ("I do not know that word")
        print("did you mean?")
        print (alt)



#main menu
def choose_function():
    solve_function =1
    while solve_function ==1 :
        print("What would you like to calculate")
        print(choices_function)
        problem_solve = input ("please choose from this list.  ")
        if problem_solve not in choices_function:
            print ("I do not know that calculation.")
        if problem_solve in choices_function:
            solve_function = 2
    while solve_function ==2:
        if problem_solve == "offset" :
            offset_to_travel()
        if problem_solve == "volume" :
            volume_shape_of()
        if problem_solve == "dictionary":
            dictionary()


















choose_function()
