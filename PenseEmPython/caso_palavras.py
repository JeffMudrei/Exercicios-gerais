def sem_e(w):
    if 'e' in w:
        pass
    else:
        print(w)



fin = open('words.txt')
total = 0
e = 0
for line in fin:
    total += 1
    word = line.strip()
    if 'e' in word:
        e += 1
    sem_e(word)

x = ((e*100)/total)
print(f"Total de palavras {total}\nTotal de palavras com 'e' {e}\nPercentual de palavras com 'e': {x}%")


    #if len(word)>= 20:
    #   print(word)
