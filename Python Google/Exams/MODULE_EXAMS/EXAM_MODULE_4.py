# Pregunta 1
# The format_address function separates out parts of the address string into new strings: 
# house_number and street_name, and returns: "house number X on street named Y". 
# The format of the input string is: numeric house number, followed by the street name which may contain numbers, 
# but never by themselves, and could be several words long. 
# For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". 
# Fill in the gaps to complete this function.
def format_address(address_string):
  street = []
  address = address_string.split()
  for parts in address:
    if parts.isnumeric():
      number = parts
    else:
      street += [parts]
  return "house number {} on street named {}".format(number, " ".join(street))

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

""""////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////"""
# Pregunta 2 The highlight_word function changes the given word in a sentence to its upper-case version. 
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". 
# Can you write this function in just one line?

def highlight_word(sentence, word):
	return(sentence.replace(word, word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
""""////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////"""
# Pregunta 3 A professor with two assistants, Jamie and Drew, wants an attendance list of the students, 
# in the order that they arrived in the classroom. Drew was the first one to note which students arrived, 
# and then Jamie took over. After the class, they each entered their lists into the computer and 
# emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. 
# Jamie emailed a follow-up, saying that her list is in reverse order. 
# Complete the steps to combine them into one list as follows: the contents of Drew's list, 
# followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
    new_list = list2 + list1[::-1]
    return new_list
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

""""////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////"""
# Use a list comprehension to create a list of squared numbers (n*n). The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively.
# For example, squares(2, 3) should return [4, 9].
def squares(start, end):
	return [ x*x for x in range(start, end+1)  ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

""""////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////"""
# Complete the code to iterate through the keys and values of the car_prices dictionary, 
# printing out some information about each one.
def car_listing(car_prices):
  result = ""
  for model, price in car_prices.items():
    result += "{} costs {} dollars".format(model, price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
""""////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////"""

""""////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////"""
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
host_addresses.keys()
""""////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////"""

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)
""""////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////"""

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])
