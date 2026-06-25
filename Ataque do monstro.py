import random

hp_heroi = 100
hp_monstro = 100

print("⚔️ A BATALHA COMEÇOU! ⚔️")

while hp_heroi > 0 and hp_monstro > 0:
    print(f"\nSeu HP: {hp_heroi} | HP do Monstro: {hp_monstro}")
    print("Escolha sua ação:")
    print("1 - Atacar")
    print("2 - Curar")
    
    acao = int(input("O que você deseja fazer? "))
    
    # 1. Crie o WHILE de validação aqui (enquanto acao não for 1 e nem 2)
    while acao != 1 and acao != 2:
        print("Ação inválida! Escolha novamente.")
        acao = int(input("O que você deseja fazer? "))
    # 2. Desenvolva as consequências da ação do herói:
    if acao == 1:
        hp_monstro -= random.randint(10, 20)  # Herói ataca o monstro com dano entre 10 e 20
        pass
    elif acao == 2:
        # Herói se cura entre 15 e 30 (Dica: use um IF depois para garantir que não passe de 100)
        hp_heroi += random.randint(15, 30)
        if hp_heroi > 100:
            hp_heroi = 100
        pass

    # 3. Verifique se o monstro morreu. Se morreu, use o 'break' para sair do loop.
    if hp_monstro <= 0:
        print("O monstro foi derrotado! 🎉")
        break

    # 4. Turno do Monstro: Se ele continuou vivo, ele ataca o herói (dano entre 12 e 22)
    hp_heroi -= random.randint(12, 22)