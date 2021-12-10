from values import Values
from readSerial import SerialStart
from xysums import xValues, xyValues

def main():
	#main function
	SerialStart()
	Values()
	print("hasta ahora todo bien")

if __name__ == '__main__':
	main()
