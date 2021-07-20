"""
Paths 2

# El objetivo del desafío es que podamos ver el desarrollo de una función. 
# La cual, recibiendo un string para el día y un entero para la cantidad de días anteriores
# devuelva una Lista de elementos que agrupe desde el día pasado como parámetro hasta los n días
# anteriores. Por lo tanto, el objetivo será generar una función Path que devuelva paths 
# para N días corridos.

"""

def generateLastDaysPaths(dia, days):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    dia=datetime.strptime(dia,'%Y%m%d')
    lista_dias = []
    path = 'http://challenge_path_2/'
    dia1=dia-relativedelta(days=days-1)
    lista = [dia1 + relativedelta(days=days) for days in range((dia - dia1).days + 1)]
    for dias in lista:
        lista_dias.append(path+dias.strftime('%Y/%m/%d')+'/')
    
    return lista_dias


generateLastDaysPaths("20210710", 15)

"""
['http://challenge_path_2/2021/06/26/',
 'http://challenge_path_2/2021/06/27/',
 'http://challenge_path_2/2021/06/28/',
 'http://challenge_path_2/2021/06/29/',
 'http://challenge_path_2/2021/06/30/',
 'http://challenge_path_2/2021/07/01/',
 'http://challenge_path_2/2021/07/02/',
 'http://challenge_path_2/2021/07/03/',
 'http://challenge_path_2/2021/07/04/',
 'http://challenge_path_2/2021/07/05/',
 'http://challenge_path_2/2021/07/06/',
 'http://challenge_path_2/2021/07/07/',
 'http://challenge_path_2/2021/07/08/',
 'http://challenge_path_2/2021/07/09/',
 'http://challenge_path_2/2021/07/10/']
 """
