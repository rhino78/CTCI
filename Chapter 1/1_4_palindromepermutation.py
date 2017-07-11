# 1.4 palindrome permutation
#given a string, write a function to check if it is a permutation of a palindrome
#the palindrome does not need to be limited to just dictionary words
#input Tact Coa
#output True (permutations: "taco cat", "atco cta", ect)

def createPalindrome(palihash, charpali):
	newchar = {}
	first = 0
	last = len(charpali)
	results = ''
	for l,n in palihash.items():
		if n == '1':
			newchar[len(charpali) / 2] = l
		else:
			newchar[first] = l
			newchar[last] = l
			first = first +1
			last = last -1

	if '\0' in newchar:
		keyindex = newchar.index('\0')
		newchar[keyindex] = ' '

	for n, l in newchar.items():
		results = results + srt(l)


	return str(results)

def createstrPalindrome(charpali):
	palichar = list(charpali)
	temp0 = palichar[0]
	temp1 = palichar[1]
	temp6 = palichar[6]
	temp7 = palichar[7]

	newchar = list(charpali)
	newchar[0] = temp1
	newchar[1] = temp0
	newchar[6] = temp7
	newchar[7] = temp6

	return ''.join(palichar)

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
		for l, n in palihash.items():
			if firstTime and n == '1':
				firstTime = False
			elif not firstTime and n != '2':
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