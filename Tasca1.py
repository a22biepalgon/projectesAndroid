num_casos = int(input())

for i in num_casos:
    num_linies = int(input())
    v = 300
    p_1 = 0
    p_2 = 0
    for j in num_linies:
        pes1 = int(input())
        pes2 = int(input())
        disminucio = 0
        if pes1 != pes2:
            disminucio = 2
        divisor = (pes1+pes2)//50
        disminucio = disminucio*divisor
        if j >= (num_linies/2):
            p_1 = p_1 + pes1 + pes2
        else:
            p_2 = p_2 + pes1 + pes2
        
        diferencia = p_1 - p_2
        resta = diferencia/100
        subtotal = resta * 5
        total_restar = disminucio + subtotal
        print(v-total_restar)


