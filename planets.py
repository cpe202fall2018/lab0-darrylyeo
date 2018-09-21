# Assignment:
# http://users.csc.calpoly.edu/~phatalsk/202/labs/lab00/lab00.pdf

def weight_on_planets():
	weight = float(input('What do you weigh on earth? '))
	output = '\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.'.format(weight * 0.38, weight * 2.34)
	print(output)

if __name__ == '__main__':
	weight_on_planets()