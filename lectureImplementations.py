# Tensors : Data structures
# 0D Tensor --> Scalars
import numpy as np
a = np.array(4)
print(a.ndim)

# 1D Tensor --> Vectors ; 1D Tensors --> Vector (basically vector is a collection of scalars similarly with matrices, etc)
arr = np.array([1, 2, 3, 4]) # specifically this example is a 4 dim vector which is nothing but 1 dim tensor
print(arr.ndim)

# 2D Tensor --> Matrices
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat.ndim)

# Similarly for ND Tensors
# 3D Tensors --> for ex :- cube (Images, Time series data)
# 4D Tensors --> for ex :- cubes in a line (Computer vision -> collection of images --> videos)
# 5D Tensors --> for ex :- cubes in a plane (Collection of videos)

# Rank = number of dim = number of axes
# Size of tensor = number of items in it --> for ex :- in a matrix of 3*3 there are 9 elements and shape is (3,3)

# Note:
# * [1, 2, 3, 4, ......, 50] --> 1D Tensor (or) 50D Vector
# * The data given as input will have N columns and each row of input is a 1D Tensor or ND Vector --> Here each row is 1D Tensor or we can say
#   all these rows can be represented as 2D Tensor of (number of rows) * N Matrix
# * The data we get as output for each row gives an element of (number of rows)D Vector or 1D Tensor
# * For 3D Tensor : NLP --> text vectorisation :
#   Three sentences : "Hi Nitish", "Hi Rahul", "Hi Ankit" --> if "Hi" is [1, 0, 0, 0], "Nitish" is [0, 1, 0, 0], "Rahul" is [0, 0, 1, 0] and "Ankit" is [0, 0, 0, 1]
#   then the sentences represented as : [[[1, 0, 0, 0], [0, 1, 0, 0]], [[1, 0, 0, 0], [0, 0, 1, 0]], [[1, 0, 0, 0], [0, 0, 0, 1]]] --> 3D Tensor

