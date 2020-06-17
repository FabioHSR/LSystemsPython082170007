
import turtle
from Gramatica import Gramatica
import canvasvg
import random

regrasDoSistema = {} 


def derivacao(axiom, steps):
    derivado = [axiom]  
    for _ in range(int(steps)):
        proximaSeq = derivado[-1]
        proximoAxioma = [regra(char) for char in proximaSeq]
        derivado.append(''.join(proximoAxioma))
    return derivado


def regra(sequencia):
    if sequencia in regrasDoSistema:
        return regrasDoSistema[sequencia]
    return sequencia 


def desenha(turtle, regrasDoSistema, comprimentoLinha, angulo,alfabeto):
    stack = []
    for command in regrasDoSistema:
        turtle.pd()
        if command in alfabeto: #Faz a flor azul/vermelha
            if command == 'R' and random.randint(1,20) >5:
                 turtle.color('red')
            elif command == 'R' : turtle.color('blue')
            if command == 'B' and random.randint(1,20) >5:
                 turtle.color('blue')
            elif command == 'B' : turtle.color('red')
            turtle.forward(comprimentoLinha)
        elif command == "f":
            turtle.pu()
            turtle.forward(comprimentoLinha)
        elif command == "+":
            turtle.color('#003500') #tons de verde
            turtle.right(float(angulo))
        elif command == "-":
            turtle.color('#005900')
            turtle.left(float(angulo))
        elif command == "[":
            turtle.color('#008000')
            stack.append((turtle.position(), turtle.heading()))
        elif command == "]":
            turtle.pu()
            turtle.color('#58463B')
            position, heading = stack.pop()
            turtle.goto(position)
            turtle.setheading(heading)



def set_turtle(anguloInicial):
    r_turtle = turtle.Turtle()
    r_turtle.screen.title("BlueRedFlower")
    r_turtle.speed(0) #Mais rápido possível
    r_turtle.setheading(anguloInicial)
        
    return r_turtle


def main():
    num_regra = 4
    f = open("Definicoes.txt", "r", encoding='utf-8')
    linhas = f.readlines()
    gramatica = Gramatica(linhas) 

    for regra in gramatica.regras:
        key, value = regra.split("->")
        regrasDoSistema[key.strip()] = value.strip()
        num_regra += 1

    axioma = gramatica.axioma
    iteracoes = gramatica.reps

    modelo = derivacao(axioma, iteracoes)

    comprimentoLinha = 8
    anguloInicial = 60
    angulo = gramatica.angulo

    r_turtle = set_turtle(anguloInicial)
    turtle_screen = turtle.Screen()
    turtle_screen.screensize(2000,2000)

    desenha(r_turtle, modelo[-1], comprimentoLinha, angulo,gramatica.alfabeto)
 
    ts = turtle.getscreen().getcanvas()
    canvasvg.saveall("Imagem.svg",ts,None,10,None)

    turtle_screen.exitonclick()


if __name__ == "__main__":
    main()

