# -*- coding: utf-8 -*-

import yaml


with open ('questionnaires.yml', 'r') as stream:
  Q=yaml.safe_load(stream)

class Player:
    def __init__(self, name):
        self.name = name
        self.responses = []
        self.score = 0

class Response:
    def __init__(self, id, response, point):
        self.id = id
        self.point = point
        self.response = response

        
game=dict()


s=None

with open ('scenario.txt', 'r') as stream:
  while(True):
    
    s=stream.readline()
    command=s.split()
    firstword=command[0]
    print (command)
    
    match firstword:
    
    # Action du maitre du jeu
    case "master":
        
        # Démarrage d'un nouveau jeu  
        case "init":
        #initialisation du nombre de joueurs, du questionnaire
            nbrplayer = 0
            players = dict()
            points=dict()
            qi = -1
            print("init nbrplayer",nbrplayer)


        # Lancement de la question suivante
        case "start":
            # Envoie de la question au UI
            qi+=1
            print ("start")
            print (Q[qi]["prompt"]) 
            
        # Validation des réponses
        case "valid":

            # Action après Buzz, la réponse du joueur est correcte
            case "buzz":
                print ("valid buzz")

                # Mettre en avant plan le joueur qui a donné la bonne réponse
                
                # Comptage des points (le nombre de point est indiqué dans le questionnaire)    
                    for c, player in players.items():
                        
                        if player.name == color:
                                player.responses.append (Response(Q[qi]['id'], 'Good',Q[qi]['point']))
                        else:
                                player.responses.append (Response(Q[qi]['id'], '',Q[qi][0]))

                    print (player.responses)
            
            # Action après multi, validation des réponses et affichage des scores    
            case "multi":
                # La bonne réponse était ...
                
                # Les réponses des joueurs sont ...
                
                # Mettre 'No response' les joueurs qui n'ont pas répondu
                
                # Comptage des points
                
          
        # Fin du jeu
        case "quit":
            # Affichage du vainqueur !
            print ("quit")

            break 
         
         

      # Action d'un joueur
      case "player":
          
          _, action, color, attr =command
          
          match action:
              
              # Nouveau joueur
              case "new":
                  
                  nbrplayer = nbrplayer+1
                  #print("nbrplayer", nbrplayer)
                  
                  player = Player(color)
                  players[color]=player
                 
              # Buzz d'un joueur
              case "buzz":
                  # Arrêt de la lecture de la vidéo, de la musique
                  print ("buzz", color)
                  
                  # Mettre en surbrillance dans le UI le joueur qui à buzzé
                  
                  # Retenir quel est le joueur qui a buzzé
                  
              # Action après Buzz, la réponse du joueur est mauvaise    
              case "failed":
                  print ("failed", color)
                  
                  # Retirer la surbrillance dans le UI du joueur qui avait buzzé
                  
        
              # Action de réponse lors d'un choix multiple
              case "multi":
                  print ("multi", color)
                  
                  # Enregistrement de la réponse du joueur
                  
                  
            
                  
                 
                 
                 

 
    
    
    
      


