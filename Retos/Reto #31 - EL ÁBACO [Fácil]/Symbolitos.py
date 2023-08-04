### El ábaco - del revés ###

"""
Hola amigos y amigas, mi alias es Symbolitos, soy nueva en esto de programar.
Este año comenzaré el primer curso de ingeniería informática en la universidad.
Programa realizado por Symbolitos.
Esto me ha salido pero del revés... 

versión 1.0.0

/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
 */
 """

def abaco_counter(text):

    abaco = {"0": "---OOOOOOOOO\n", "1": "O---OOOOOOOO\n", "2": "OO---OOOOOOO\n", "3": "OOO---OOOOOO\n",
            "4": "OOOO---OOOOO\n", "5": "OOOOO---OOOO\n", "6": "OOOOOO---OOO\n", "7": "OOOOOOO---OO\n",
            "8": "OOOOOOOO---O\n", "9": "OOOOOOOOO---\n"}

    abaco_text = ""

    for word in text:
        if word.upper() in abaco.keys():
            abaco_text += abaco[word.upper()]
        else:
            abaco_text += word

    return abaco_text

print(("\n\n Bienvenidos al ábaco de Laura\n"), ("\n Introduzca sus números para obtener las secuencias en el ábaco  \n\n"))
print(abaco_counter(input("Solución en el ábaco de: ")))
