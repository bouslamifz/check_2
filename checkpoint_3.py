'''Task_1'''

# Write a Python program that multiplies all the items in a list.

liste = []
lenght = int(input("donner la taille de la liste "))
for i in range(lenght):
    liste.append(int(input(f"donner l'item numero {i} \t")))

p=1
for i in liste:
    p = p * i
print("le produit de tous les elements de liste est ",p)



"""Task_2"""


# Write a Python program to get a list, sorted in increasing order by the last element in each tuple, from a given list
#
# of non-empty tuples.
#
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# Expected result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#
# Hint: You can use the sort function.


"""Methode_1"""

def last(n):
	return n[-1]

def sort(tuples):
	return sorted(tuples, key=last)

a= [(4, 8), (7, 2),(6, 3), (9, 1)]
print("Sorted:")

print(sort(a))

"""Methode_2"""

liste = [(2,5,6),(1,2,8),(4,4,4),(2,3,2),(2,1,7)]
#use the sort function


liste.sort(key=lambda x:x[-1])
print(liste)


"""Task_3"""


#Write a Python program that combines two dictionaries by adding values for common keys.

#d1 = {'a': 100, 'b': 200, 'c':300}

#d2 = {'a': 300, 'b': 200, 'd':400}

#Expected result: {'a': 400, 'b': 400, 'd': 400, 'c': 300}

d1 = {'a': 100, 'b': 200, 'c':300}

d2 = {'a': 300, 'b': 200, 'd':400}

d3 = dict(d1)

d3.update(d2)

for i, j in d1.items():
    
    for x, y in d2.items():
        if i == x:
            d3[i]=(j+y)
print(d3)


"""Task_4"""

#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) so that is an 
# integral number between 1 and n (both included). Then the program should print
# the dictionary. Suppose the following input is supplied to the program: 8. Then, the output should be:\
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

number = int(input("Type a number: "))

numberDict = {}
for i in range(1, number+1):
    numberDict[i] = i*i

print(numberDict)

"""Task_6"""

#Write a program to sort a tuple by its float element.

#For example: list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

#Expected result: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]"""



liste= [('item1', '50.10','54.3'), ('item2', '10.82','52.6'), ('item3', '100.9','8.04')]
print( sorted(liste, key = lambda x: float(x[2]), reverse=True))
