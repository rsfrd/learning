name = ''
while not name:
    print('Enter your name:')
    name = input()
while True:
	print('How many guests will you have?')
	try:
		numOfGuests = int(input())
		break
	except ValueError:
		print ('Needs to be a number!')
if numOfGuests <= 4:
	print ('That\'ll be easy.')
else:
	print('Be sure to have enough room for all your guests.') #(3)
print('Done')
