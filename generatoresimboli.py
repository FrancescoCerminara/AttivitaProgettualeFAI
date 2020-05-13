import movimento
import simbolo

#qui genero l'oggetto generatoresimboli il quale mi permetterà di eseguire la classificazione
class GeneratoreSimboli(object):

      movimento=movimento.Movimento
      def __init__(self):
         self.listasimboli=[]
         self.movimento=movimento



      def getListaSimboli(self):
         return self.listasimboli

      def setListaSimboli(self,listasimboli):
         self.listasimboli=listasimboli


      def aggiungigisimbolo(self,simbolo):
         return self.listasimboli.append(simbolo)

      #procedo alla classificazione dei simboli per direzione
      def classificasimbolodirezioneedaltezza(self,movimento):
        for direzione in movimento[3]:
          if  direzione==' in alto':
               simbolo.Simbolo.set_Label(self,"s1")
               simbolo.Simbolo.set_Nome(self,"UP")
               return simbolo.Simbolo.get_Label(self) + "-" +simbolo.Simbolo.get_Nome(self)

          elif direzione==' indietro':
                simbolo.Simbolo.set_Label(self,"s2")
                simbolo.Simbolo.set_Nome(self,"BACK")
                return simbolo.Simbolo.get_Label(self) + "-" +simbolo.Simbolo.get_Nome(self)

          elif direzione==' in basso':
               simbolo.Simbolo.set_Label(self,"s3")
               simbolo.Simbolo.set_Nome(self,"DOWN")
               return simbolo.Simbolo.get_Label(self) + "-" +simbolo.Simbolo.get_Nome(self)

          elif direzione==' intermedia':
               simbolo.Simbolo.set_Label(self,"s9")
               simbolo.Simbolo.set_Nome(self,"MIDDLE")
               return simbolo.Simbolo.get_Label(self) + "-" +simbolo.Simbolo.get_Nome(self)

          elif direzione==' avanti':
               simbolo.Simbolo.set_Label(self,"s4")
               simbolo.Simbolo.set_Nome(self,"FORWARD")
               return simbolo.Simbolo.get_Label(self) + "-" +simbolo.Simbolo.get_Nome(self)

          elif direzione==' sinistra':
               simbolo.Simbolo.set_Label(self,"s5")
               simbolo.Simbolo.set_Nome(self,"LEFT")
               return simbolo.Simbolo.get_Label(self) + "-" +simbolo.Simbolo.get_Nome(self)

          elif direzione==' destra':
               simbolo.Simbolo.set_Label(self,"s6")
               simbolo.Simbolo.set_Nome(self,"RIGHT")
               return simbolo.Simbolo.get_Label(self) + "-" +simbolo.Simbolo.get_Nome(self)

          else:
               simbolo.Simbolo.set_Label(self,"s7")
               simbolo.Simbolo.set_Nome(self,"STOP")
               return simbolo.Simbolo.get_Label(self) + "-" + simbolo.Simbolo.get_Nome(self)


      #accendo dunque ad una posizione specifica della tupla poiche essa 'è composta da liste o elementi semplici
      def classificazionesimbolopartedelcorpo(self,movimento):
           for partedelcorpo in movimento[4]: #posizione 4 della tupla
               if partedelcorpo==' gambadestra':
                   simbolo.Simbolo.set_Label(self,"s8")
                   simbolo.Simbolo.set_Nome(self,"RightLeg")
                   return simbolo.Simbolo.get_Label(self)+ "-" +simbolo.Simbolo.get_Nome(self)
               if partedelcorpo==' gambasinistra':
                   simbolo.Simbolo.set_Label(self,"s9")
                   simbolo.Simbolo.set_Nome(self,"LeftLeg")
                   return simbolo.Simbolo.get_Label(self)+ "-" +simbolo.Simbolo.get_Nome(self)
               if partedelcorpo==' bracciodestro':
                   simbolo.Simbolo.set_Label(self,"s10")
                   simbolo.Simbolo.set_Nome(self,"RIghtARM")
                   return simbolo.Simbolo.get_Label(self) + "-" +simbolo.Simbolo.get_Nome(self)
               if  partedelcorpo==' bracciosinistro':
                   simbolo.Simbolo.set_Label(self,"s11")
                   simbolo.Simbolo.set_Nome(self,"LeftARM")
                   return simbolo.Simbolo.get_Label(self) + "-" +simbolo.Simbolo.get_Nome(self)
               if  partedelcorpo==' gambe':
                   simbolo.Simbolo.set_Label(self,"s12")
                   simbolo.Simbolo.set_Nome(self,"BothLEG")
                   return simbolo.Simbolo.get_Label(self)+ "-" +simbolo.Simbolo.get_Nome(self)
               if partedelcorpo==' braccia ':
                   simbolo.Simbolo.set_Label(self,"s12")
                   simbolo.Simbolo.set_Nome(self,"BothARMS")
                   return simbolo.Simbolo.get_Label(self)+ "-" + simbolo.Simbolo.get_Nome(self)


      def classificazioneduratamovimento(self,movimento):
              if movimento[1]=="5":
                  simbolo.Simbolo.set_Label(self,"s7")
                  simbolo.Simbolo.set_Nome(self,"LUNGO")
                  return simbolo.Simbolo.get_Label(self)+ "-" + simbolo.Simbolo.get_Nome(self)
              else:
                  simbolo.Simbolo.set_Label(self,"s7")
                  simbolo.Simbolo.set_Nome(self,"BREVE")
                  return simbolo.Simbolo.get_Label(self)+ "-" +simbolo.Simbolo.get_Nome(self)


      # x ogni movimento,seguendo le dispoziioni della notaizone Laban creo un simbolo per la direzione/altezza,durata,
      #parte del corpo
      def generaSimboli(self,listamovimenti):
          pos=0
          while pos<len(listamovimenti):
            self.aggiungigisimbolo(self.classificazionesimbolopartedelcorpo(listamovimenti[pos]))
            self.aggiungigisimbolo(self.classificasimbolodirezioneedaltezza(listamovimenti[pos]))
            self.aggiungigisimbolo(self.classificazioneduratamovimento(listamovimenti[pos]))
            pos+=1
          return self.listasimboli




























