import movimento
import generatoresimboli
import posizione



"""
In questa classe andro a definire la rappresentazione sotto forma di dizionario per la definizione dei
simboli della danza
"""
class NotazioneLaban(object):


     generatore=generatoresimboli.GeneratoreSimboli

     def __init__(self):
         self.notazione={} #dizionario di output
         #self.movimento=movimento



     #da ultimare domani prova ad accedere ad un singolo moviment con gli indici e ricavarne il nome
     #poi prova ad elimanare le righe in fondo dove generi i dimboli perche tanto li richiami in tale metodo
     def costruisciNotazione(self,listamovimenti):
          danza= input("inserisci danza per la notazione")
          listasimboli=[]
          listasimboli.append(generatore.generaSimboli(listamovimenti))
          pos=0
          while pos<len(listamovimenti):
              self.notazione.update({ danza : listasimboli})
              pos+=1
          return self.notazione






#definendo il planning a mano ne ricavo tale procedura per creare i simboli
posizionepartenza=posizione.Posizione(3,4,5) #posizione da impiedi del robot,immagino che il robot sia in posizione in piedi nel mio asse
print("definisco il primo movimento e comincio a costruirlo")
movimento1 = movimento.Movimento("Sit",1,posizionepartenza,[]) #il numero indica la durata del movimento e la lista vuota le partidelcorpo impiegate
print(movimento1.get_Nome())
print(movimento1.getPosizionepartenza(posizionepartenza))
listaposizioni= movimento1.costruiscidanza()
listamovimenti=[] #la lista dei movimenti della danza che verra passata in tutti i metodi delle varie classi impiegate
#print(listamovimenti) # stampo la lista per controllare che il movimento sia stato aggiunto
print("passo al secondo movimento e lo costruisco")
movimento2= movimento.Movimento("RaggiungiPosizioneCrouch",1,movimento1.ricavaUltimaPosizione(),[])
print(movimento2.get_Nome())
print(movimento2.costruiscidanza())
print("Stampo i movimenti della danza costruita a runtime comprensivi di posizioni durata e partidel corpo coinvolte")
listamovimenti.append(movimento1.getDescrizione())
listamovimenti.append(movimento2.getDescrizione()) #me li salva come lista di tuple
print(listamovimenti)#ora  dovrei avere la lista dei due movimenti della danza con i due movimenti interessati
print("creo i simboli")
generatore= generatoresimboli.GeneratoreSimboli()
#print(generatore.generaSimboli(listamovimenti))#ùdefinisco l'istanza per creare il generatore di simboli
#genero la notazione per i primi movimenti
print("genero la notazione")
notazione= NotazioneLaban()
print(notazione.costruisciNotazione(listamovimenti))












