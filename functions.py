def sum_to (num):
  sum = 0
  for i in range(num+1):
    sum+=i
  return sum
print(sum_to(6)) 
print(sum_to(10)) 

#############

def largest(nums):
  return max(nums) #If max() is called with an iterable, it returns the largest item in it

print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))

##############

def occurances(str1, str2):
  return str1.count(str2)

occurances('fleep floop', 'e')
occurances('fleep floop', 'p')
occurances('fleep floop', 'ee')
occurances('fleep floop', 'fe')

#############
def product (*args):
  product = 1
  for arg in args:
    product *= arg
  return product

print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))