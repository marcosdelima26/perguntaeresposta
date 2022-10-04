print('A seguir você irá responder um questionário que irá analisar o seu conhecimento no conteúdo já passado.')
print('Para passar no teste necessário ter uma porcentagem de acerto de 70% ou superior, Boa Sorte!')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            '[a]': '1',
            '[b]': '4',
            '[c]': '3',
            '[d]': '5',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Qual o livro famoso ajuda no desenvolvimento de boas práticas de um programador?',
        'respostas': {
            '[a]': 'Arquitetura de Dados',
            '[b]': 'Como programar em Java',
            '[c]': 'Python dados',
            '[d]': 'Código limpo',
        },
        'resposta_certa': 'd',
    },
    'Pergunta 3': {
        'pergunta': 'Qual biblioteca no Python utilizamos para cálculos matemáticos?',
        'respostas': {
            '[a]': 'Random',
            '[b]': 'Math',
            '[c]': 'Cos',
            '[d]': 'Pandas'
        },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Qual função utilizamos para retirar os espaços no Python?',
        'respostas': {
            '[a]': 'input',
            '[b]': 'Slip',
            '[c]': 'Strip',
            '[d]': 'String',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 5': {
        'pergunta': 'O que é proporção Áurea?',
        'respostas': {
            '[a]': 'Proporção áurea é uma constante real algébrica irracional utilizada na arquitetura, '
                   'nas artes e no design gráfico. Ela é representada pela divisão de uma reta em dois '
                   'segmentos (a e b), sendo que quando a soma desses segmentos é dividida pela parte mais longa, '
                   'o resultado obtido é de aproximadamente 1,61803398875.',
            '[b]': 'O número de ouro é o representante matemático da perfeição na natureza. '
                   'Ele é estudado desde a Antiguidade e muitas construções gregas e obras artísticas '
                   'apresentam esse número como base. Seu número aproximado é 1.61803399',
            '[c]': 'É um dos métodos mais utilizados nas análises técnicas no mercado financeiro. '
                   'Este se traduz em uma sequência numérica utilizada em análises de tendências para traçar '
                   'projeções e retrações nos preços de ativos.',
            '[d]': 'Determina que a força de atração gravitacional é diretamente proporcional ao produto das massas '
                   'e inversamente proporcional ao quadrado da distância que separa os dois corpos.',
        },
        'resposta_certa': 'a',
    }
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print('[{}]: {}'.format(pk, pv["pergunta"]))

    for rk, rv in pv['respostas'].items():
        print('{}: {}'.format(rk, rv))

    resposta_usuario = input('Selecione a alternativa correta: ')

    if resposta_usuario == pv['resposta_certa']:
        print("Parabéns, resposta correta!")
        respostas_certas += 1
    else:
        print('Ops!!! Resposta incorreta!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

if porcentagem_acerto <= 70:
    print('Você não passou no teste!')
else:
    print('Parabéns, você concluiu o teste com Êxito.')
    print('Aprovado!!!!')

print('Você acertou {} respostas de {} perguntas.'.format(respostas_certas, qtd_perguntas))
print('Sua porcentagem de acerto foi de {:.1f}%'.format(porcentagem_acerto))

