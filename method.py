def move(time,speed):
	print("i am moving on"+str(speed)+"kmph"+"at"+str(time));
	time=time+1;
	speed=speed-1;
	print("i am moving on"+str(speed)+"kmph"+"at"+str(time));
move(10,5);
print("------------");
move(20,5);
print("------------")