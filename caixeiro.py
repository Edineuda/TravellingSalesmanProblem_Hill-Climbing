# -*- coding: utf-8 -*-

class TSP:
    def __init__(self, entrada):
        f = open(entrada) #entrada é o nome do arquivo
        data = f.readlines()
# Criando uma lista de tuplas, 1° uma lista do 'x', 1° lista, transforma todos os elementos no float. Depois no 'y'.
# Tem-se uma lista de pontos

        xl, yl = map(float, data[0].split()), map(float, data[1].split())
        self.points = [(xl[i], yl[i]) for i in range(len(xl))]
 # Fechando o arquivo, é importate.
        f.close()
    def distance(self, i, j):
        dx = self.points[i][0] - self.points[j][0]
        dy = self.points[i][1] - self.points[j][1]
        return (dx**2 +dy**2)**(1/2.0)
    def tour_cost(self, tour):
        #tour = [0, 3, 1, 4, 2, 5]
        #       [5, 3, 1, 4, 2, 0]
        #       [0, 1, 3, 4, 2, 5]
        soma = 0
        i = 0 
        tam = len(tour)
        for i in xrange(tam):
            soma += self.distance(tour[i], tour[(i+1) % tam])
        return soma
# Inverte dois elementos numa lista.    

    def operator1(self, l, a, b):
# Pegando uma cópia da lista recebida por argumento. Porque senão o opetador1 vai mudar os elementos inplace. Tem que pegar a cópia.

        lista = l[:]
        lista[a], lista[b] = lista[b], lista[a]
        return lista
#Pega uma faixa de A a B e inverte somente ela.

    def operator2(self, l, a, b):
        temp = l[a:b+1]#Pegando o proximo.
        temp.reverse()
        return l[0:a] + temp + l[b+1:]


#def subidaencosta():
#		iteracoes = 0
#		valor = sys.maxint
#		while (valor > 26000):
#			solucaoInicial()
#			cont = 0
#			while (cont < 50000):
#				valor = funcaoObjetivo()
#				swap()
#				novoValor = funcaoObjetivo()
#				if (novoValor > valor):
#					volta()
#				cont++
#			iteracoes++

#		print funcaoObjetivo()
#		mostrarTour()
#	def solucaoInicial():
#		for i in range(tam):
#			tour[i] = i


# Do 0 até o A sem incluí-lo, concatenado com o temp que foi revertido, e do B+1 até o final.
 
    def neighbors(self, tour, operation='op1'): #Pega um circuito hamiltoniano, aplica o operador para todas as possibilidades de A e B.
        n = []
        tam = len(tour)
        for i in xrange(tam):
            for j in xrange(i + 1, tam):
                if operation == 'op1':
                    neig = self.operator1(tour, i, j)
                else:
                    neig = self.operator2(tour, i, j)
                n.append(tuple([neig, self.tour_cost(neig)])) # Recebendo o caminho e o custo.
        
        return n



