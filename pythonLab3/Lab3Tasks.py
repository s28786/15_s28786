class SquareGenerator:
    def e_squares(start, end):
        tasklist = list(range(start, end))
        reslist = [x * x for x in tasklist]
        return reslist

print(SquareGenerator.e_squares(1,11))