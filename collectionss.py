# # Lists - ordered, mutable, collection of values.
# # Tuples - ordered, immutable, collection of values.
# # Dictionaries - unordered, mutable, collection of key-value pairs.
# # Sets - unordered, mutable, collection of unique values.

#lists

# Lists refer to multiple values which are all contained in, and accessible through, a single variable.
# The values in a list can be altered after the list has been created, and the list can even hold duplicate values.

# Lists are defined with square braces, [ ], and each element in the list is separated by commas.
# cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
#referencing elements:
# >>> cool_cows[2] - 'Milkshake'
# >>> cool_cows[-1] -'Mooana'
#slice e.g.
# >>> cool_cows[1:3] ['Moolan', 'Milkshake']
# If we wanted to include the final element in our result, we would not specify an index to stop at:
# >>> cool_cows[1:] -- ['Moolan', 'Milkshake', 'Mooana']

# Altering Lists
# cool_cows[0] = "Aladdin but a cow" replaces whatever [0] was with "aladdin but a cow"
# del cool_cows[0] - del for delete can us list.pop e.g.
# list.pop()
# list.append() - Append object to the end of the list.
# list.remove() - Remove first occurrence of value.
# list.insert() - Insert object before index. e.g.  
 #  >>> my_fruit.insert(0, "Mango")
#   >>> print(my_fruit)
#   ['Mango', 'Apple', 'Banana', 'Orange']
# list.extend() - Extend list by another list (or any iterable). e.g
#   >>> my_fruit.extend(["Grapefruit", "Kiwi"])
#   >>> print(my_fruit)
#   ['Apple', 'Banana', 'Orange', 'Grapefruit', 'Kiwi']
# list.index() - Return first index of value. e.g.   >>> my_fruit.index("Apple") -- is 0
# list.count() - Return number of occurrences of value.
# list.reverse() - Reverse the list.
# list.sort() - Sort the list in ascending order. .sort(key=len) # Sort by the length, so we will have shortest items first

# Checking Membership
# Checking membership is to check if an object is contained in a collection. We can do this using the in keyword.
# Doing so will return a boolean depending on whether the object was found or not.

# Tuples
# A tuple is defined in the same way that a list is, except we use ( ) instead of [ ], or nothing at all.

# We may decide to use tuples over lists for any of the following reasons:
# 1) Readability - makes it clear to anyone reading our code we do not intend to change the values in this collection.
# 2) Memory usage - tuples are more memory efficient in comparison to lists, because they do not need to worry about changing size later on.
# 3) Speed - tuples are quicker than lists in many cases, although this is fairly minimal.

# Dictionaries
# e.g. >>> noises = {"cow" : "moo", "sheep" : "baa"}
# Dictionaries are similar to lists as well, except they use keys as indexes, instead of numbers, as items in a dictionary are not held in any particular order.

# They make use of a key-value pair system.
# This means that when defining a dictionary, we have to make sure that there is a unique key which corresponds to each value in the collection.

# We know the keys are what we use to query a dictionary, and the values are what we get out when we query it.

# In order to find out all of the keys, or all of the values, we can use the methods dict.keys(), or dict.values(), respectively.

# Sets
# Sets are similar to lists, as they are mutable, but there are a few key distinctions:

# Sets are unordered, and so we cannot index items within them in any way.
# Sets cannot contain duplicate values, similar to the keys in a dictionary.
# Sets cannot contain other sets, so we can never have a multi-dimensional set.
# e.g. >>> my_items = ["Apple", "Banana", "Apple", "Banana", "Orange"]
# >>> set(my_items)
# {'Orange', 'Apple', 'Banana'}