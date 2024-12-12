def index():
    suly = float(input("Testsúly (kg): "))
    magassag_cm = float(input("Magasság (cm): "))
    magassag = magassag_cm / 100
    bmi = suly / (magassag * magassag)

    if bmi < 18.5:
        kategoria = "Alultáplált"
    elif 18.5 <= bmi <= 24.9:
        kategoria = "Normál testsúly"
    elif 25 <= bmi <= 29.9:
        kategoria = "Túlsúlyos"
    else:
        kategoria = "Elhízott"

    print(f"BMI: {bmi}, Kategória: {kategoria}")

index()
