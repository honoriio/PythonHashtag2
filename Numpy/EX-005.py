import numpy as np

salarios = np.array([2500, 3200, 4100, 2900, 3700, 4600, 5200])

media = np.mean(salarios)

funcionario_acima_media = np.where(salarios > media) # podemos usar o where para fazer a filtragem de informações 

print(salarios[salarios > 3000])  # tambem podemos fazer isso, para buscarmos valores diretamente no array de forma facil e simples.



print(np.where(salarios > media, 'acima da media', 'abaixo da media')) 