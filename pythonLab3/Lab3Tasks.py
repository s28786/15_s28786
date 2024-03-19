import math


class SquareGenerator:
    def e_squares(self, start, end):
        if end < start:
            return
        return [x * x for x in (range(start, end+1))]

S = SquareGenerator()
square_list = S.e_squares(11,10)
print(square_list)

square_root = [math.sqrt(x) for x in S.e_squares(1,10)]
print(square_root)