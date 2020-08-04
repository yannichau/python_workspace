# Numpy Tutorial Notes

## Why are lists slow and Numpy Faster
Normally, a list contains
- size
- reference count
- object type
- object value
- operations
    - insertion, deletion, appending, concatenation (numpy does much more.........like multiply arrays)
Numpy
- has no type checking
- Contiguous memory:
    - Lists contain pointers to scatters location within the computer's memory location, which is not really efficient
    - Whereas for numpy: you just store one pointer, information on start, length, end etc.
- Benefits
    - Computers use SIMD Vector Processing: perform similar computations on a large data set at the same time
    - effective cache utilisation
- Applications
    - SciPy: look at that as well!
    - MATLAB replacement
    - Plot with Matplotlib
    - Backend for Pandas, Connect 4, Digital Photography
    - Tensors and machine learningP