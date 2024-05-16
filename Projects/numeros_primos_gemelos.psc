Funcion primos <- prim ( num )
	definir primos, count Como Entero
	count <- 0
	para i<- 1 hasta num con paso 1 Hacer
		si num mod i == 0 Entonces
			count <- count + 1
		FinSi
	FinPara
	si count == 2 Entonces
		escribir "si es primo"
		primos <- num
	FinSi
Fin Funcion

Algoritmo sin_titulo
	definir num1, num2, count, temp Como Entero
	definir deci Como Caracter
	Repetir
		escribir "desea saber si dos numeros primos son gemelos (si/no)"
		leer deci
		si deci == "si" Entonces
			escribir "escriba el primer numero"
			leer num1
			escribir "escriba el segundo numero"
			leer num2
			si prim(num1) + 2 <> prim(num2) Entonces
				Escribir "no gemelos"
			SiNo
				escribir "si son"
			FinSi
			
		FinSi
	Hasta Que deci == "no"
FinAlgoritmo
