# 1.6 string compression
# Implement a method to perform basic string compression using the counts of repeated characters
# ex string aabcccccaaa would become a2b1c5a3
# if the compressed string would not become smaller than the origional
# string your method should return the origional string
# you can assume the string has only uppercase or lowercase


def compressString(stringtocompress):
    count = 0
    results = ""
    compressedstr = list(stringtocompress)
    for i in range(len(compressedstr)):
        count = count + 1
        if i + 1 == len(compressedstr):
            results = results + str(compressedstr[i]) + str(count)
        elif compressedstr[i] != compressedstr[i + 1]:
            results = results + str(compressedstr[i]) + str(count)
            count = 0
    if len(stringtocompress) == len(results):
        return stringtocompress
    else:
        return results
