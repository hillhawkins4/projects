

#This area was made to define certain atributes in the code


password = input("Check your Password Here: ")
score = 0
special_chars = "_?><-+=|\!@#$%^&*"


# This area is designed to take parts out of the password and award "points" to good passwords


if len(password) > 8:
    score = score + 1
if any(char.isupper() for char in password):
    score = score + 1
if any(char.isnumeric() for char in password):
    score = score + 1
if any(char in special_chars for char in password):
    score += 1


# This area is designed to correlate a score to feedback


if score == 0:
    print('Teribble Password')
if score == 1:
    print('Bad Password')
if score == 2:
    print('Good Password')
if score == 3:
    print('Great Password')
if score == 4:
    print('Amazing Password')