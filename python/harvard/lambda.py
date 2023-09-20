people = [
    {'name': 'Satyam', 'house': 'red'},
    {'name': 'Shivam' , 'house': 'green'},
    {'name': 'Aditya' , 'house': 'blue'}
]
# dictionary inside list

print(people)
print(people[0])
#people.sort() --> gives type error as python don't know how to sort it
#print(people) 

# lambda function for sorting dict inside list
def f(person):
    return person['name']

people.sort(key= f)
print(people)

human = [
    {'name': 'Satyam', 'house': 'blue'},
    {'name': 'Shivam' , 'house': 'green'},
    {'name': 'Aditya' , 'house': 'red'}
]

# use direct lambda function

human.sort(key = lambda person: person['house'])
print(human)

