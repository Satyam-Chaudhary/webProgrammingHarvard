class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

class Flight():
    def __init__(self , capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats(): # if self.open_seats() == 0:
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
    

p = Point(2, 4)
print(p.x)
print(p.y)

flight = Flight(3)
peoples = ['Satyam', 'Hermione', 'Shivam', 'Shobhit']
for people in peoples:
    succes = flight.add_passenger(people)
    if succes:
        print(f'Added {people} to flight succesfuly')
    else:
        print(f'Failed to add {people} to flight')

print(flight.passengers)


