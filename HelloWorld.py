my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10
poker_hand_1 = "Royal Flush"
f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")
	
f.write(poker_hand_1)
f.close()