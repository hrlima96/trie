class Trie:
    
    palavras = []
    
    def __str__(self):
        return str(self.palavras)
    
    def incluir(self, palavra):
        if len(self.palavras) == 0:
            self.palavras.append(palavra)
            self.palavras.append([])
            return
        else:
            for i in range(len(palavra)):
                if palavra[:i] in self.palavras:
                    self.palavras[self.palavras.index(palavra[:i]) + 1].append(palavra[i:])
                    return
                        
            for x in range(len(self.palavras)):
                for i in range(len(self.palavras[x])):
                    if palavra == self.palavras[x][:i]:
                        self.palavras.insert(x, palavra)
                        aux = self.palavras.pop(x + 1)[i:]
                        for j in range(len(self.palavras[x + 1])):
                            aux2 = self.palavras[x + 1].pop(j)
                            self.palavras[x + 1].insert(j, aux + aux2)
                        self.palavras[x + 1].append(aux)
                        return

        self.palavras.append(palavra)
        self.palavras.append([])

    def busca(self, palavra):
        for i in range(len(palavra) + 1): #percorre a palavra
            for j in range(len(self.palavras)): #percorre a lista
                if palavra[:i] == self.palavras[j]: #compara o pedaco da palavra com a palavra da lista
                    aux = palavra[:i] #atribui o pedaco da palavra a uma variavel
                    if palavra == self.palavras[j]:
                        print palavra
                    for x in range(len(self.palavras[j + 1])): #percorre o array referente ao pedaco da palavra
                        if palavra[i:] in self.palavras[j + 1][x]:
                            print aux + self.palavras[j + 1][x]




x = Trie()
x.incluir("Pato")
print x
x.incluir("Patota")
print x
x.incluir("Patotinha")
print x
x.incluir("Pa")
print x
x.incluir("Hugo")
print x
x.incluir("Hu")
print x
x.busca("Hu")
x.busca("Pato")