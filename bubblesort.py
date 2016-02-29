#Program for Bubble Sort.

my_list=[23,56,7,-4,0,5]
print(my_list)
length= len(my_list)

for i in range(length):
	for j in range(length-1):
		if my_list[j]>my_list[j+1]:
			my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
			print(my_list)
