def havi_torlesztoreszlet():
    hitelosszeg = float(input("Add meg a hitelösszeget (Forintban): "))
    eves_kamatlab = float(input("Add meg az éves kamatlábat (százalékban): "))
    futamido = int(input("Add meg a futamidőt (hónapokban): "))
    havi_kamatlab = eves_kamatlab / 100 / 12

    if havi_kamatlab == 0:
        torlesztoreszlet = hitelosszeg / futamido
    else:
        torlesztoreszlet = (hitelosszeg * havi_kamatlab * (1 + havi_kamatlab) ** futamido) / ((1 + havi_kamatlab) ** futamido - 1)
        
    torlesztoreszlet = round(torlesztoreszlet, 2)

    print(f"A havi törlesztőrészlet: {torlesztoreszlet} Ft")

havi_torlesztoreszlet()
