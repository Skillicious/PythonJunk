from graphics import*

def main():
	principal = eval(input("Enter the intial principal: "))
	apr = eval(input("Enter the annualized unterest rate: "))
	
	win = GraphWin("Investment Growth Chart", 320,240)
	win.setBackground("white")
	
	Text(Point(20,230), " 0.0K").draw(win)
	Text(Point(20,180), " 2.5K").draw(win)
	Text(Point(20,130), " 5.0K").draw(win)
	Text(Point(20,80), " 7.5K").draw(win)
	Text(Point(20,30), " 10.0K").draw(win)

	height = principal * 0.02
	cat = Rectangle(Point(40,230), Point(65, 230-height))
	cat.setFill("green")
	cat.setWidth(2)
	cat.draw(win)

	for year in range(1,11):
		principal = principal * (1 + apr)
		x11 = year * 25 + 40
		height = principal * 0.02
		bar = Rectangle(Point(x11, 230), Point(x11+25, 230 -height))
		bar.setFill("green")
		bar.setWidth(2)
		bar.draw(win)



	input("Press <Enter> to quit")
	win.close()

main()

