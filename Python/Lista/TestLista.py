import unittest
from Lista import Lista
import random
import math

class TestLista(unittest.TestCase) :

    def numero_aleatorio(self) :
        return 10 + random.randint(0, 100)

    def setUp(self):
        self.lista = Lista()
        return self.lista
    
    def valida_lista(self, lista) :
        if (not isinstance(lista, Lista)) :
            return
        l = []
        contador = 0
        for elemento in lista :
            l.append(elemento)
            self.assertTrue(l[contador] == lista.get(contador))
            contador += 1
        self.assertTrue(len(lista) == contador)

    def test_constructor(self) :
        self.assertTrue(self.lista != None)
        self.assertTrue(self.lista.es_vacia())
        self.assertTrue(len(self.lista) == 0)
    
    def test_get_longitud(self) :
        self.assertTrue(len(self.lista) == 0)
        i = self.numero_aleatorio()
        contador = 0
        while (contador < (i / 2)) :
            self.lista.agrega_final(random.randint(0, 100))
            contador += 1
            self.assertTrue(len(self.lista) == contador)
        while (contador < i) :
            self.lista.agrega_final(random.randint(0, 100))
            contador += 1
            self.assertTrue(len(self.lista) == contador)
        self.assertTrue(len(self.lista) == contador)
        self.assertFalse(self.lista.es_vacia())
    
    def test_get_elementos(self) :
        self.assertTrue(len(self.lista) == 0)
        self.assertTrue(self.lista.es_vacia())
        i = self.numero_aleatorio()
        contador = 0
        while (contador < (i / 2)) :
            self.lista.agrega_final(random.randint(0, 100))
            contador += 1
            self.assertTrue(len(self.lista) == contador)
        while (contador < i) :
            self.lista.agrega_final(random.randint(0, 100))
            contador += 1
            self.assertTrue(len(self.lista) == contador)
        self.assertTrue(len(self.lista) == contador)
        self.assertFalse(self.lista.es_vacia())
    
    def test_es_vacia(self) :
        self.assertTrue(len(self.lista) == 0)
        self.assertTrue(self.lista.es_vacia())
        self.lista.agrega_final(random.randint(0, 100))
        self.assertFalse(self.lista.es_vacia())
        self.assertFalse(len(self.lista) == 0)
        self.lista.elimina_primero()
        self.assertTrue(self.lista.es_vacia())
        self.assertTrue(len(self.lista) == 0)
    
    def test_agrega(self) :
        with self.assertRaises(TypeError) :
            self.lista.agrega_final(None)
            self.fail()
        self.lista.agrega(random.randint(0, 100))
        n = self.lista.get_primero()
        self.assertEqual(self.lista.get_primero(), n)
        self.valida_lista(self.lista)
        self.lista.agrega_inicio(random.randint(0, 100))
        numero = self.lista.get_primero()
        while (numero == n) :
            numero = random.randint(0, 100)
        self.assertNotEqual(n, numero)
        self.valida_lista(self.lista)
        self.assertNotEqual(self.lista.get_ultimo(), 2)
        i = self.numero_aleatorio()
        contador = 0
        while (contador < i) :
            num = self.numero_aleatorio()
            self.lista.agrega(num)
            self.assertEqual(self.lista.get_ultimo(), num)
            contador += 1
    
    def test_agrega_final(self) :
        with self.assertRaises(TypeError) :
            self.lista.agrega_final(None)
            self.fail()
        numero = self.numero_aleatorio()
        self.lista.agrega_final(numero)
        self.assertEqual(numero, self.lista.get_primero())
        self.valida_lista(self.lista)
        n = self.numero_aleatorio()
        self.lista.agrega_inicio(n)
        self.assertNotEqual(n, self.lista.get_ultimo())
        num = self.numero_aleatorio()
        c = 0
        while (c < num) :
            nuevo_numero = self.numero_aleatorio()
            self.lista.agrega_final(nuevo_numero)
            self.assertEqual(nuevo_numero, self.lista.get_ultimo())
            c += 1
    
    def test_agrega_inicio(self) :
        with self.assertRaises(TypeError) :
            self.lista.agrega_inicio(None)
            self.fail()
        numero = self.numero_aleatorio()
        self.lista.agrega_inicio(numero)
        self.valida_lista(self.lista)
        self.assertEqual(self.lista.get_primero(), numero)
        n = self.numero_aleatorio()
        while (n == numero) :
            n = self.numero_aleatorio()
        self.lista.agrega_final(n)
        self.assertNotEqual(self.lista.get_primero(), n)
        self.valida_lista(self.lista)
        num = self.numero_aleatorio()
        c = 0
        while (c < num) :
            nuevo_numero = self.numero_aleatorio()
            self.lista.agrega_inicio(nuevo_numero)
            self.assertEqual(self.lista.get_primero(), nuevo_numero)
            c += 1
    
    def test_inserta(self) :
        with self.assertRaises(TypeError) :
            self.lista.inserta(self.numero_aleatorio(), None)
            self.fail()
        l = Lista()
        total = self.numero_aleatorio()
        c = 0
        while (c < total) :
            l.agrega_inicio(total + c)
            self.lista.inserta(-1, total + c)
            self.valida_lista(self.lista)
            self.assertEqual(self.lista, l)
            self.assertEqual(self.lista.get_primero(), total + c)
            c += 1
        with self.assertRaises(TypeError) :
            c = -1
            while (c <= total) :
                self.lista.inserta(c, None)
                self.fail()
                c += 1
        self.lista.limpia()
        self.assertTrue(self.lista.es_vacia())
        l.limpia()
        self.assertTrue(l.es_vacia())
        c = 0
        while (c < total) :
            self.lista.inserta(0, total + c)
            l.agrega_inicio(total + c)
            self.valida_lista(self.lista)
            self.assertEqual(self.lista, l)
            self.assertEqual(self.lista.get_primero(), total + c)
            c += 1
        self.lista.limpia()
        self.assertTrue(self.lista.es_vacia())
        l.limpia()
        self.assertTrue(l.es_vacia())
        c = 0
        while (c < total) :
            self.lista.inserta(len(self.lista), total + c)
            l.agrega_final(total + c)
            self.valida_lista(self.lista)
            self.assertEqual(self.lista.get_ultimo(), total + c)
            self.assertEqual(self.lista, l)
            c += 1
        self.lista.limpia()
        self.assertTrue(self.lista.es_vacia())
        l.limpia()
        self.assertTrue(l.es_vacia())
        c = 0
        while (c < total) :
            indice = random.randint(1, total - 2)
            self.lista.limpia()
            self.assertTrue(self.lista.es_vacia())
            l.limpia()
            self.assertTrue(l.es_vacia())
            i = 0
            while (i < total) :
                l.agrega_final(total + i)
                if (i != indice) :
                    self.lista.agrega_final(total + i)
                self.valida_lista(l)
                self.valida_lista(self.lista)
                i += 1
            self.assertEqual(len(l), len(self.lista) + 1)
            self.lista.inserta(indice, total + indice)
            self.valida_lista(self.lista)
            self.assertEqual(self.lista, l)
            c += 1

    def test_elimina(self) :
        self.lista.elimina(None)
        self.assertTrue(self.lista.es_vacia())
        self.assertTrue(len(self.lista) == 0)
        self.lista.elimina(self.numero_aleatorio())
        self.assertTrue(self.lista.es_vacia())
        self.assertTrue(len(self.lista) == 0)
        self.lista.agrega_final(self.numero_aleatorio())
        self.assertFalse(self.lista.es_vacia())
        self.assertFalse(len(self.lista) == 0)
        self.lista.elimina_ultimo()
        self.assertTrue(self.lista.es_vacia())
        i = self.numero_aleatorio()
        c = random.randint(1, i)
        j = 0
        m = 0
        while (j < i) :
            self.lista.agrega_final(c)
            c += 1
            if (j == math.floor(i / 2)) :
                m = c - 1
            j += 1
        p = self.lista.get_primero()
        u = self.lista.get_ultimo()
        self.assertTrue(self.lista.contiene(m))
        self.assertTrue(self.lista.contiene(p))
        self.assertTrue(self.lista.contiene(u))
        self.lista.elimina(p)
        self.valida_lista(self.lista)
        self.assertFalse(self.lista.contiene(p))
        j -= 1
        self.assertTrue(len(self.lista) == j)
        self.lista.elimina(u)
        self.valida_lista(self.lista)
        self.assertFalse(self.lista.contiene(u))
        j -= 1
        self.assertTrue(len(self.lista) == j)
        self.lista.elimina(m)
        self.valida_lista(self.lista)
        self.assertFalse(self.lista.contiene(m))
        j -= 1
        self.assertTrue(len(self.lista) == j)
        while (not (self.lista.es_vacia())) :
            self.lista.elimina(self.lista.get_primero())
            j -= 1
            self.assertTrue(len(self.lista) == j)
            if (self.lista.es_vacia()) :
                continue
            self.lista.elimina(self.lista.get_ultimo())
            j -= 1
            self.assertTrue(len(self.lista) == j)
        with self.assertRaises(Exception) :
            self.lista.get_primero()
            self.fail()
        with self.assertRaises(Exception) :
            self.lista.get_ultimo()
            self.fail()
        i = self.numero_aleatorio()
        j = self.numero_aleatorio()
        k = self.numero_aleatorio()
        self.lista.agrega_final(i)
        self.lista.agrega_final(j)
        self.lista.agrega_final(k)
        self.lista.agrega_final(j)
        self.assertTrue(self.lista.contiene(i))
        self.assertTrue(self.lista.contiene(j))
        self.assertTrue(self.lista.contiene(k))
        self.lista.elimina(j)
        self.assertEqual(self.lista.get(0), i)
        self.assertEqual(self.lista.get(1), k)
        self.assertEqual(self.lista.get(2), j)
        self.lista.elimina(j)
        self.assertFalse(self.lista.contiene(j))
        self.assertEqual(self.lista.get(0), i)
        self.assertEqual(self.lista.get(1), k)

    def test_elimina_primero(self) :
        with self.assertRaises(Exception) :
            self.lista.elimina_primero(1)
            self.fail()
        l = []
        i = self.numero_aleatorio()
        c = 0
        while (c < i) :
            nuevo_numero = self.numero_aleatorio()
            self.lista.agrega_final(nuevo_numero)
            l.append(nuevo_numero)
            c += 1
        self.assertTrue(len(self.lista) == c)
        self.assertFalse(self.lista.es_vacia())
        indice = 0
        while (not (self.lista.es_vacia())) :
            elemento_eliminado = self.lista.elimina_primero()
            self.assertEqual(elemento_eliminado, l[indice])
            c -= 1
            indice += 1
            self.assertTrue(len(self.lista) == c)
        with self.assertRaises(Exception) :
            self.lista.elimina_primero()
            self.fail()
    
    def test_elimina_ultimo(self) :
        with self.assertRaises(Exception) :
            self.lista.elimina_ultimo()
            self.fail()
        self.assertTrue(len(self.lista) == 0)
        self.assertTrue(self.lista.es_vacia())
        l = []
        i = self.numero_aleatorio()
        c = 0
        while (c < i) :
            nuevo_numero = self.numero_aleatorio()
            self.lista.agrega_final(nuevo_numero)
            l.append(nuevo_numero)
            c += 1
        self.assertTrue(len(self.lista) == c)
        while (not (self.lista.es_vacia())) :
            elemento_eliminado = self.lista.elimina_ultimo()
            c -= 1
            self.assertEqual(elemento_eliminado, l[c])
            self.assertTrue(len(self.lista) == c)
        with self.assertRaises(Exception) :
            self.lista.elimina_ultimo()
            self.fail()

    def test_contiene(self) :
        self.assertTrue(self.lista.es_vacia())
        numero = self.numero_aleatorio()
        self.assertFalse(self.lista.contiene(numero))
        self.lista.agrega_final(numero)
        self.assertTrue(self.lista.contiene(numero))
        i = self.numero_aleatorio()
        c = 0
        while (c < i) :
            numero_nuevo = self.numero_aleatorio()
            self.lista.agrega_final(numero_nuevo)
            self.assertTrue(self.lista.contiene(numero_nuevo))
            c += 1
        m = self.lista.get(random.randint(0, len(self.lista) - 1))
        self.assertTrue(self.lista.contiene(m))
    
    def test_reversa(self) :
        reversa = self.lista.reversa()
        self.assertTrue(reversa.es_vacia())
        self.assertTrue(len(self.lista) == len(reversa))
        self.assertIsNot(self.lista, reversa)
        i = self.numero_aleatorio()
        c = 0
        while (c < i) :
            self.lista.agrega_final(self.numero_aleatorio())
            c += 1
        reversa = self.lista.reversa()
        self.valida_lista(reversa)
        self.assertTrue(len(self.lista) == len(reversa))
        self.assertIsNot(self.lista, reversa)
        while (not (reversa.es_vacia())) :
            elemento = reversa.elimina_ultimo()
            e = self.lista.elimina_primero()
            self.assertEqual(elemento, e)
        self.assertTrue(len(self.lista) == len(reversa))
        self.assertTrue(self.lista.es_vacia() and reversa.es_vacia())
        
    def test_copia(self) :
        copia = self.lista.copia()
        self.assertTrue(copia.es_vacia())
        self.assertTrue(len(self.lista) == len(copia))
        self.assertIsNot(self.lista, copia)
        i = self.numero_aleatorio()
        c = 0
        while (c < i) :
            self.lista.agrega_final(self.numero_aleatorio())
            c += 1
        copia = self.lista.copia()
        self.valida_lista(copia)
        self.assertTrue(len(self.lista) == len(copia))
        self.assertIsNot(self.lista, copia)
        while (not (copia.es_vacia())) :
            elemento = copia.elimina_primero()
            e = self.lista.elimina_primero()
            self.assertEqual(elemento, e)
        self.assertTrue(len(self.lista) == len(copia))
        self.assertTrue(self.lista.es_vacia() and copia.es_vacia())
    
    def test_limpia(self) :
        self.assertTrue(self.lista.es_vacia())
        primero = self.numero_aleatorio()
        self.lista.agrega_final(primero)
        self.assertFalse(self.lista.es_vacia())
        i = self.numero_aleatorio()
        c = 0
        while (c < i) :
            self.lista.agrega_final(self.numero_aleatorio())
            c += 1
        self.assertFalse(self.lista.es_vacia())
        self.assertTrue(len(self.lista) != 0)
        ultimo = self.numero_aleatorio()
        self.lista.agrega_final(ultimo)
        self.assertEqual(self.lista.get_primero(), primero)
        self.assertEqual(self.lista.get_ultimo(), ultimo)
        self.assertFalse(self.lista.es_vacia())
        self.lista.limpia()
        self.assertTrue(len(self.lista) == 0)
        self.assertTrue(self.lista.es_vacia())
    
    def test_get_primero(self) :
        with self.assertRaises(Exception) :
            self.lista.get_primero()
            self.fail()
        self.assertTrue(self.lista.es_vacia())
        i = self.numero_aleatorio()
        c = 0
        while (c < i) :
            elemento = self.numero_aleatorio()
            self.lista.agrega_inicio(elemento)
            self.assertEqual(elemento, self.lista.get_primero())
            c += 1
            self.assertTrue(len(self.lista) == c)
        self.assertFalse(self.lista.es_vacia())
        self.assertTrue(len(self.lista) == c)
    
    def test_get_ultimo(self) :
        with self.assertRaises(Exception) :
            self.lista.get_ultimo()
            self.fail()
        self.assertTrue(self.lista.es_vacia())
        i = self.numero_aleatorio()
        c = 0
        while (c < i) :
            elemento = self.numero_aleatorio()
            self.lista.agrega_final(elemento)
            self.assertEqual(self.lista.get_ultimo(), elemento)
            c += 1
            self.assertTrue(len(self.lista) == c)
        self.assertFalse(self.lista.es_vacia())
        self.assertTrue(len(self.lista) == c)
    
    def test_get(self) :
        self.assertTrue(self.lista.es_vacia())
        l = []
        i = self.numero_aleatorio()
        c = 0
        while (c < i) :
            nuevo_numero = self.numero_aleatorio()
            l.append(nuevo_numero)
            self.lista.agrega_final(nuevo_numero)
            self.assertEqual(self.lista.get(c), l[c])
            c += 1
        with self.assertRaises(Exception) :
            self.lista.get(-1)
            self.fail()
        with self.assertRaises(Exception) :
            self.lista.get(-10)
            self.fail()
        with self.assertRaises(Exception) :
            self.lista.get(len(self.lista))
            self.fail()
        with self.assertRaises(Exception) :
            self.lista.get(len(self.lista) * 15)
            self.fail()
    
    def test_indice_de(self) :
        self.assertTrue(self.lista.es_vacia())
        numero = self.numero_aleatorio()
        self.assertTrue(self.lista.indice_de(numero) == -1)
        i = self.numero_aleatorio()
        c = 0
        while (c < i) :
            nuevo_numero = i + c
            self.lista.agrega_final(nuevo_numero)
            self.assertEqual(self.lista.indice_de(nuevo_numero), c)
            c += 1
            self.assertTrue(len(self.lista) == c)
        self.assertTrue(len(self.lista) == c)

    def test_str(self) :
        self.assertEqual(self.lista.__str__(), "[]")
        l = []
        i = self.numero_aleatorio()
        c = 0
        while (c < i) :
            nuevo_numero = self.numero_aleatorio()
            l.append(nuevo_numero)
            self.lista.agrega_final(nuevo_numero)
            c += 1
        cadena = "["
        c = 0
        while (c < len(l) - 1) :
            cadena += str(l[c]) + ", "
            c += 1
        cadena += str(l[c]) + "]"
        self.assertEqual(cadena, self.lista.__str__())
    
    def test_eq(self) :
        self.assertNotEqual(self.lista, None)
        l = Lista()
        self.assertEqual(self.lista, l)
        i = self.numero_aleatorio()
        c = 0
        while (c < i) :
            nuevo_numero = self.numero_aleatorio()
            l.agrega_final(nuevo_numero)
            self.lista.agrega_final(nuevo_numero)
            c += 1
        self.assertEqual(self.lista, l)
        ultimo = l.elimina_ultimo()
        self.assertNotEqual(self.lista, l)
        self.lista.agrega_final(ultimo)
        self.assertNotEqual(self.lista, l)
        self.assertNotEqual(self.lista, None)


if (__name__ == "__main__") :
    unittest.main()