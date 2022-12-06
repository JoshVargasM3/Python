# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
        #Here, despite G.B. Shaw's quote, our characters have started with 
        #different amounts of apples so we can better observe the results. 
        #We're going to have Martin and Johanna exchange ALL their apples with #one another.
        #Hint: how would you switch values of variables, 
        #so that "you" and "me" will exchange ALL their apples with one another?
    #####Do you need a temporary variable to store one of the values?############
        #You may need more than one line of code to do that, which is OK. 
    temporal = you.apples # para cambiar una variables con el valor de otra debes almacenar el valor en una variable temporal.
    you.apples = me.apples
    me.apples = temporal
    return you.apples, me.apples
    
    
def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    ###########the sum of ideas, or can you find another way? #############
    #Use as many lines of code as you need here.
    you.ideas += me.ideas #para sumar tus ideas y las mias y que siempre se sumen, debes asignar esta logica:
    me.ideas = you.ideas

    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))

"""///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"""
# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
		# Initialize the variable that will hold 
		# the information of the city with 
		# the highest elevation 
	return_city = ""

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population >= min_population:
		if city1.elevation > city2.elevation or city1.elevation > city3.elevation:
			return_city = city1.name + ", " + city1.country
		return return_city
			# Evaluate the 2nd instance to meet the requirements:
			# does city #2 have at least min_population and
			# is its elevation the highest evaluated so far?
	if city2.population >= min_population:
		if city2.elevation > city3.elevation or city2.elevation > city1.elevation:
			return_city = city2.name + ", " + city2.country
		return return_city
			# Evaluate the 3rd instance to meet the requirements:
			# does city #3 have at least min_population and
			# is its elevation the highest evaluated so far?
	if city3.population >= min_population:
		if city3.elevation > city2.elevation or city3.elevation > city1.elevation:
			return_city = city3.name + ", " + city3.country
		return return_city
			#Format the return string
	
	if min_population >= 10000000:
		return return_city
	else: 
		return_city


print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""


# METHODS AND CONSTRUCTORS

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {} ".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Josh Vargas")
# Call the greeting method
print(some_person.greeting())
