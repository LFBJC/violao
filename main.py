import pandas as pd
import numpy as np
import random
rng = np.random.default_rng()
a = np.array([list('1234')]*30)
exercicios_mobilidade = list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
a = np.array([list('12341234')]*180)
exercicios_mobilidade += list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
acordes_maiores_basicos = list('ABCDEFG')
acordes_maiores_basicos += [x + '#' for x in acordes_maiores_basicos]
acordes_maiores_basicos = [acorde for acorde in acordes_maiores_basicos if acorde not in ['E#', 'B#']]
acordes_menores_basicos = [x + 'm' for x in acordes_maiores_basicos]
acordes_suspensos = [x + 'sus' for x in acordes_maiores_basicos]
todos_os_acordes = acordes_maiores_basicos + acordes_menores_basicos + acordes_suspensos
todos_os_acordes += [
    acorde + complemento for acorde in (acordes_maiores_basicos + acordes_menores_basicos)
    for complemento in ['7', '9', '11', '7/9', '7/11', '9/11', '7/9/11', '7+', '9+', '11+']
]
todos_os_acordes += [
    acorde + complemento for acorde in acordes_suspensos
    for complemento in ['2', '4', '2+', '4+']
]
todos_os_acordes += [
    acorde + '/' + baixa for acorde in todos_os_acordes
    for baixa in acordes_maiores_basicos if not acorde.endswith('7/9/11') and not baixa.startswith(acorde[0])
]
todos_os_acordes += [acorde + 'º' for acorde in acordes_maiores_basicos]
todos_os_acordes += ['F (sem Pestana)', 'G (com pestana)']
acordes_conhecidos = ['C9', 'B5', 'A9', 'F#m7/11', 'Am7', 'G/B', 'B4(7)', 'D7', 'C7', 'F (sem Pestana)', 'G (com pestana)']
acordes_conhecidos += acordes_maiores_basicos + acordes_menores_basicos
acordes_para_dedilhado = list(rng.permuted([acordes_conhecidos]*90, axis=1)[:, :3])
acordes_para_dedilhado += list(rng.permuted([todos_os_acordes]*120, axis=1)[:, :3])
a = np.array([list('0123')]*30)
sequencias_de_dedilhado = list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
a = np.array([list('01234')]*30)
sequencias_de_dedilhado += list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
a = np.array([list('0123123')]*30)
sequencias_de_dedilhado += list(map(lambda x: '-'.join(list(x)).replace('1-1', '1').replace('2-2', '2').replace('3-3', '3'), rng.permuted(a, axis=1)))
a = np.array([list('012341234')]*30)
sequencias_de_dedilhado += list(map(lambda x: '-'.join(list(x)).replace('1-1', '1').replace('2-2', '2').replace('3-3', '3').replace('4-4', '4'), rng.permuted(a, axis=1)))
a = np.array([['0A', '0B', '1', '2', '3']]*30)
sequencias_de_dedilhado += list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
a = np.array([['0A', '0B', '1', '2', '3', '4']]*30)
sequencias_de_dedilhado += list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
for _ in range(30):
    if np.random.rand() > 0.5:
        seq = ['0A', '0B']
    else:
        seq = ['0']
    seq += ['1', '2', '3']
    if np.random.rand() > 0.5:
        seq += ['4']
    seq1, seq2 = seq.copy(), seq.copy()
    random.shuffle(seq1)
    random.shuffle(seq2)
    seq = list(map(str, zip(seq1, seq2)))
    sequencias_de_dedilhado.append('-'.join(seq))
df = pd.DataFrame(columns=['Exercício', 'Acordes', 'Sequência'])
for i in range(210):
    df = pd.concat([
        df,
        pd.DataFrame.from_records([
            {'Exercício': 'Mobilidade', 'Sequência': exercicios_mobilidade[i]},
            {'Exercício': 'Dedilhado', 'Acordes': acordes_para_dedilhado[i], 'Sequência': sequencias_de_dedilhado[i]},
        ])
    ])
df['Realizado com Sucesso'] = 'Não'
df.to_excel('Exercícios de Violão.xlsx', index=False)
