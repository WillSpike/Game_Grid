import random
import os

def clear_screen():
    if os.name == 'nt':  # pour Windows a voir
        os.system('cls')
    else:  # pour Mac et Linux
        os.system('clear')
       
def creer_grille(taille):
    return [[' ' for _ in range(taille)] for _ in range(taille)]

def afficherGrille(grid):
    for row in grid:
        for cell in row:
            if cell == ' ':
                print('⬛', end='')  # Utiliser un émoji pour les espaces vides
            elif cell == '🚶':
                print('🚶', end='')  # Utiliser un émoji pour le joueur
            elif cell == '⭐':
                print('⭐', end='')  # Utiliser un émoji pour l'étoile
            elif cell == '🔲':
                print('🔲', end='')  # Utiliser un émoji pour l'obstacle
        print()

def position_aleatoire(taille, grid, exclure=[]):
    while True:
        pos = [random.randint(0, taille-1), random.randint(0, taille-1)]
        if pos not in exclure and grid[pos[0]][pos[1]] == ' ':
            return pos

def ajouter_obstacles(grid, nombre):
    for _ in range(nombre):
        obstacle_pos = position_aleatoire(len(grid), grid)
        grid[obstacle_pos[0]][obstacle_pos[1]] = '🔲'

def boucle_de_jeu(grid, player_pos, star_pos, taille):
    score = 0
    while True:    
        print("Votre score est : " + str(score) + "")
        move = input("Commandes :(z)Haut, (s)bas, (q)gauche, (d) droite (Q ou quitter)  : ")
        if move not in ['z', 's', 'q', 'd', 'Q']:
            print("Commande non reconnue. Veuillez réessayer.")
            continue

        if move == 'Q' or move == 'quitter':
            print("Merci d'avoir joué ! Votre score final est : ", score)
            break

        grid[player_pos[0]][player_pos[1]] = ' '  # effacer la position actuelle du joueur

        if move == 'z' and grid[max(0, player_pos[0] - 1)][player_pos[1]] != '🔲':
            player_pos[0] = max(0, player_pos[0] - 1)
        elif move == 's' and grid[min(taille-1, player_pos[0] + 1)][player_pos[1]] != '🔲':
            player_pos[0] = min(taille-1, player_pos[0] + 1)
        elif move == 'q' and grid[player_pos[0]][max(0, player_pos[1] - 1)] != '🔲':
            player_pos[1] = max(0, player_pos[1] - 1)
        elif move == 'd' and grid[player_pos[0]][min(taille-1, player_pos[1] + 1)] != '🔲':
            player_pos[1] = min(taille-1, player_pos[1] + 1)

        # Vérifier si le joueur a atteint l'étoile
        if player_pos == star_pos:
            score += 1            
            # Créer une nouvelle étoile à une position aléatoire
            while True:
                star_pos = position_aleatoire(taille, grid, [player_pos])
                if grid[star_pos[0]][star_pos[1]] != '🔲':
                    break

        clear_screen()

        grid[player_pos[0]][player_pos[1]] = '🚶'  # mettre à jour la nouvelle position du joueur
        grid[star_pos[0]][star_pos[1]] = '⭐'  # mettre à jour la position de l'étoile
        
        afficherGrille(grid)


def main():
    taille = 10
    grid = creer_grille(taille)
    player_pos = position_aleatoire(taille, grid)
    grid[player_pos[0]][player_pos[1]] = '🚶'
    star_pos = position_aleatoire(taille, grid, [player_pos])
    grid[star_pos[0]][star_pos[1]] = '⭐'
    ajouter_obstacles(grid, 10)
    afficherGrille(grid)
    boucle_de_jeu(grid, player_pos, star_pos, taille)

if __name__ == "__main__":
    main()
