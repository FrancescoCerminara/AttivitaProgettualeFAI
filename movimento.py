import posizione


#classe per costruire i movimenti che andrà ad eseguire il robot durante la danza

class Movimento(object):




    def __init__(self, nome,durata,posizionepartenza,partidelcorpo):
        self.nome = nome
        self.posizioni =[]
        self.direzione = []
        self.durata = durata
        self.posizionepartenza=posizionepartenza
        self.partidelcorpo=partidelcorpo
        self.listasimboli=[]

    def get_Nome(self):
        return self.nome

    def set_Nome(self,nome):
        self.nome=nome

    def get_posizione(self):
        return self.posizione

    def get_direzione(self):
        return self.direzione

    def __setDirezione(self, direzione):
        self.direzione.append(direzione)
        return self.direzione


    def get_durata(self):
        return self.durata

    def __setDurata(self, durata):
        self.durata = durata

    def getDescrizione(self):
        return self.get_Nome(),self.durata,self.posizioni,self.get_direzione(),self.get_Partidelcorpo()

    def aggiungiParteDelcorpoCoinvolta(self,partedelcorpo):
        self.partidelcorpo.append(partedelcorpo)
        return self.partidelcorpo

    def get_Partidelcorpo(self):
        return self.partidelcorpo

    def setposizione(self,nuovaposizione):
      self.posizionepartenza=nuovaposizione


    def add_posizionepartenza(self,posizionepartenza):
         if self.posizioni==[]:
          self.posizioni.insert(0,(posizionepartenza.get_X(),posizionepartenza.get_Y(),posizionepartenza.get_Z()))
         else:
          self.posizioni.append((posizionepartenza.get_X(),posizionepartenza.get_Y(),posizionepartenza.get_Z()))
         return self.posizioni

    def getPosizionepartenza(self,posizionepartenza):
        return self.add_posizionepartenza(posizionepartenza)

    # tutte le posizioni coinvolte nel movimento
    def add_posizioni(self,nuovaposizione):
        self.posizioni.append((nuovaposizione.get_X(),nuovaposizione.get_Y(),nuovaposizione.get_Z()))
        return self.posizioni


    def get_posizioni(self):
       return self.posizioni

    def aggiungisimbolo(self,simbolo):
        return self.listasimboli.append(simbolo)

    def ricavaUltimaPosizione(self):
        return self.posizioni[-1]



    # ogni movimento modifica le posizioni in un immaginario asse che considera laban
    # sistema di laban , ad esempio lo spazio lo rappresento per comoditò sul'ase x, y,z
    #determino l'effetto di ogni movimento

    def costruiscidanza(self,):
        if self.durata == 0:
           return None
        else:
            print("Costruisco la danza ")
            while self.durata != 0:
                print("aggiungiposizone")
                partedelcorpo=input("inserisci parte del corpo")
                self.aggiungiParteDelcorpoCoinvolta(partedelcorpo)
                self.__setDirezione(input("inserisci direzione"))
                valoreposizioneX= int(input("inserisci valore coordinataX"))
                valoreposizioneY= int(input("inserisci valore coordinataY"))
                valoreposizioneZ= int(input("inserisci valore coordinataZ"))
                nuovaposizione=posizione.Posizione #creo le nuove posizioni
                nuovaposizione.set_X(self,valoreposizioneX)
                nuovaposizione.set_Y(self,valoreposizioneY)
                nuovaposizione.set_Z(self,valoreposizioneZ)
                self.posizioni.append((nuovaposizione.get_X(self),nuovaposizione.get_Y(self),nuovaposizione.get_Z(self)))
                self.durata -= 1
            return self.posizioni




