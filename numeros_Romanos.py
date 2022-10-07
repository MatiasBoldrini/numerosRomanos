def convertir_a_romanos(numeroNatural):
    numero_Natural = numeroNatural
    numeroRomano = ""
    contador_De_Decenas = numero_Natural // 10 # Obtener cuantas decenas tiene el numero a convertir.

    if contador_De_Decenas >= 10 and contador_De_Decenas < 40:
        numeroRomano += "C" * (contador_De_Decenas // 10)
        numero_Natural -=  100 * (numero_Natural // 100)
        contador_De_Decenas = numero_Natural // 10 
    if contador_De_Decenas == 9: 
        numeroRomano += "XC" 
        numero_Natural -= 90
        contador_De_Decenas = numero_Natural // 10 
    if contador_De_Decenas < 9 and contador_De_Decenas >= 5:
        numeroRomano += "L"
        numero_Natural -=50
        contador_De_Decenas = numero_Natural // 10 
    if contador_De_Decenas == 4: 
        numeroRomano += "XL" 
        numero_Natural -= 40
        numeroRomano
    if contador_De_Decenas >= 1 and contador_De_Decenas <= 3:
        numeroRomano += "X" * contador_De_Decenas
        numero_Natural = numero_Natural - contador_De_Decenas*10 
        numeroRomano
    if numero_Natural == 9: 
        numeroRomano += "IX"
        numero_Natural -= 9
        numeroRomano 
    if numero_Natural < 9 and numero_Natural >= 5:
        numeroRomano += "V"
        numero_Natural -=5
        numeroRomano
    if numero_Natural == 4:
        numeroRomano += "IV" 
        numero_Natural -= 4
        numeroRomano
    if numero_Natural < 4 and numero_Natural >= 1:
        numeroRomano += "I" * numero_Natural
        numeroRomano

    return numeroRomano


