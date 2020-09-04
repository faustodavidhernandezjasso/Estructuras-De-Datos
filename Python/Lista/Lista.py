class Lista :

    class __Nodo :


        def __init__(self, elemento) :
            self.__elemento = elemento
            self.siguiente = None
            self.anterior = None

        @property
        def elemento(self) :
            return self.__elemento


    def __init__(self) :
        self.__cabeza = self.__Nodo(None)
        self.__rabo = self.__Nodo(None)
        self.__elementos = 0
    
    def __len__(self) :
        return self.__elementos

    def __iter__(self) :
        self.siguiente = self.__cabeza
        while (self.siguiente != None) :
            yield self.siguiente.elemento
            self.siguiente = self.siguiente.siguiente

    def get_elementos(self) :
        return self.__elementos
    
    def get_longitud(self) :
        return self.__elementos
    
    def es_vacia(self) :
        return self.__elementos == 0
    
    def agrega(self, elemento) :
        if (elemento == None) :
            raise TypeError
        nuevo = self.__Nodo(elemento)
        if (self.__elementos == 0) :
            self.__cabeza = self.__rabo = nuevo
        else :
            self.__rabo.siguiente = nuevo
            nuevo.anterior = self.__rabo
            self.__rabo = nuevo
        self.__elementos += 1
    
    def agrega_final(self, elemento) :
        if (elemento == None) :
            raise TypeError
        nuevo = self.__Nodo(elemento)
        if (self.__elementos == 0) :
            self.__cabeza = self.__rabo = nuevo
        else :
            self.__rabo.siguiente = nuevo
            nuevo.anterior = self.__rabo
            self.__rabo = nuevo
        self.__elementos += 1
    
    def agrega_inicio(self, elemento) :
        if (elemento == None) :
            raise TypeError
        nuevo = self.__Nodo(elemento)
        if (self.__elementos == 0) :
            self.__cabeza = self.__rabo = nuevo
        else :
            self.__cabeza.anterior = nuevo
            nuevo.siguiente = self.__cabeza
            self.__cabeza = nuevo
        self.__elementos += 1

    def __iesimo_Nodo(self, i) :
        auxiliar = self.__cabeza
        contador = 0
        while (auxiliar != None) :
            if (contador == i) :
                return auxiliar
            contador += 1
            auxiliar = auxiliar.siguiente
        return None

    def inserta(self, i, elemento) :
        if (elemento == None) :
            TypeError
        if (i <= 0) :
            self.agrega_inicio(elemento)
        elif (i >= self.__elementos) :
            self.agrega_final(elemento)
        else :
            nuevo = self.__Nodo(elemento)
            s = self.__iesimo_Nodo(i)
            a = s.anterior
            nuevo.anterior = a
            a.siguiente = nuevo
            nuevo.siguiente = s
            s.anterior = nuevo
            self.__elementos += 1

    def __busca_nodo(self, elemento) :
        auxiliar = self.__cabeza
        while (auxiliar != None) :
            if (auxiliar.elemento == elemento) :
                return auxiliar
            auxiliar = auxiliar.siguiente
        return None
            
    def elimina(self, elemento) :
        if (elemento == None) :
            return 
        eliminar = self.__busca_nodo(elemento)
        if (eliminar == None) :
            return 
        self.__elementos -= 1
        if (self.__elementos == 0) :
            self.__cabeza = self.__rabo = None
        elif (eliminar.anterior == None) :
            s = eliminar.siguiente
            s.anterior = None
            self.__cabeza = s
        elif (eliminar.siguiente == None) :
            a = eliminar.anterior
            a.siguiente = None
            self.__rabo = a
        else :
            a = eliminar.anterior
            s = eliminar.siguiente
            a.siguiente = s
            s.anterior = a
    
    def elimina_primero(self) :
        if (self.__elementos == 0) :
            raise Exception
        elemento_eliminado = self.__cabeza.elemento
        if (self.__elementos == 1) :
            self.__cabeza = self.__rabo = None
        else :
            self.__cabeza = self.__cabeza.siguiente
            self.__cabeza.anterior = None
        self.__elementos -= 1
        return elemento_eliminado
    
    def elimina_ultimo(self) :
        if (self.__elementos == 0) :
            raise Exception
        elemento_eliminado = self.__rabo.elemento
        if (self.__elementos == 1) :
            self.__cabeza = self.__rabo = None
        else :
            self.__rabo = self.__rabo.anterior
            self.__rabo.siguiente = None
        self.__elementos -= 1
        return elemento_eliminado
    
    def contiene(self, elemento) :
        auxiliar = self.__cabeza
        while (auxiliar != None) :
            if (auxiliar.elemento == elemento) :
                return True
            auxiliar = auxiliar.siguiente
        return False

    def reversa(self) :
        lista = Lista()
        if (self.es_vacia()) :
            return lista
        auxiliar = self.__cabeza
        while (auxiliar != None) :
            lista.agrega_inicio(auxiliar.elemento)
            auxiliar = auxiliar.siguiente
        return lista
    
    def copia(self) :
        lista = Lista()
        if (self.es_vacia()) :
            return lista
        auxiliar = self.__cabeza
        while (auxiliar != None) :
            lista.agrega_final(auxiliar.elemento)
            auxiliar = auxiliar.siguiente
        return lista
    
    def limpia(self) :
        self.__cabeza = self.__rabo = None
        self.__elementos = 0
    
    def get_primero(self) :
        if (self.__elementos == 0) :
            raise Exception
        return self.__cabeza.elemento
    
    def get_ultimo(self) :
        if (self.__elementos == 0) :
            raise Exception
        return self.__rabo.elemento
    
    def get(self, i) :
        if (i < 0 or i >= self.__elementos) :
            raise Exception
        contador = 0
        auxiliar = self.__cabeza
        while (auxiliar != None) :
            if (contador == i) :
                return auxiliar.elemento
            auxiliar = auxiliar.siguiente
            contador += 1
    
    def indice_de(self, elemento) :
        contador = 0
        auxiliar = self.__cabeza
        while (auxiliar != None) :
            if (auxiliar.elemento == elemento) :
                return contador
            auxiliar = auxiliar.siguiente
            contador += 1
        return -1
    
    def __str__(self) :
        if (self.__elementos == 0) :
            return "[]"
        else :
            lista = "[{}".format(self.__cabeza.elemento)
            auxiliar = self.__cabeza.siguiente
            while (auxiliar != None) :
                lista += ", {}".format(auxiliar.elemento)
                auxiliar = auxiliar.siguiente
            return lista + "]"

    def __eq__(self, lista) :
        if ((lista == None) or (type(self) != type(lista))) :
            return False
        if (self.__elementos != lista.__elementos ) :
             return False
        nodo = self.__cabeza
        n = lista.__cabeza
        while (nodo != None and n != None) :
            if (nodo.elemento != n.elemento) :
                return False
            nodo = nodo.siguiente
            n = n.siguiente
        return True
