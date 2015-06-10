def star(n):
	for x in range(1,10):
		print(n*"*");
		print("*"+(n-2)*" "+"*");
		print(" ");
		print("*"+(n-2)*" "+"*");
		print(n*"*");

star(7);