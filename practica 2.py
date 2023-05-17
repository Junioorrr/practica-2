print("calculadora basica")
print("utilizamos while para evaluar la condicion,si la condiocion es verdadera se ejecutara ,si la condicon se sigue cumplioendo se repite este proceso , si es falsa el terminara ")

variable_1 = (input("ingresa el primer numero:"))
variable_2 = (input("ingresa el segundo numero:"))

if variable_1.isnumeric() and variable_2.isnumeric():
    variable_1 = int(variable_1)
    variable_2 = int(variable_2)
else:
    raise ValueError("error por favor ingresa otro numero")

opcion_1 = 0

while opcion_1 !=4:
    print("""     
    selecione la operacion que desea realizar que esten en la pantalla 
    1)suma 
    2)resta
    3)multiplicacion
    4)divicion
    """  )

    opcion_1 = int(input())

    if opcion_1 == 1:
        print(" ")
        print("el resultado de la suma es:", variable_1, "+", variable_2,"=",variable_1 + variable_2)

    elif opcion_1 == 2:
         print(" ")
         print("el resultado de la resta es:", variable_1, "-", variable_2, "=", variable_1 - variable_2)

    elif opcion_1 == 3:
        print(" ")
        print("el resultado de la multiplicacion es:", variable_1, "*", variable_2, "=", variable_1 * variable_2)

    elif opcion_1 == 4:
         if variable_2 > 0:
            print(" ")
            print("el resultado de la divicion es:", variable_1, "/", variable_2, "=", variable_1 / variable_2)
         else:
             raise ZeroDivisionError ("no se puede dividir entre cero, ingresa otro numero")
         





