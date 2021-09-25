import colon

while True:
	usr_input = input('colon=> ')
	result, error = colon.run('<stdin>', usr_input)

	if error:
		print(error.as_string())
	else: 
		print(result)  

# !!! REFACTOR: Variable Type System, If needed.

# !!! IMPLIMENT: BOOLEAN variable type.