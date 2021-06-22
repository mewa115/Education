class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.s = 1 / 2 * (self.a * self.b)


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]
print(input_c, input_b, input_a)
# write your code here
if input_a**2 + input_b**2 == input_c**2:
    triangle = RightTriangle(input_c, input_a, input_b)
    print(triangle.s)
else:
    print('Not right')
