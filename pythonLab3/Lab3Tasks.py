import math
from square_generator import CubicGenerator

S = CubicGenerator()
square_list = S.e_squares(1,10)
print(square_list)

square_root = [math.sqrt(x) for x in S.e_squares(1,10)]
print(square_root)

cubic_list = S.e_cubes(1,10)
print(cubic_list)