Algoritmo sin_titulo
    Definir cantidad, cantidadBilletes10k, cantidadBilletes20k, cantidadBilletes50k, cantidadBilletes100k, resto como real
    Definir deci Como Caracter
    cantidadBilletes100k <- 0
    cantidadBilletes50k <- 0
    cantidadBilletes20k <- 0
    cantidadBilletes10k <- 0
    Repetir
        Escribir "Desea realizar un retiro (Si/No)"
        Leer deci
        Si deci == "si" Entonces
            Escribir "Valor a retirar: "
            Leer cantidad
            Si cantidad < 10000 O cantidad mod 10000 <> 0 Entonces
                Escribir "Error cantidad no valida"
            Sino
                cantidadBilletes100k <- cantidad / 100000
                resto <- cantidad MOD 100000
                cantidadBilletes50k <- resto / 50000
                resto <- resto MOD 50000
                cantidadBilletes20k <- resto / 20000
                resto <- resto MOD 20000
                cantidadBilletes10k <- resto / 10000
            FinSi
        FinSi
        Escribir trunc(cantidadBilletes100k), " de 100k"
        Escribir trunc(cantidadBilletes50k) , " de 50k"
        Escribir trunc(cantidadBilletes20k), " de 20k"
        Escribir trunc(cantidadBilletes10k), " de 10k"
        cantidadBilletes100k <- 0
        cantidadBilletes50k <- 0
        cantidadBilletes20k <- 0
        cantidadBilletes10k <- 0
    Hasta Que deci == "no"
	
FinAlgoritmo

