print('Hello')
input_user = input('\nEnter you cube or square: ')
no_chances = 0
while input_user == "cube" or "square":
	if input_user == "cube":
		cube_number = int(input("Enter numbers: "))
		result = cube_number * cube_number * cube_number
		print("Answer is:", result)
		no_chances = no_chances + 1
		print('You have played', no_chances, "time")
		if no_chances == 1:
			print('\nFree trial over')
			quit(10)
		input_user = input('\nEnter you cube or square: ')
			
	elif input_user == "square":
		square_number = int(input("Enter numbers: "))
		result_2 = square_number * square_number
		print("Answer is:", result_2)
		no_chances = no_chances + 1
		print(f'You have played {no_chances}')
		if no_chances == 1:
			print('\nFree trial over')
			quit(10)
		input_user = input('\nEnter you cube or square: ')
	
	else: 
		print("Error")
		break

if no_chances == 1:
	print('Free trial over')
	quit(10)