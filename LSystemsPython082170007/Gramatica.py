import re 

class Gramatica(object):

     def defineAlfabeto(self,arrayString):
        for string in arrayString:
            i = string.find('Σ :')
            if i != -1:
                alfabetoString = string.replace('Σ :','').strip()
                alfabetotArray =  alfabetoString.split(',')
                alfabetotArray = list(map(str.strip, alfabetotArray))
                alfabetotArray.remove('+')
                alfabetotArray.remove('-')
                return alfabetotArray
        return None

     def defineReps(self,arrayString):
        for string in arrayString:
            i = string.find('n :')
            if i != -1:
                return string.replace('n :','').strip()            
        return None

     def defineAxioma(self,arrayString):
        for string in arrayString:
            i = string.find('ω :')
            if i != -1:
                return string.replace('ω :','').strip()            
        return None

     def definiAngulo(self,arrayString):
        for string in arrayString:
            i = string.find('δ :')
            if i != -1:
                return string.replace('δ :','').strip().replace('º','')            
        return None

     def defineRegras(self,arrayString):
          regras = []
          for string in arrayString:
               if(re.match('(p\d* :)',string)):
                   stringfix = string.replace('\n','').replace('→','->')
                   regras.append(re.sub('(p\d* :)','',stringfix))
          return regras

     def __init__(self, ArrayDeStringsDoTxt):
         self.alfabeto = self.defineAlfabeto(ArrayDeStringsDoTxt)
         self.reps = self.defineReps(ArrayDeStringsDoTxt)
         self.axioma = self.defineAxioma(ArrayDeStringsDoTxt)
         self.angulo = self.definiAngulo(ArrayDeStringsDoTxt)
         self.regras = self.defineRegras(ArrayDeStringsDoTxt)

