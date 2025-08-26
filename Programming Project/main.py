##########################################################################
#
#    main.py
#    randomized selection
#
#    simple main to test randSelect
#    NOTE: this main is only for you to test randSelect. We will compile
#          your code against a different main in our autograder directory
#
##########################################################################

from randSelect import randSelect


def main():
	v = [4,4,5,4,4]
	rankWeWant = 4
	ourNumber = randSelect(v, rankWeWant)
	expectedNumber = sorted(v)[rankWeWant]
	print("Nooo!") if ourNumber != expectedNumber else print("Yayy!")
	print(ourNumber)
	print(expectedNumber)


if __name__ == '__main__':
	main()