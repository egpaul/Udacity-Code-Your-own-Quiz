# questions for easy level
easy_level = "Old McDonald __1__ a farm E I E I O. And on his __2__ he had a cow E I E I O.\n"\
             "With a __3__ moo here and a moo moo there here a moo, there a moo everywhere a moo moo.\n"\
             "__4__ McDonald had a farm E I E I O"

# answers for easy level
easy_level_answers = ["had", "farm", "moo", "old"]

# questions for medium level
medium_level = "Old McDonald had a __1__ E I E I O. And on his farm he had a __2__ E I E I O.\n"\
               "With a oink __3__ here and a oink oink there here a oink, __4__ a oink everywhere a oink oink.\n"\
               "Old McDOnald had a farm E I E I O"

# answers for medium level
medium_level_answers = ["farm", "pig", "oink", "there"]

# questions for hard level
hard_level = "Old McDonald had __1__ farm E I E I O. And __2__ his __3__ he had a duck E I E I O.\n"\
             "With a __4__ quack here and a quack quack there here a quack, there a quack everywhere a quack quack.\n"\
             "Old McDOnald had a farm E I E I O"

# answers for hard level
hard_level_answers = ["a", "on", "farm", "quack"]

# list of question numbers for each level for player to add answer
questions = ["__1__", "__2__","__3__","__4__"]

# begining of game asking user to select a level
def get_level():
    print "Welcome to the farm! Please Select a level. You get 4 attempts per question."
    level_name = raw_input("Type in easy, medium or hard\n").lower()
    if level_name=="easy":
        process_paragraph(easy_level, questions, easy_level_answers)
    elif level_name=="medium":
        process_paragraph(medium_level, questions, medium_level_answers)
    elif level_name=="hard":
        process_paragraph(hard_level, questions, hard_level_answers)
    else:
        print "Please choose only easy, medium or hard"
    print get_level

# Starts the quiz, checks answers, limits users input
def process_paragraph(quiz, blanks, answers):
	print quiz
	for count_blanks in range(0, len(blanks)):
		answer_input = raw_input("What is " + blanks[count_blanks] +"?")
		attempts = 1
		max_attempts = 4
		while answer_input.lower()!= answers[count_blanks]:
			attempts += 1
			answer_input = raw_input("Womp womp. Lets try again. What is" + blanks[count_blanks] + "?")
			if attempts == max_attempts:
				print ("Looks like you don't belong on the farm. Let's try again!")
				get_level()
		else:
			quiz = quiz.replace(blanks[count_blanks], answers[count_blanks])
			print("Correct! " + quiz)
	if len(blanks) == len(answers):
		print ("You're going to make a great farmer! Want to try another level?")
		get_level()

get_level()
