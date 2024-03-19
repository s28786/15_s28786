class SquareGenerator:
    def e_squares(self, start, end):
        return [x * x for x in (range(start, end+1))]

S = SquareGenerator()
print(S.e_squares(1,10))