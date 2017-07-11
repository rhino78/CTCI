#is unique
#implement an algorithm to determine if a string has all unique characters
def is_unique(string):
	if not string:
		return False
	else:
		hashset = set()
		for l in string:
			if l in hashset:
				return False
			else:
				hashset.add(l)
	return True