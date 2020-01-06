def desenha_grade_linhas():
    print('+ ', '- ' * 4, end=' ')
    print('+ ', '- ' * 4, end=' ')
    print('+')

def desenha_colunas():
    print('|', ' ' *9,'+', ' ' * 9, '|')

def do_four():
    desenha_colunas()
    desenha_colunas()
    desenha_colunas()
    desenha_colunas()

def grade():
    desenha_grade_linhas()
    do_four()
    desenha_grade_linhas()
    do_four()
    desenha_grade_linhas()

grade()