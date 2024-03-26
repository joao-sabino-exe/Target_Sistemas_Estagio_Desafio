fib_sequence = [0, 1]
n = int(input('Digite um número e descubra se ele faz parte da sequência de Fibonacci: '))

while fib_sequence[-1] < n:
    next_fib = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_fib)

if n in fib_sequence:
    print('{} faz parte da sequência de Fibonacci!'.format(n))
else:
    print('{} não faz parte da sequência de Fibonacci.'.format(n))