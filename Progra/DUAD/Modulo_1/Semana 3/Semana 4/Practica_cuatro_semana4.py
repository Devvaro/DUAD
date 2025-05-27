primer_numero = input('Ingrese el primer numero: ')
segundo_numero = input('Ingrese el segundo numero: ')
tercer_numero = input('Ingrese el tercer numero: ')

if(primer_numero > segundo_numero):
    print(f'El valor mas alto es {primer_numero}')

elif(segundo_numero > primer_numero):
    print(f'El valor mas alto es: {segundo_numero}')
    
elif(tercer_numero > primer_numero or segundo_numero):
    print(f'El valor mas alto es: {tercer_numero}')

