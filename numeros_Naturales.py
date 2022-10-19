def convertir_a_naturales(numeroRomano): 
    numeroNatural = 0
    orden_numeros_romanos = ["C", "L", "X", "V", "I"]
    lastchar = orden_numeros_romanos[0]
    for char in numeroRomano:
        if lastchar == char or orden_numeros_romanos.index(char) > orden_numeros_romanos.index(lastchar):
            if char == "C":
                numeroNatural += 100
            if char == "L":
                numeroNatural += 50
            if char == "X":
                numeroNatural += 10
            if char == "V":
                numeroNatural += 5
            if char == "I":
                numeroNatural += 1
        else: 
            if char == "C" and lastchar == "X":
                numeroNatural += 80
            if char == "L" and lastchar == "X":
                numeroNatural += 30
            if char == "X" and lastchar == "I":
                numeroNatural += 8
            if char == "V" and lastchar == "I":
                numeroNatural += 3
        lastchar = char
    
    return numeroNatural
    
    

        
