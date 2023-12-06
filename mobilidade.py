import numpy as np
rng = np.random.default_rng()
exercicios_mobilidade_basicos = []
while len(exercicios_mobilidade_basicos)<30:
    a = np.array([list('1234')]*(30-len(exercicios_mobilidade_basicos)))
    novos_exercicios = list(map(lambda x: '-'.join(list(x)), rng.permuted(a, axis=1)))
    exercicios_mobilidade_basicos += [ex for ex in novos_exercicios if ex not in exercicios_mobilidade_basicos]
while len(exercicios_mobilidade_basicos)<60:
    a = np.array([list('12341234')]*(60-len(exercicios_mobilidade_basicos)))
    novos_exercicios = list(map(lambda x: '-'.join(list(x)).replace('1-1', '1').replace('2-2', '2').replace('3-3', '3').replace('4-4', '4'), rng.permuted(a, axis=1)))
    exercicios_mobilidade_basicos += [exercicio for exercicio in novos_exercicios if not exercicio.split('-') == exercicio.split('-')[::-1]]
with open('Exercícios de Mobilidade.txt', 'w', encoding='utf-8') as out_file:
    for num_ex, exercicio in enumerate(exercicios_mobilidade_basicos):
        out_file.write(f'\n\nEXERCÍCIO {num_ex}:\n')
        cordas = ['E|-', 'B|-', 'G|-', 'D|-', 'A|-', 'E|-']
        for corda_atual in range(6):
            cordas[corda_atual] += exercicio + '-'
            for outra_corda in range(6):
                if outra_corda != corda_atual:
                    cordas[outra_corda] += '-' * (len(exercicio) + 1)
        for corda in cordas:
            out_file.write(corda + '|\n')