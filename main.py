import redis

r = redis.Redis(host='localhost', port=6379)

#-------------------------------FUNCTIONS-------------------------------

def add_word(word,meaning):
  palabra = ({"word":word,"meaning":meaning})
  col.insert_one(palabra)

def change_word(word,new_word):
  col.update_one({"word":word},{"$set": {"word":new_word}})

def delete_word(w):
    col.delete_one({"word":w})

def word_meaning(w):
    pal = col.find_one({"word":w})
    print(pal)
      
#--------------------------------MAIN_APP--------------------------------

print("_________________Diccionario slang panameño_________________")
do{
  print("""
      Elegir una de las siguientes opciones:
         1.- Añadir nueva palabra
         2.- Cambiar palabra existente
         3.- Eliminar palabra del diccionario
         4.- Mostrar todas las palabras con su significado
         5.- Buscar el significado de una palabra
   """)
   num = input()
   if num == 1:
     print("Añadir nueva palabra")
     w = input("nueva palabra: ")
     m = input("nueva palabra: ")
     add_word(w,m)
   elif num == 2:
     print("Cambiar palabra existente")
     w = input("palabra a cambiar: ")
     nw = input("nueva palabra: ")
     change_word(w,nw)
   elif num == 3:
     print("Eliminar palabra del diccionario")
     w = input("Palabra a eliminar: ")
     delete_word(w)
   elif num == 4:
     print("Mostrar todas las palabras con su significado")
     all = col.find({})
     print(all)
   elif num == 5:
     print("Buscar el significado de la siguiente palabra")
     w = input("Palabra: ")
     word_meaning(w)
   elif:
     print("El programa se reiniciara")
}while(num>0);