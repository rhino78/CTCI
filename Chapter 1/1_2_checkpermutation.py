#check permutation 1.2
#given two strings write a method to decide if one is a permutation of the other

def sort(string):
	content = list(string)
	content.sort()
	results = ''.join(content)
	return results

def permutations(one, two):
	if len(one) != len(two):
		return False
	else:
		return sort(one) == sort(two)
