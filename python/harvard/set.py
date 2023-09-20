# all elements are unique and don't care about order

#create an empty set

s = set()

# Add element to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(4) # no element ever occur twice thus it is not seen when printed
print(s)
s.remove(2)
print(s)
print(f'length of set --> {len(s)}')
