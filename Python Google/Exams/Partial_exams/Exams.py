def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))

11 % 5

"big" > "small"

((10 >= 5*2) and (10 <= 5*2))


def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient
	if denominator==0:
		return 0
	else:
		return (numerator/denominator)%1
	
print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

5%5
5//4
5%4
5/4
(5/4)%1
1.25%1
6%4
6//4
6/4
(6//4)%1

def calculate_storage(filesize):
    block_size = 4096
 # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//4096
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize%4096
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return 4096 * (full_blocks+1)
    return full_blocks*4096

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(9000)) # Should be 8192

x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
  print("x=" + str(x))