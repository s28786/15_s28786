import math
from square_generator import SquareGenerator

S = SquareGenerator()
square_list = S.e_squares(11,10)
print(square_list)

square_root = [math.sqrt(x) for x in S.e_squares(1,10)]
print(square_root)