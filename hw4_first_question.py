# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.

def triple(x):
  return x * 3

print(triple(3))
print(triple(5))
print(triple(9))



# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#
def subtract(c, d):
    return c - d
print(subtract(2,1))
print(subtract(9,2))
print(subtract(10,5))

# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}
def dictionary_maker(list_2_tuples):
    d = {}

    for i in list_2_tuples:
      d[i[0]] = i[1]
      
    print(d)
    return d
print('the returned fruit is:', dictionary_maker([('foo', 1), ('bar', 3)]))
