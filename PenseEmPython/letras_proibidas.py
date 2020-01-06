def letras_proibidas(a, words):
    if a in words:
        pass
    else:
        print(words)

fin = open('words.txt')
a = 'abcde'
n = 0
for line in fin:
    word = line.strip()
    if a in word:
        pass
    else:
        n += 1
    letras_proibidas(a, word)
print(f'Palavras sem {a}: {n}')