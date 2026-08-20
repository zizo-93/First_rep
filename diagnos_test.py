
print('Hej och välkommen till multiplikationsbyggaren')
rader = int(input('Mata ett heltal som skall representera antalet rader i tabellen: '))
kolumer = int(input('Mata ett tillhel tal som skall representera antalet kolumer i tabellen: '))
for rad in range(1,rader+1):
    for kol in range(1,kolumer +1):
        print(rad * kol, end='\t')
    print()
    


