#romina_mendoza-22438480
#francisco_gorrin-19606845

print("esta calculadora hace operaciones de suma, resta y multiplicacion")

var1 = int(input("ingrese un numero"))
var2 = input("ingrese operacion a realizar (+,-,*):")
var3 = int(input("ingrese un numero"))

if var2 == "+":
    var4 = (var1 + var3)
    print("el resultado es:",var4)



elif var2 == "-":
    var4 = (var1 - var3)
    print("el resultado es:",var4)

elif var2 == "*":
    var4 = (var1 * var3)
    print("el resultado es:",var4)

else :
        print('esta operacion no puede realizada.')
