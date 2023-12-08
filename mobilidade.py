import random

import numpy as np
from tqdm import tqdm
rng = np.random.default_rng()
exercicios_mobilidade_basicos = []
def replace_nth_occurrence(input_string, char_to_replace, new_char, n):
    # Encontra todas as ocorrências do caractere a ser substituído
    occurrences = [i for i, char in enumerate(input_string) if char == char_to_replace]

    # Verifica se há pelo menos n ocorrências
    if len(occurrences) < n:
        return input_string  # Retorna a string original se não houver n ocorrências

    # Substitui o caractere na posição correspondente à n-ésima ocorrência
    index_to_replace = occurrences[n - 1]
    result_string = input_string[:index_to_replace] + new_char + input_string[index_to_replace + 1:]

    return result_string

def unique(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (str(x) in seen or seen_add(str(x)))]

pbar = tqdm(total=90)
while len(exercicios_mobilidade_basicos)<30:
    a = np.array([list('1234')]*(30-len(exercicios_mobilidade_basicos)))
    novos_exercicios = list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
    novos_exercicios = [ex for ex in novos_exercicios if ex not in exercicios_mobilidade_basicos]
    pbar.update(len(novos_exercicios))
    exercicios_mobilidade_basicos += novos_exercicios
while len(exercicios_mobilidade_basicos)<60:
    a = np.array([list('12341234')]*(60-len(exercicios_mobilidade_basicos)))
    novos_exercicios = list(map(lambda x: '-'.join(list(x)).replace('1-1', '1').replace('2-2', '2').replace('3-3', '3').replace('4-4', '4'), rng.permuted(a, axis=1)))
    novos_exercicios = [exercicio for exercicio in novos_exercicios if not exercicio.split('-') == exercicio.split('-')[::-1] and exercicio not in exercicios_mobilidade_basicos]
    pbar.update(len(novos_exercicios))
    exercicios_mobilidade_basicos += novos_exercicios
while len(exercicios_mobilidade_basicos)<90:
    a = np.array([list('12341234')]*(90-len(exercicios_mobilidade_basicos)))
    novos_exercicios = list(map(lambda x: '-'.join(list(x)).replace('1-1', '1').replace('2-2', '2').replace('3-3', '3').replace('4-4', '4'), rng.permuted(a, axis=1)))
    for indice_ex, exercicio in enumerate(novos_exercicios):
        total_hifens = exercicio.count('-')
        indice_hifen = np.random.randint(total_hifens)
        tecnica_diferenciada = np.random.choice(['/', 'p', '~'])
        novos_exercicios[indice_ex] = replace_nth_occurrence(
            exercicio, '-', tecnica_diferenciada, indice_hifen + 1
        ).replace('4p3', '4t3').replace('4p2', '4t2').replace('4p1', '4t1').replace(
            '3p2', '3t2'
        ).replace('3p1', '3t1').replace('2p1', '2t1')
    novos_exercicios = [ex for ex in novos_exercicios if ex not in exercicios_mobilidade_basicos]
    pbar.update(len(novos_exercicios))
    exercicios_mobilidade_basicos += novos_exercicios
with open('Exercícios de Mobilidade.txt', 'w', encoding='utf-8') as out_file:
    for num_ex, exercicio in enumerate(exercicios_mobilidade_basicos):
        out_file.write(f'\n\nEXERCÍCIO {num_ex + 1}:\n')
        cordas = ['E|-', 'B|-', 'G|-', 'D|-', 'A|-', 'E|-']
        for corda_atual in range(6):
            cordas[corda_atual] += exercicio + '-'
            for outra_corda in range(6):
                if outra_corda != corda_atual:
                    cordas[outra_corda] += '-' * (len(exercicio) + 1)
        for corda in cordas:
            out_file.write(corda + '|\n')
    escalas = {
        # ESCALA MAIOR
        'ESCALA MAIOR': '0-2-4-5-7-9-11', # T T s T T T s
        # ESCALA MENOR
        'ESCALA MENOR NATURAL': '0-2-3-5-7-8-10', # T S T T S T T
        'ESCALA MENOR HARMÔNICA': '0-2-3-5-7-8-11', # T S T T S (T+S) S
        'ESCALA MENOR MELÓDICA': '0-2-3-5-7-9-11', # T S T T T T S
        # ESCALA PENTATÔNICA
        'ESCALA PENTATÔNICA MAIOR': '0-2-4-7-9',
        'ESCALA PENTATÔNICA MENOR': '0-3-5-7-10',
        # ESCALAS GREGAS
        'ESCALA DÓRICA': '0-2-3-5-7-9-10',
        'ESCALA FRÍGIA': '0-1-3-5-7-8-10',
        'ESCALA LÍDIA': '0-2-4-6-7-9-11',
        # ESCALA ÁRABE
        'ESCALA ÁRABE': '0-1-4-5-7-8-11',
        # ESCALA NORDESTINA
        'ESCALA NORDESTINA': '0-2-4-5-7-9-10',
        # ESCALA NONATONICA (USADA EM BLUES)
        'ESCALA NONATONICA': '0-2-3-4-5-7-9-10-11'
    }
    for nome_escala, exemplo_escala in escalas.items():
        escala_como_inteiro = [int(x) for x in exemplo_escala.split('-')]
        out_file.write(("\n" + '-'*50)*2  + "\n")
        out_file.write(f"EXERCÍCIOS BASEADOS NA {nome_escala}\n\n")
        casa_que_define_o_tom = np.random.randint(11) + 1
        escala_como_tuplas = []
        for casa in escala_como_inteiro:
            if casa < 4:
                escala_como_tuplas.append(('E', casa + casa_que_define_o_tom))
                if casa < 2:
                    escala_como_tuplas.append(('D', casa + casa_que_define_o_tom + 2))
                else:
                    escala_como_tuplas.append(('G', casa + casa_que_define_o_tom - 3))
            elif casa < 9:
                escala_como_tuplas.append(('A', casa + casa_que_define_o_tom - 5))
                if casa < 6:
                    escala_como_tuplas.append(('G', casa + casa_que_define_o_tom -3))
                else:
                    escala_como_tuplas.append(('B', casa + casa_que_define_o_tom - 7))
            else:
                escala_como_tuplas.append(('D', casa + casa_que_define_o_tom - 10))
                escala_como_tuplas.append(('B', casa + casa_que_define_o_tom - 7))
        seq_mi = '-'.join(sorted([str(e[1]) for e in escala_como_tuplas if e[0] == 'E'], key=lambda x: int(x)))
        seq_la = '-'.join(sorted([str(e[1]) for e in escala_como_tuplas if e[0] == 'A'], key=lambda x: int(x)))
        seq_re = '-'.join(sorted([str(e[1]) for e in escala_como_tuplas if e[0] == 'D'], key=lambda x: int(x)))
        seq_sol = '-'.join(sorted([str(e[1]) for e in escala_como_tuplas if e[0] == 'G'], key=lambda x: int(x)))
        seq_si = '-'.join(sorted([str(e[1]) for e in escala_como_tuplas if e[0] == 'B'], key=lambda x: int(x)))
        escala_cromatica = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        notas_escala = '-'.join(unique([escala_cromatica[(escala_cromatica.index(e[0]) + e[1]) % len(escala_cromatica)] for e in escala_como_tuplas]))
        out_file.write(f"Escala em tom de {escala_cromatica[(casa_que_define_o_tom-8)%12]}: {notas_escala}\n")
        out_file.write('E|-' + seq_mi + '-'*(len(seq_si) + len(seq_sol) + len(seq_re) + len(seq_la) + len(seq_mi)) + '-|\n')
        out_file.write('B|-' + '-'*len(seq_mi) + seq_si + '-'*(len(seq_sol) + len(seq_re) + len(seq_la) + len(seq_mi)) + '-|\n')
        out_file.write('G|-' + '-'*(len(seq_mi) + len(seq_si)) + seq_sol + '-'*(len(seq_re) + len(seq_la) + len(seq_mi)) + '-|\n')
        out_file.write('D|-' + '-'*(len(seq_mi) + len(seq_si) + len(seq_sol)) + seq_re + '-'*(len(seq_la) + len(seq_mi)) + '-|\n')
        out_file.write('A|-' + '-'*(len(seq_mi) + len(seq_si) + len(seq_sol) + len(seq_re)) + seq_la +  '-'*(len(seq_mi)) + '-|\n')
        out_file.write('E|-' + '-'*(len(seq_si) + len(seq_sol) + len(seq_re) + len(seq_la) + len(seq_mi)) + seq_mi + '-|\n')
        tom_antigo = casa_que_define_o_tom
        casa_que_define_o_tom = np.random.randint(11) + 1
        out_file.write(f'Mudando um pouco a ordem e mudando o tom para {escala_cromatica[(casa_que_define_o_tom-8)%12]}\n')
        escala_como_tuplas = [(e[0], e[1]-tom_antigo+casa_que_define_o_tom) for e in escala_como_tuplas]
        escala_como_tuplas += [('e', e[1]) for e in escala_como_tuplas if e[0] == 'E']
        escala_como_tuplas = unique(escala_como_tuplas)
        cordas = ['e|-','B|-','G|-','D|-','A|-','E|-']
        print('-'*50)
        random.shuffle(escala_como_tuplas)
        # escala_como_tuplas = rng.permuted(escala_como_tuplas, axis=0)
        for corda_escala, casa in escala_como_tuplas:
            print(f"corda: {corda_escala}, casa: {casa}")
            for i in range(len(cordas)):
                if cordas[i].startswith(corda_escala):
                    cordas[i] += str(casa) + '-'
                else:
                    cordas[i] += '-'*(len(str(casa))+1)
        cordas[0] = 'E'+cordas[0][1:]
        for corda in cordas:
            out_file.write(corda+'-|\n')
        tom_antigo = casa_que_define_o_tom
        casa_que_define_o_tom = np.random.randint(11) + 1
        out_file.write(
            f'Agora com mais algumas técnicas e tom de {escala_cromatica[(casa_que_define_o_tom - 8) % 12]}\n'
        )
        escala_como_tuplas = [(e[0], e[1] - tom_antigo + casa_que_define_o_tom) for e in escala_como_tuplas]
        escala_como_tuplas += [('e', e[1]) for e in escala_como_tuplas if e[0] == 'E']
        escala_como_tuplas = unique(escala_como_tuplas)
        random.shuffle(escala_como_tuplas)
        cordas = ['e|-', 'B|-', 'G|-', 'D|-', 'A|-', 'E|-']
        skip = []
        for i, (corda_escala, casa) in enumerate(escala_como_tuplas):
            print(f"corda: {corda_escala}, casa: {casa}")
            if i not in skip:
                if np.random.rand() < 1/4:
                    if i < (len(escala_como_tuplas) + 1) and corda_escala in [escala_como_tuplas[k][0] for k in range(i+1, len(escala_como_tuplas))]:
                        if casa != 0:
                            technique = np.random.choice(['/', 'p', '~'])
                        else:
                            technique = np.random.choice(['/', 'p'])
                        proxima_nota = next(j for j in range(i+1, len(escala_como_tuplas)) if escala_como_tuplas[j][0] == corda_escala)
                        if technique == '~':
                            for j in range(len(cordas)):
                                if cordas[j].startswith(corda_escala):
                                    cordas[j] += str(casa) + '~-'
                                else:
                                    cordas[j] += '-' * (len(str(casa)) + 2)
                        else:
                            if technique == 'p':
                                if escala_como_tuplas[proxima_nota][1] > escala_como_tuplas[i][1]:
                                    technique = 't'
                                elif casa == 0:
                                    technique = 'h'
                            for j in range(len(cordas)):
                                if cordas[j].startswith(corda_escala):
                                    cordas[j] += str(casa) + technique + str(escala_como_tuplas[proxima_nota][1]) + '-'
                                else:
                                    cordas[j] += '-'*(len(str(casa))+2+len(str(escala_como_tuplas[proxima_nota][1])))
                            skip.append(proxima_nota)
                    elif casa != 0:
                        for j in range(len(cordas)):
                            if cordas[j].startswith(corda_escala):
                                cordas[j] += str(casa) + '~-'
                            else:
                                cordas[j] += '-' * (len(str(casa)) + 2)
                else:
                    for j in range(len(cordas)):
                        if cordas[j].startswith(corda_escala):
                            cordas[j] += str(casa) + '-'
                        else:
                            cordas[j] += '-'*(len(str(casa))+1)
        cordas[0] = 'E' + cordas[0][1:]
        for corda in cordas:
            out_file.write(corda + '-|\n')
        tom_antigo = casa_que_define_o_tom
        casa_que_define_o_tom = np.random.randint(11) + 1
        out_file.write(
            f'Por fim com algumas cordas tocadas simultaneamente e tom de {escala_cromatica[(casa_que_define_o_tom - 8) % 12]}\n'
        )
        escala_como_tuplas = [(e[0], e[1] - tom_antigo + casa_que_define_o_tom) for e in escala_como_tuplas]
        escala_como_tuplas += [('e', e[1]) for e in escala_como_tuplas if e[0] == 'E']
        escala_como_tuplas = unique(escala_como_tuplas)
        random.shuffle(escala_como_tuplas)
        cordas = ['e|-', 'B|-', 'G|-', 'D|-', 'A|-', 'E|-']
        skip = []
        for i, (corda_escala, casa) in enumerate(escala_como_tuplas):
            print(f"corda: {corda_escala}, casa: {casa}")
            if i not in skip:
                if np.random.rand() < 1/3 and i < (len(escala_como_tuplas) + 1) and len([k for k in range(i+1, len(escala_como_tuplas)) if escala_como_tuplas[k][0] != corda_escala]):
                    nota_simultanea = next(
                        j for j in range(i + 1, len(escala_como_tuplas)) if escala_como_tuplas[j][0] != corda_escala
                    )
                    for j in range(len(cordas)):
                        if cordas[j].startswith(corda_escala):
                            cordas[j] += str(casa) + '-'
                            if len(str(casa)) < len(str(escala_como_tuplas[nota_simultanea][1])):
                                cordas[j] += '-'*(len(str(escala_como_tuplas[nota_simultanea][1])) - len(str(casa)))
                        elif cordas[j].startswith(escala_como_tuplas[nota_simultanea][0]):
                            cordas[j] += str(escala_como_tuplas[nota_simultanea][1]) + '-'
                            if len(str(casa)) > len(str(escala_como_tuplas[nota_simultanea][1])):
                                cordas[j] += '-' * (len(str(casa)) - len(str(escala_como_tuplas[nota_simultanea][1])))
                        else:
                            cordas[j] += '-'*(max(len(str(casa)), len(str(escala_como_tuplas[nota_simultanea][1])))+1)
                elif np.random.rand() < 1/4:
                    if i < (len(escala_como_tuplas) + 1) and corda_escala in [escala_como_tuplas[k][0] for k in range(i+1, len(escala_como_tuplas))]:
                        if casa != 0:
                            technique = np.random.choice(['/', 'p', '~'])
                        else:
                            technique = np.random.choice(['/', 'p'])
                        proxima_nota = next(j for j in range(i+1, len(escala_como_tuplas)) if escala_como_tuplas[j][0] == corda_escala)
                        if technique == '~':
                            for j in range(len(cordas)):
                                if cordas[j].startswith(corda_escala):
                                    cordas[j] += str(casa) + '~-'
                                else:
                                    cordas[j] += '-' * (len(str(casa)) + 2)
                        else:
                            if technique == 'p':
                                if escala_como_tuplas[proxima_nota][1] > escala_como_tuplas[i][1]:
                                    technique = 't'
                                elif casa == 0:
                                    technique = 'h'
                            for j in range(len(cordas)):
                                if cordas[j].startswith(corda_escala):
                                    cordas[j] += str(casa) + technique + str(escala_como_tuplas[proxima_nota][1]) + '-'
                                else:
                                    cordas[j] += '-'*(len(str(casa))+2+len(str(escala_como_tuplas[proxima_nota][1])))
                            skip.append(proxima_nota)
                    elif casa != 0:
                        for j in range(len(cordas)):
                            if cordas[j].startswith(corda_escala):
                                cordas[j] += str(casa) + '~-'
                            else:
                                cordas[j] += '-' * (len(str(casa)) + 2)
                else:
                    for j in range(len(cordas)):
                        if cordas[j].startswith(corda_escala):
                            cordas[j] += str(casa) + '-'
                        else:
                            cordas[j] += '-'*(len(str(casa))+1)
        cordas[0] = 'E'+cordas[0][1:]
        for corda in cordas:
            out_file.write(corda+'-|\n')
        out_file.write(("\n" + '-' * 50) * 2 + "\n")
