#impor numpy to do the mathematics for the code
import numpy as np
#import pprint to give a better presentation to our project
import pprint

#define the function calculate
def calculate(data):
    #we declare the condition that our numbers must be 9
    if len(data) !=9:
        raise ValueError('List must contain nine numbers.')
    #transform our 1 dimension array into a 3x3 Matrix
    matrix = np.array(data).reshape(3,3)
    #we create our dictionary and specify each process    
    dictionary = { 
            'mean': [
        [float(x) for x in matrix.mean(axis=0).tolist()],  # Convertir a float
        [float(x) for x in matrix.mean(axis=1).tolist()],  # Convertir a float
        float(matrix.mean())                              # Convertir a float
    ],
    'variance': [
        [float(x) for x in matrix.var(axis=0).tolist()],   # Convertir a float
        [float(x) for x in matrix.var(axis=1).tolist()],   # Convertir a float
        float(matrix.var())                                # Convertir a float
    ],
    'standard deviation': [
        [float(x) for x in matrix.std(axis=0).tolist()],   # Convertir a float
        [float(x) for x in matrix.std(axis=1).tolist()],   # Convertir a float
        float(matrix.std())                                # Convertir a float
    ],
    'max': [
        [float(x) for x in matrix.max(axis=0).tolist()],   # Convertir a float
        [float(x) for x in matrix.max(axis=1).tolist()],   # Convertir a float
        float(matrix.max())                                # Convertir a float
    ],
    'min': [
        [float(x) for x in matrix.min(axis=0).tolist()],   # Convertir a float
        [float(x) for x in matrix.min(axis=1).tolist()],   # Convertir a float
        float(matrix.min())                                # Convertir a float
    ],
    'sum': [
        [float(x) for x in matrix.sum(axis=0).tolist()],   # Convertir a float
        [float(x) for x in matrix.sum(axis=1).tolist()],   # Convertir a float
        float(matrix.sum())                                # Convertir a float
    ]
    }
    
    #the return of our fuction will be the dictionary we created bf
    return dictionary

#we specify the input
a = input('insert a list of 9 numbers separed by a coma: ')
#we transform our str input into a int array
a = [int(x) for x in a.split(',')]
#we call the function
a = calculate(a)

#To print each data properly
for stat, values in a.items():
    print(f"{stat.capitalize()}: {values}")
    print()