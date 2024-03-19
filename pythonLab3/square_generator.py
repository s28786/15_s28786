class SquareGenerator:
    def e_squares(self, start, end):
        if end < start:
            return
        return [x * x for x in (range(start, end+1))]