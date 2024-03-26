maximo = 10
contador_a = 0
contador_b = 0
contador_c = 0
contador_d = 0
cont_vlr_d = 12
contador_e = 0

a = [1]
b = [2]
c = [0, 1]
c1 = [0, 1]
d = [4, 16]
e = [0, 1]

while contador_a < maximo:
    contador_a = contador_a + 1
    vlr_a = a[-1] + 2
    a.append(vlr_a)

while contador_b < maximo:
    contador_b = contador_b + 1
    vlr_b = b[-1] * 2
    b.append(vlr_b)

while contador_c < maximo:
    contador_c = contador_c + 1
    vlr_c = c1[-1] + 2
    vlr_c2 = c[-1] + vlr_c
    c.append(vlr_c2)
    c1.append(vlr_c)

while contador_d < maximo:
    contador_d = contador_d + 1
    cont_vlr_d = cont_vlr_d + 8
    vlr_d = d[-1] + cont_vlr_d
    d.append(vlr_d)

while len(e) < maximo:
    contador_e = contador_e + 1
    next_fib = e[-1] + e[-2]
    e.append(next_fib)
    

print('Logica A: {}'.format(a))
print('Logica B: {}'.format(b))
print('Logica C: {}'.format(c))
print('Logica D: {}'.format(d))
print('Logica E: {}'.format(e))
print('Logica F: [2, 10, 12, 16, 17, 18, 19, 27, 29, 33]')