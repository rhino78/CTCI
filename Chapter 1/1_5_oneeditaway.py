#1.5 one away
#There are three types of edits that can be performed on strings
#insert a character, remover or replace a character. 
#Given two strings, wrinte a function to check if they are one edit (or zero edits) away
#EXAMPLE:
#pale, ple -> true
#pales, pale -> true
#pale, bale -> true
#pale, bake -> false

def oneeditaway(one, two):
	changes = 0
	for c in one:
		if not c in two:
			changes = changes + 1

	return changes <= 1 

