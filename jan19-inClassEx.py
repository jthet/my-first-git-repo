


with open('/usr/share/dict/words', 'r') as f:
    word = f.readlines()

    count = 0
    for w in word:
        if len(w.strip('\n')) == 25:
            count +=1

        if count == 10:
            print(w)
            break