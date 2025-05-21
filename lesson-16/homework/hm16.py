#1.

import numpy as np


original_list = [12.23, 13.32, 100, 36.32]


array = np.array(original_list)


print("Original List:", original_list)
print("One-dimensional NumPy array:", array)

#2.

import numpy as np


matrix = np.arange(2, 11).reshape(3, 3)


print(matrix)


#3.

import numpy as np

vector = np.zeros(10)
print("Original null vector:", vector)


vector[6] = 11
print("Updated vector:", vector)

#4.
import numpy as np

array = np.arange(12, 38)

print(array)


#5.

import numpy as np

original_array = np.array([1, 2, 3, 4])
print("Original array:", original_array)

float_array = original_array.astype(float)
print("Array converted to float type:", float_array)

#6.import numpy as np

celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])

fahrenheit = celsius * 9/5 + 32

print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)


#7.Append Values to Array (Do self-tudy)
Write a NumPy program to append values to the end of an array.

Expected Output:

Original array: [10, 20, 30]

After append values to the end of the array: [10 20 30 40 50 60 70 80 90]

  
import numpy as np

original_array = np.array([10, 20, 30])
print("Original array:", original_array)

values_to_append = [40, 50, 60, 70, 80, 90]

updated_array = np.append(original_array, values_to_append)

print("After append values to the end of the array:", updated_array)

#8.
import numpy as np

array = np.random.randint(0, 100, size=10)

mean_val = np.mean(array)
median_val = np.median(array)
std_dev = np.std(array)

print("Random array:", array)
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)

#9.

  import numpy as np

array = np.random.rand(10, 10)

min_val = np.min(array)
max_val = np.max(array)

print("10x10 Random Array:\n", array)
print("\nMinimum value:", min_val)
print("Maximum value:", max_val)


#10.

     import numpy as np

array_3d = np.random.rand(3, 3, 3)

print("3x3x3 Random Array:\n", array_3d)

       
  3x3x3 Random Array:
[[[0.54 0.73 0.91]
  [0.85 0.02 0.67]
  [0.49 0.88 0.21]]

 [[0.10 0.30 0.42]
  [0.96 0.55 0.75]
  [0.34 0.61 0.18]]

 [[0.81 0.27 0.04]
  [0.66 0.93 0.59]
  [0.45 0.79 0.07]]]

      
