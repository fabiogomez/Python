
PESOS = []
VALORES = []
def morral(tamano_morral, n):
    
    if n == 0 or tamano_morral == 0:
        return 0
    
    if PESOS[n - 1] > tamano_morral:
        return morral(tamano_morral, n - 1)

    return max(VALORES[n - 1] + morral(tamano_morral - PESOS[n - 1], n - 1),
                morral(tamano_morral, n - 1))


if __name__ == '__main__':
    VALORES = [100 ,60 , 120]
    PESOS = [20, 10, 30]
    tamano_morral = 50
    n = len(VALORES)

    resultado = morral(tamano_morral, n)
    print(resultado)
"""
n = 3
tamaño = 50
peso = 30

120 + 
    (
        tamañomorral = 20
        n=2
        pesos[1] = 10
        valores[1] = 60
        60 + 
        (
            tamañomorral = 10
            n=1
            pesos[0] = 20
            return (
                tamañomorral = 10
                n=0
                return 0
            )=> 0
            
        )=> 0
        (
            tamañomorral = 20
            n=1
            pesos[0] = 20
            valores[1] = 100
            100 + 
            (
                tamañomorral = 0
                n=0
                return 0


            )=> 0
            (
                tamañomorral = 20
                n=0
                return 0

            )=> 0
        )=> 100
        




    )

    (
        tamañomorral = 50
        n=2
        pesos[1] = 10

        


    )





"""
