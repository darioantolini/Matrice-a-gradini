def quartotipo(i,j,M): 
    # Scambia i-esima riga con j-esima riga
    c = M[j]
    M[j] = M[i]
    M[i] = c

m = int(input('Inserisci il numero di righe della matrice: '))
n = int(input('Inserisci il numero di colonne della matrice: '))
M = [] 

for j in range(m):
    a = [0 for l in range(n)]
    for i in range(n):
        a[i] = float(input('Inserire il ' + str(i+1) + ' elemento della riga '+ str(j+1)+': \n'))
    print('Fine riga {}\n'.format(j+1))
    M.append(a)

for k in range(m):
    print(M[k])
print('\n')

v = 0
i = 0
j = 0
val = 0

while val < m:
    while v == val:
        while v == val and j < m and i < n:
            if M[j][i] != 0:
                v += 1 
                quartotipo(val,j,M)
            else:
                j+=1
        if v == val:
            i += 1
            j = val
            
    k = val + 1
    
    while k < m:
        if M[k][i] != 0:
            coef = M[k][i] / M[val][i]
            for count in range(n):
                M[k][count] += -coef*M[val][count]
        k+=1
        
    val+=1
    j = val

print('Matrice a gradini: ')

for k in range(m):
    print(M[k])