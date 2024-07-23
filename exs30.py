total18 = toth = totm20 = 0
while True:
    idade = int(input("Digite sua idade: "))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input("Digite seu sexo? M/F")).strip().upper()[0]
        if idade > 18:
            total18 += 1
        if sexo == 'M':
            toth += 1
        if sexo == 'F' and idade < 20:
            totm20 +=1

    resp = ' '
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == 'Nn':
         break
    print(f"Acabou! Tem maiores de 18 {total18}, tem {toth} homens, e tem {totm20} pessoas cadastradas. ")

