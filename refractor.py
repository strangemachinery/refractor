import sys

#first = int(raw_input("What the first number do you want?  "))
#second = int(raw_input("Whats the second number?  "))
#print "The two numbers you have picked are: %d, %d" % (first, second)

def divisible(a, b):
        return a % b == 0

#	 a % b == 0 or b % a == 0
#		return True
#	else:
#		return False
#divided = divisible(first,second)
#print "Is it true or false? Well.....it's %s!!!!" % divided

def upperlimit(upper=100):
        for x in range(1, upper+1):
                if divisible(x, 15):
                        print "fizz buzz"
#		if divisble(x, 3) and divisble(x, 5):
                elif divisible(x, 3):
                        print "fixx"
                elif divisible(x, 5):
                        print "buzz"
                else:
                        print x

if __name__ == '__main__':
	upper = int(sys.argv[1])
	upperlimit(upper)
