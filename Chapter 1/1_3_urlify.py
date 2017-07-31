# 1.3 urlify
# write a method to replace all spaces of a string with '%20'
# you may assume the string has space at the end to hold characters
# and that you are given the true length of a string
# input example "Mr John Smith      ", 13
# output "Mr%20John%20Smith


def urlify(strtochange, truelength):
    urlit = list(strtochange)
    spaceCount = 0
    for i in range(truelength):
        if urlit[i] == " ":
            spaceCount += 1

    index = truelength + spaceCount * 2
    if truelength < len(strtochange):
        urlit[truelength] = '\0'
    for i in range(truelength - 1, -1, -1):
        if urlit[i] == " ":
            urlit[index - 1] = '0'
            urlit[index - 2] = '2'
            urlit[index - 3] = '%'
            index = index - 3
        else:
            urlit[index - 1] = urlit[i]
            index = - index - 1
    return ''.join(urlit)
