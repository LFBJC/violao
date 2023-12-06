import pandas as pd
import numpy as np
import random
rng = np.random.default_rng()
def unique(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (str(x) in seen or seen_add(str(x)))]
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
acordes_para_dedilhado = []
while len(acordes_para_dedilhado) < 90:
    acordes_para_dedilhado += unique(list(rng.permuted([acordes_conhecidos]*(90 - len(acordes_para_dedilhado)), axis=1)[:, :3]))
    acordes_para_dedilhado = unique(acordes_para_dedilhado)
while len(acordes_para_dedilhado) < 210:
    acordes_para_dedilhado += unique(list(rng.permuted([todos_os_acordes]*(210 - len(acordes_para_dedilhado)), axis=1)[:, :3]))
    acordes_para_dedilhado = unique(acordes_para_dedilhado)
sequencias_de_dedilhado = []
while len(sequencias_de_dedilhado)<30:
    a = np.array([list('0123')]*(30-len(sequencias_de_dedilhado)))
    sequencias_de_dedilhado += list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
while len(sequencias_de_dedilhado)<60:
    a = np.array([list('01234')]*(60-len(sequencias_de_dedilhado)))
    sequencias_de_dedilhado += list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
while len(sequencias_de_dedilhado)<90:
    a = np.array([list('0123123')]*(90-len(sequencias_de_dedilhado)))
    sequencias_de_dedilhado += list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
while len(sequencias_de_dedilhado)<120:
    a = np.array([list('012341234')]*(120-len(sequencias_de_dedilhado)))
    sequencias_de_dedilhado += list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
while len(sequencias_de_dedilhado)<150:
    a = np.array([['0A', '0B', '1', '2', '3']]*(150-len(sequencias_de_dedilhado)))
    sequencias_de_dedilhado += list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
while len(sequencias_de_dedilhado)<180:
    a = np.array([['0A', '0B', '1', '2', '3', '4']]*(180-len(sequencias_de_dedilhado)))
    sequencias_de_dedilhado += list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
i = 0
while i < 30:
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
    if '-'.join(seq) not in sequencias_de_dedilhado:
        sequencias_de_dedilhado.append('-'.join(seq))
        i+=1
df_dedilhado = pd.DataFrame(columns=['Acordes', 'Sequência'])
for i in range(210):
    df_dedilhado = pd.concat([
        df_dedilhado,
        pd.DataFrame.from_records([
            {'Acordes': acordes_para_dedilhado[i], 'Sequência': sequencias_de_dedilhado[i]},
        ])
    ])
df_dedilhado['Realizado com Sucesso'] = 'Não'
df_dedilhado.to_excel('Exercícios de Dedilhado.xlsx', index=False)
