"""
####   Paths 1   ####

# El objetivo del desafío es que podamos ver el desarrollo de una función. 
# La cual, recibiendo un conjunto de strings devuelva una Lista de elementos 
# que agrupe desde el primer día del mes hasta la fecha ingresada como parámetros inclusive. 
# Por lo tanto, el objetivo será generar una función Path que devuelva paths hasta el día solicitado. 
# El formato de la url es ficticio. Podés usar por ejemplo:
"""
def generateMonthlyPathList(year, month, day):
    
    lista_dias = []
    path = 'http://challenge_path_1/'
    for days in range(1,int(day)+1): # Recorro una lista de los días desde el 1eo al dia indicado mas 1 para incluirlo en el resultado
        lista_dias.append(path+year+'/'+month+'/{:02}/'.format(days))
    return lista_dias

generateMonthlyPathList("2021", "07", "11")
"""
['http://challenge_path_1/2021/07/01/',
 'http://challenge_path_1/2021/07/02/',
 'http://challenge_path_1/2021/07/03/',
 'http://challenge_path_1/2021/07/04/',
 'http://challenge_path_1/2021/07/05/',
 'http://challenge_path_1/2021/07/06/',
 'http://challenge_path_1/2021/07/07/',
 'http://challenge_path_1/2021/07/08/',
 'http://challenge_path_1/2021/07/09/',
 'http://challenge_path_1/2021/07/10/',
 'http://challenge_path_1/2021/07/11/']
"""
