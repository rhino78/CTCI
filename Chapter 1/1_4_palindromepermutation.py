# 1.4 palindrome permutation
#given a string, write a function to check if it is a permutation of a palindrome
#the palindrome does not need to be limited to just dictionary words
#input Tact Coa
#output True (permutations: "taco cat", "atco cta", ect)

def createPalindrome(palihash, charpali):
	return False

def createstrPalindrome(charpali):
	return False

def populateallpalidromes(palihash, palichar):
	results = []
	firstchar = createPalindrome(palihash, palichar)
	results.append(firstchar)
	secondchar = createstrPalindrome(firstchar)
	results.append(secondchar)
	return results

def ispalindrome(palihash, count):
	firstTime = True
	if count % 2 ==1:
		for p in palihash:
			if firstTime and p.Value == '1':
				firstTime = False
			else if not firstTime and p.Value != '2':
				return False
	return True

def palindromepermutations(checkstr):
	palichar = list(checkstr)
	palihash = {}
	countofchars = 0

	for i in range(len(checkstr)):
		if palichar[i] != ' ':
			countofchars += 1
			if palichar[i].lower() in palihash:
				k = palihash[palichar[i].lower()]
				palihash[palichar[i].lower()] = k + 1
			else:
				palihash[palichar[i].lower()] = 1

	if ispalindrome(palihash, countofchars):
		listofpalidromes = populateallpalidromes(palihash, palichar)
		print("{0} (permutations: {1}, ect)".format("True", ",".join(listofpalidromes)))