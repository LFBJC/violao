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