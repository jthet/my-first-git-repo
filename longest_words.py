

words = []


with open('/usr/share/dict/words', 'r') as infile:
    words = infile.read().splitlines()

# words.sort(key=len, reverse = True)      <- Changes list directly

sorted_words = sorted(words,key=len, reverse=True)

for i in range(5):
    print(sorted_words[i])
