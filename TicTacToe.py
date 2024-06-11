joueur = 2
while True:
    da = 0
    db = 0
    dc = 0
    ea = 0
    eb = 0
    ec = 0
    fa = 0
    fb = 0
    fc = 0
    case = 0
    if joueur == 1:
        joueur = 2
    elif joueur == 2:
        joueur = 1
    win = 0
    score1 = 0
    score2 = 0
    while win == 0:
        # système de victoire
        if da == 1 and db == 1 and dc == 1:
            win = 1
            score1 = score1 + 1
            print("JOUEUR 1 A GAGNER (O)")
        if da == 2 and db == 2 and dc == 2:
            win = 2
            score2 = score2 + 1
            print("JOUEUR 1 A GAGNER (X)")
        if ea == 1 and eb == 1 and ec == 1:
            win = 1
            score1 = score1 + 1
            print("JOUEUR 1 A GAGNER (O)")
        if ea == 2 and eb == 2 and ec == 2:
            win = 2
            score2 = score2 + 1
            print("JOUEUR 1 A GAGNER (X)")
        if fa == 1 and fb == 1 and fc == 1:
            win = 1
            score1 = score1 + 1
            print("JOUEUR 1 A GAGNER (O)")
        if fa == 2 and fb == 2 and fc == 2:
            win = 2
            score2 = score2 + 1
            print("JOUEUR 1 A GAGNER (X)")
        if da == 1 and ea == 1 and fa == 1:
            win = 1
            score1 = score1 + 1
            print("JOUEUR 1 A GAGNER (O)")
        if da == 2 and ea == 2 and fa == 2:
            win = 2
            score2 = score2 + 1
            print("JOUEUR 1 A GAGNER (X)")
        if db == 1 and eb == 1 and fb == 1:
            win = 1
            score1 = score1 + 1
            print("JOUEUR 1 A GAGNER (O)")
        if db == 2 and eb == 2 and fb == 2:
            win = 2
            score2 = score2 + 1
            print("JOUEUR 1 A GAGNER (X)")
        if dc == 1 and ec == 1 and fc == 1:
            win = 1
            score1 = score1 + 1
            print("JOUEUR 1 A GAGNER (O)")
        if dc == 2 and ec == 2 and fc == 2:
            win = 2
            score2 = score2 + 1
            print("JOUEUR 1 A GAGNER (X)")
        if da == 1 and eb == 1 and fc == 1:
            win = 1
            score1 = score1 + 1
            print("JOUEUR 1 A GAGNER (O)")
        if da == 2 and eb == 2 and fc == 2:
            win = 2
            score2 = score2 + 1
            print("JOUEUR 1 A GAGNER (X)")
        if dc == 1 and eb == 1 and fa == 1:
            win = 1
            score1 = score1 + 1
            print("JOUEUR 1 A GAGNER (O)")
        if dc == 2 and eb == 2 and fa == 2:
            win = 2
            score2 = score2 + 1
            print("JOUEUR 1 A GAGNER (X)")

        # ligne 1
        if da == 0 and db == 0 and dc == 0:
            print(".  .  .")
        if da == 0 and db == 0 and dc == 1:
            print(".  .  0")
        if da == 0 and db == 0 and dc == 2:
            print(".  .  X")
        if da == 0 and db == 1 and dc == 0:
            print(".  0  .")
        if da == 0 and db == 1 and dc == 1:
            print(".  0  0")
        if da == 0 and db == 1 and dc == 2:
            print(".  0  X")
        if da == 0 and db == 2 and dc == 0:
            print(".  X  .")
        if da == 0 and db == 2 and dc == 1:
            print(".  X  0")
        if da == 0 and db == 2 and dc == 2:
            print(".  X  X")
        if da == 1 and db == 0 and dc == 0:
            print("0  .  .")
        if da == 1 and db == 0 and dc == 1:
            print("0  .  0")
        if da == 1 and db == 0 and dc == 2:
            print("0  .  X")
        if da == 1 and db == 1 and dc == 0:
            print("0  0  .")
        if da == 1 and db == 1 and dc == 1:
            print("0  0  0")
        if da == 1 and db == 1 and dc == 2:
            print("0  0  X")
        if da == 1 and db == 2 and dc == 0:
            print("O  X  .")
        if da == 1 and db == 2 and dc == 1:
            print("O  X  O")
        if da == 1 and db == 2 and dc == 2:
            print("O  X  X")
        if da == 2 and db == 0 and dc == 0:
            print("X  .  .")
        if da == 2 and db == 0 and dc == 1:
            print("X  .  0")
        if da == 2 and db == 0 and dc == 2:
            print("X  .  X")
        if da == 2 and db == 1 and dc == 0:
            print("X  0  .")
        if da == 2 and db == 1 and dc == 1:
            print("X  0  0")
        if da == 2 and db == 1 and dc == 2:
            print("X  0  X")
        if da == 2 and db == 2 and dc == 0:
            print("X  X  .")
        if da == 2 and db == 2 and dc == 1:
            print("X X   0")
        if da == 2 and db == 2 and dc == 2:
            print("X  X  X")

        # ligne 2
        if ea == 0 and eb == 0 and ec == 0:
            print(".  .  .")
        if ea == 0 and eb == 0 and ec == 1:
            print(".  .  0")
        if ea == 0 and eb == 0 and ec == 2:
            print(".  .  X")
        if ea == 0 and eb == 1 and ec == 0:
            print(".  0  .")
        if ea == 0 and eb == 1 and ec == 1:
            print(".  0  0")
        if ea == 0 and eb == 1 and ec == 2:
            print(".  0  X")
        if ea == 0 and eb == 2 and ec == 0:
            print(".  X  .")
        if ea == 0 and eb == 2 and ec == 1:
            print(".  X  0")
        if ea == 0 and eb == 2 and ec == 2:
            print(".  X  X")
        if ea == 1 and eb == 0 and ec == 0:
            print("0  .  .")
        if ea == 1 and eb == 0 and ec == 1:
            print("0  .  0")
        if ea == 1 and eb == 0 and ec == 2:
            print("0  .  X")
        if ea == 1 and eb == 1 and ec == 0:
            print("0  0  .")
        if ea == 1 and eb == 1 and ec == 1:
            print("0  0  0")
        if ea == 1 and eb == 1 and ec == 2:
            print("0  0  X")
        if ea == 1 and eb == 2 and ec == 0:
            print("O  X  .")
        if ea == 1 and eb == 2 and ec == 1:
            print("O  X  O")
        if ea == 1 and eb == 2 and ec == 2:
            print("O  X  X")
        if ea == 2 and eb == 0 and ec == 0:
            print("X  .  .")
        if ea == 2 and eb == 0 and ec == 1:
            print("X  .  0")
        if ea == 2 and eb == 0 and ec == 2:
            print("X  .  X")
        if ea == 2 and eb == 1 and ec == 0:
            print("X  0  .")
        if ea == 2 and eb == 1 and ec == 1:
            print("X  0  0")
        if ea == 2 and eb == 1 and ec == 2:
            print("X  0  X")
        if ea == 2 and eb == 2 and ec == 0:
            print("X  X  .")
        if ea == 2 and eb == 2 and ec == 1:
            print("X  X  0")
        if ea == 2 and eb == 2 and ec == 2:
            print("X  X  X")

        # ligne 3
        if fa == 0 and fb == 0 and fc == 0:
            print(".  .  .")
        if fa == 0 and fb == 0 and fc == 1:
            print(".  .  0")
        if fa == 0 and fb == 0 and fc == 2:
            print(".  .  X")
        if fa == 0 and fb == 1 and fc == 0:
            print(".  0  .")
        if fa == 0 and fb == 1 and fc == 1:
            print(".  0  0")
        if fa == 0 and fb == 1 and fc == 2:
            print(".  0  X")
        if fa == 0 and fb == 2 and fc == 0:
            print(".  X  .")
        if fa == 0 and fb == 2 and fc == 1:
            print(".  X  0")
        if fa == 0 and fb == 2 and fc == 2:
            print(".  X  X")
        if fa == 1 and fb == 0 and fc == 0:
            print("0  .  .")
        if fa == 1 and fb == 0 and fc == 1:
            print("0  .  0")
        if fa == 1 and fb == 0 and fc == 2:
            print("0  .  X")
        if fa == 1 and fb == 1 and fc == 0:
            print("0  0  .")
        if fa == 1 and fb == 1 and fc == 1:
            print("0  0  0")
        if fa == 1 and fb == 1 and fc == 2:
            print("0  0  X")
        if fa == 1 and fb == 2 and fc == 0:
            print("O  X  .")
        if fa == 1 and fb == 2 and fc == 1:
            print("O  X  O")
        if fa == 1 and fb == 2 and fc == 2:
            print("O  X  X")
        if fa == 2 and fb == 0 and fc == 0:
            print("X  .  .")
        if fa == 2 and fb == 0 and fc == 1:
            print("X  .  0")
        if fa == 2 and fb == 0 and fc == 2:
            print("X  .  X")
        if fa == 2 and fb == 1 and fc == 0:
            print("X  0  .")
        if fa == 2 and fb == 1 and fc == 1:
            print("X  0  0")
        if fa == 2 and fb == 1 and fc == 2:
            print("X  0  X")
        if fa == 2 and fb == 2 and fc == 0:
            print("X  X  .")
        if fa == 2 and fb == 2 and fc == 1:
            print("X  X  0")
        if fa == 2 and fb == 2 and fc == 2:
            print("X  X  X")

        print("")
        case = int(input("ENTRER LA CASE"))
        if joueur == 1:
            joueur = 2
        elif joueur == 2:
            joueur = 1
        if case == 1:
            if da == 0:
                if joueur == 1:
                    da = 1
                elif joueur == 2:
                    da = 2
            else:
                print("CETTE CASE EST DEJA OCCUPEE!")
                if joueur == 1:
                    joueur = 2
                elif joueur == 2:
                    joueur = 1
        if case == 2:
            if db == 0:
                if joueur == 1:
                    db = 1
                elif joueur == 2:
                    db = 2
            else:
                print("CETTE CASE EST DEJA OCCUPEE!")
                if joueur == 1:
                    joueur = 2
                elif joueur == 2:
                    joueur = 1
        if case == 3:
            if dc == 0:
                if joueur == 1:
                    dc = 1
                elif joueur == 2:
                    dc = 2
            else:
                print("CETTE CASE EST DEJA OCCUPEE!")
                if joueur == 1:
                    joueur = 2
                elif joueur == 2:
                    joueur = 1
        if case == 4:
            if ea == 0:
                if joueur == 1:
                    ea = 1
                elif joueur == 2:
                    ea = 2
            else:
                print("CETTE CASE EST DEJA OCCUPEE!")
                if joueur == 1:
                    joueur = 2
                elif joueur == 2:
                    joueur = 1
        if case == 5:
            if eb == 0:
                if joueur == 1:
                    eb = 1
                elif joueur == 2:
                    eb = 2
            else:
                print("CETTE CASE EST DEJA OCCUPEE!")
                if joueur == 1:
                    joueur = 2
                elif joueur == 2:
                    joueur = 1
        if case == 6:
            if ec == 0:
                if joueur == 1:
                    ec = 1
                elif joueur == 2:
                    ec = 2
            else:
                print("CETTE CASE EST DEJA OCCUPEE!")
                if joueur == 1:
                    joueur = 2
                elif joueur == 2:
                    joueur = 1
        if case == 7:
            if fa == 0:
                if joueur == 1:
                    fa = 1
                elif joueur == 2:
                    fa = 2
            else:
                print("CETTE CASE EST DEJA OCCUPEE!")
                if joueur == 1:
                    joueur = 2
                elif joueur == 2:
                    joueur = 1
        if case == 8:
            if fb == 0:
                if joueur == 1:
                    fb = 1
                elif joueur == 2:
                    fb = 2
            else:
                print("CETTE CASE EST DEJA OCCUPEE!")
                if joueur == 1:
                    joueur = 2
                elif joueur == 2:
                    joueur = 1
        if case == 9:
            if fc == 0:
                if joueur == 1:
                    fc = 1
                elif joueur == 2:
                    fc = 2
            else:
                print("CETTE CASE EST DEJA OCCUPEE!")
                if joueur == 1:
                    joueur = 2
                elif joueur == 2:
                    joueur = 1

    print("SCORE JOUEUR 1 (0):", score1)
    print("SCORE JOUEUR 2 (X):", score2)
