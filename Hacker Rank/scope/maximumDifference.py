class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximunDiference = 0
        
    def computeDifference(self):
        elements = sorted(self.__elements)
        self.maximumDifference = elements[-1] - elements[0]

	# Add your code here

# End of Difference class
#input
#3
#1 2 5
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)