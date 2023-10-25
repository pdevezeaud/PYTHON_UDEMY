import random
#NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN,NOMBRE_MAX)


def poser_question():
    operateur_A = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    operateur_B = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    addition = operateur_A + operateur_B
    question = input(f" qu'elle le resultat de {operateur_A} + {operateur_B}\n")
    reponse_addition = int(question)

    if reponse_addition == operateur_A + operateur_B:
        return True
    
    else:
        return False
        
        
        

NOMBRE_POINTS = 0
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION = 4
   
for i in range(0,NB_QUESTION):
    print(F"question N° {i+1} sur {NB_QUESTION}")
    if poser_question() == True:
        print("Réponse correcte")
        NOMBRE_POINTS += 1
    else:
        print("Réponse incorrect")
        
    print()
        
    

print(f"votre note est de {NOMBRE_POINTS}/{NB_QUESTION}")

