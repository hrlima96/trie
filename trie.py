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
            for i in range(len(palavra) - 1):
                if palavra[:i] in self.palavras:
                    self.palavras[self.palavras.index(palavra[:i]) + 1].append(palavra[i:])
                    return
                        
            for x in range(len(self.palavras)):
                for i in range(len(self.palavras[x])):
                    if palavra == self.palavras[x][:i]:
                        self.palavras.insert(x, palavra)
                        aux = self.palavras.pop(x + 1)[i:]
                        print aux
                        for j in range(len(self.palavras[x + 1])):
                            aux2 = self.palavras[x + 1].pop(j)
                            self.palavras[x + 1].insert(j, aux + aux2)
                        self.palavras[x + 1].append(aux)
                        return

        self.palavras.append(palavra)
        self.palavras.append([])





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