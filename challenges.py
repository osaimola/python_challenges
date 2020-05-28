"""Create a function that takes a 2D array as an argument and returns
the number of people whose view is blocked by a tall person. The concert
stage is pointed towards the top of the 2D array and the tall person
(represented by a 2) blocks the view of all the people (represented by a 1)
behind them."""
def block(lst):
	rows = len(lst) - 1
	blocked = 0
	for i in range(rows):
		blocked += (lst[i].count(2) * (rows - i))
	return blocked