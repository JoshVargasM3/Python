# Introduccion a los diccionarios, estos se elaboran con {} y las entradas o 'keys' son losas paalabras y 
# los numeros son los valores
# para ingresar nuevos valores 1
# para cambiar valores 2
# para consultar valores 3
# para corroborar si el elemento se encuentra en la key 4

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39 ----- 1
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24 ----- 2
print(toc) # What are the current contents of the dictionary? ----- 3
print("Chapter 5" in toc)  # Is there a Chapter 5? ----- 4


""""////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////"""


#In Python, a dictionary can only hold a single value for a given key. 
# To workaround this, our single value can be a list containing multiple values. 
# Here we have a dictionary called "wardrobe" with items of clothing and their colors. 
# Fill in the blanks to print a line for each item of clothing with each color, 
# for example: "red shirt", "blue shirt", and so on.

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloths, colors in wardrobe.items():
	for color in colors:
		print("{} {}".format(color, cloths)) 
        # asi se llama un elemento dentro de un valor almacenado en formato de lista con multiples valores.