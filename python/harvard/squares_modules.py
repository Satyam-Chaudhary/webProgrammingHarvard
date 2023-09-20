#from functions import square # import square function from functions
import functions # import functions but need to use functions.square() in this case
for i in range(10):
    print(f'Square of {i} --> {functions.square(i)}')
