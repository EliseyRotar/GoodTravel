from tabulate import tabulate
import os
pacchetti = [
{'nome':'Parigi', 'prezzo':500, 'inizio':'3/05/2025', 'fine':'10/05/2025', 'posti':10},
{'nome':'Londra', 'prezzo':520, 'inizio':'11/05/2025', 'fine':'16/05/2025', 'posti':2},
{'nome':'Barcellona', 'prezzo':380, 'inizio':'13/06/2025', 'fine':'15/06/2025', 'posti':12},
{'nome':'Amsterdam', 'prezzo':650, 'inizio':'14/04/2025', 'fine':'19/04/2025', 'posti':5},
{'nome':'Amsterdam', 'prezzo':600, 'inizio':'25/05/2025', 'fine':'1/06/2025', 'posti':8}
]

def aggiungi_pacchetto():
    nome=input("Inserisci Il nome della destinazione: ")
    count = 0
    lista = []
    while count<2:
        data=input(f"Inserisci la {count +1} data(gg/mm/aaaa): ")
        if len(data)==10:
            lista.append(data)
        else:
            print("Usa il formato gg/mm/aaaa")
            continue
        count+=1
    lista.sort()
    try:
        prezzo=int(input("Inserisci il prezzo: "))
        posti=int(input("Quanti sono i posti?: "))
    except ValueError:
        print("Dovevi inserire un intero")
    
    pacchetto = {
        'nome':nome,
        'prezzo':prezzo,
        'inizio':lista[0],
        'fine':lista[1],
        'posti':posti
    }
    pacchetti.append(pacchetto)
    visualizza_pacchetto(pacchetto[-1])
    
def modifica_pacchetto():
    visualizza_pacchetti()
    try:
        indice = int(input("Seleziona il numero del pacchetto di cui vuoi modificare il prezzo: ")) - 1
    except ValueError:
        print("Dovevi mettere un intero")
    if  indice>=0 and indice < len(pacchetti):
        try:
            nuovo_prezzo = int(input("Inserisci il nuovo prezzo: "))
        except ValueError:
            print("Dovevi mettere un intero")
        if nuovo_prezzo < 0:
            print("Il prezzo non può essere negativo.")
            return
        pacchetti[indice]['prezzo'] = nuovo_prezzo
        print("Prezzo modificato con successo!")
    else:
        print("Selezione non valida.")
def visualizza_pacchetto(lista,header="keys"):
    print(tabulate(lista,headers=header, tablefmt="pretty"))        

def file_verifica():
    file= open("test.txt","r")
    contenuto=file.read()
    file.close()
    
    lista = contenuto.split(",").lower()
    
    scelta=input("Quale destinazione vuoi verificare sia presente nell'altro file?: ").lower()
    if scelta in lista:
        print("E' Presente!")
    else:
        print("Inesistente")

def pacchetti_destinazione():
    scelta=input("Di quale destinazione vuoi cercare i pacchetti?: ").lower()
    count=0
    lista =[]
    while count<len(pacchetti):
        if scelta== pacchetti[count]['nome'].lower():
            lista.append(pacchetti[count])
        count+=1
    if len(lista)<=0:
        print("Nessun pacchetto con quella destinazione")
    else:
        visualizza_pacchetto(lista)

#scop = in quale parte del codice la variabile puo' essere "vista"
#def controllo_prezzo(lista:list)->bool:    serve per stabilire che il prezzo sia compreso tra 2 valori
    #return not (prezzo < 200 or prezzo > 1000)
#def controllo_data(data:str)-> bool
    #if len(data) != 10:
        #return False
    #if not data[:2].isdecimal():
        #return false
    #if not data[3:5].isdecimal():
        #return false
    #if not data[-4:].isdecimal():
        #return false
    #return True
#def controllo_giorno(giorno:str)->bool:
    #if int(giorno) < 1:
    #   return False
    #if int(giorno) > 31:
    #    return False
    #return True
    

def menu():

    print("1. Visualizza i pacchetti")
    print("2. Aggiungi un pacchetto")
    print("3. Modifica il prezzo di un pacchetto")
    print("4. Cerca pacchetti in base alla destinazione")
    print("5. Verifica pacchetti nei file")
    print("6. Esci")


os.system("cls")
while True:
    
    menu()
    scelta=int(input("Cosa intendi fare?: "))
    if scelta<1 or scelta>6:
        print("Hai sbagliato a inserire l'indice")
    elif scelta==1:
        visualizza_pacchetto(pacchetti)
    elif scelta==2:
        aggiungi_pacchetto()
    elif scelta==3:
        modifica_pacchetto()
    elif scelta==4:
        pacchetti_destinazione()
    elif scelta==5:
        file_verifica()
    elif scelta==6:
        print("Uscita dal programma")
        break
    
    
