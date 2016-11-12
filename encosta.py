# -*- coding: utf-8 -*-
import caixeiro
import sys
import random
import time
import timeit

def variacao1(entrada):
    instance = caixeiro.TSP(entrada)
    tam = len(instance.points)
    current_state = (range(tam), instance.tour_cost(range(tam)))
    while True:
        temp = current_state
        neig = instance.neighbors(current_state[0])
        for i in neig:
            if i[1] < current_state[1]:
                current_state = i
                break
        if temp == current_state:
            break
    return current_state

def variacao2(entrada):
    instance = caixeiro.TSP(entrada)
    tam = len(instance.points)
    current_state = (range(tam), instance.tour_cost(range(tam)))
    while True:
        temp = current_state
        neig = instance.neighbors(current_state[0])
        random.shuffle(neig)
        for i in neig:
            if i[1] < current_state[1]:
                current_state = i
                break
        if temp == current_state:
            break
    return current_state

def variacao3(entrada):
    instance = caixeiro.TSP(entrada)
    tam = len(instance.points)
    current_state = (range(tam), instance.tour_cost(range(tam)))
    while True:
        temp = current_state
        neig = instance.neighbors(current_state[0], 'op2')
        for i in neig:
            if i[1] < current_state[1]:
                current_state = i
                break
        if temp == current_state:
            break
    return current_state

def variacao4(entrada):
    instance = caixeiro.TSP(entrada)
    tam = len(instance.points)
    current_state = (range(tam), instance.tour_cost(range(tam)))
    while True:
        temp = current_state
        neig = instance.neighbors(current_state[0], 'op2')
        random.shuffle(neig)
        for i in neig:
            if i[1] < current_state[1]:
                current_state = i
                break
        if temp == current_state:
            break
    return current_state

def variacao5(entrada):
    instance = caixeiro.TSP(entrada)
    tam = len(instance.points)
    current_state = (range(tam), instance.tour_cost(range(tam)))
    random.shuffle(current_state[0])
    while True:
        temp = current_state
        neig = instance.neighbors(current_state[0])
        for i in neig:
            if i[1] < current_state[1]:
                current_state = i
                break
        if temp == current_state:
            break
    return current_state

def variacao6(entrada):
    instance = caixeiro.TSP(entrada)
    tam = len(instance.points)
    current_state = (range(tam), instance.tour_cost(range(tam)))
    random.shuffle(current_state[0])
    while True:
        temp = current_state
        neig = instance.neighbors(current_state[0])
        random.shuffle(neig)
        for i in neig:
            if i[1] < current_state[1]:
                current_state = i
                break
        if temp == current_state:
            break
    return current_state

def variacao7(entrada):
    instance = caixeiro.TSP(entrada)
    tam = len(instance.points)
    current_state = (range(tam), instance.tour_cost(range(tam)))
    random.shuffle(current_state[0])
    while True:
        temp = current_state
        neig = instance.neighbors(current_state[0], 'op2')
        for i in neig:
            if i[1] < current_state[1]:
                current_state = i
                break
        if temp == current_state:
            break
    return current_state

def variacao8(entrada):
    instance = caixeiro.TSP(entrada)
    tam = len(instance.points)
    current_state = (range(tam), instance.tour_cost(range(tam)))
    random.shuffle(current_state[0])
    while True:
        temp = current_state
        neig = instance.neighbors(current_state[0], 'op2')
        random.shuffle(neig)
        for i in neig:
            if i[1] < current_state[1]:
                current_state = i
                break
        if temp == current_state:
            break
    return current_state

variacao = [variacao1, variacao2, variacao3, variacao4,
     variacao5, variacao6, variacao7,variacao8]

def trescasas(n, casas=2):
    return int(n*(10**casas))/(10.0**casas)

def main(entrada):
#       print variacao1(entrada)
#       print variacao2(entrada)
#       print variacao3(entrada)
#       print variacao4(entrada)
#       print variacao5(entrada)
#       print variacao6(entrada)
#       print variacao7(entrada)
#       print variacao8(entrada)

#
    inicio = timeit.default_timer()
    tabela = []
    for v in variacao:
        linha = [v(entrada)[1] for i in xrange(20)]
        tabela.append(linha)

    for i in tabela:
    #  print i
      print map(lambda x: trescasas(x, 3), i)
    fim = timeit.default_timer()
    print ('duracao: %f' % (fim - inicio))


if __name__ == '__main__':
    main(sys.argv[1])



