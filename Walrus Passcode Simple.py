#Walrus expression testing
pu = ["abc", "123"]
while True:
	if (a := input("username: ")) == pu[0]:
		if (a := input("password: ")) == pu[1]:
			break