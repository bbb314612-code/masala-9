import math

# FunSimple56: Ikki nuqta orasidagi masofani hisoblash
def Leng(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# FunSimple57: Uchburchak perimetrini hisoblash
def Perim(xA, yA, xB, yB, xC, yC):
    ab = Leng(xA, yA, xB, yB)
    bc = Leng(xB, yB, xC, yC)
    ac = Leng(xA, yA, xC, yC)
    return ab + bc + ac

# FunSimple58: Uchburchak yuzini (Heron formulasi bilan)
def Area(xA, yA, xB, yB, xC, yC):
    ab = Leng(xA, yA, xB, yB)
    bc = Leng(xB, yB, xC, yC)
    ac = Leng(xA, yA, xC, yC)
    p = (ab + bc + ac) / 2  # Yarim perimetr
    # Manfiy son chiqib qolmasligi uchun abs ishlatish tavsiya etiladi
    return math.sqrt(p * (p - ab) * (p - bc) * (p - ac))

# FunSimple59: Nuqtadan kesmagacha bo'lgan balandlik
def Dist(xA, yA, xB, yB, xP, yP):
    s_pab = Area(xA, yA, xB, yB, xP, yP)
    ab = Leng(xA, yA, xB, yB)
    if ab == 0: return 0  # Nolga bo'lishdan qochish
    return (2 * s_pab) / ab

# FunSimple60: Uchburchakning uchta balandligini hisoblash
def Heights(xA, yA, xB, yB, xC, yC):
    ha = Dist(xB, yB, xC, yC, xA, yA) # A dan BC tomonga
    hb = Dist(xA, yA, xC, yC, xB, yB) # B dan AC tomonga
    hc = Dist(xA, yA, xB, yB, xC, yC) # C dan AB tomonga
    return ha, hb, hc

# Asosiy qism (Ma'lumotlarni kiritish)
try:
    print("Nuqtalarni x y formatida kiriting (masalan: 0 0):")
    xA, yA = map(float, input("A nuqta: ").split())
    xB, yB = map(float, input("B nuqta: ").split())
    xC, yC = map(float, input("C nuqta: ").split())
    xD, yD = map(float, input("D nuqta: ").split())

    print("\n" + "="*20)
    
    # 57-masala: Perimetrlar
    print(f"ABC Perimetri: {Perim(xA, yA, xB, yB, xC, yC):.2f}")
    print(f"ABD Perimetri: {Perim(xA, yA, xB, yB, xD, yD):.2f}")
    print(f"ACD Perimetri: {Perim(xA, yA, xC, yC, xD, yD):.2f}")

    # 58-masala: Yuzalar
    print(f"\nABC Yuzi: {Area(xA, yA, xB, yB, xC, yC):.2f}")
    print(f"ABD Yuzi: {Area(xA, yA, xB, yB, xD, yD):.2f}")
    print(f"ACD Yuzi: {Area(xA, yA, xC, yC, xD, yD):.2f}")

    # 60-masala: ABC uchburchak balandliklari
    ha, hb, hc = Heights(xA, yA, xB, yB, xC, yC)
    print(f"\nABC Balandliklari: hA={ha:.2f}, hB={hb:.2f}, hC={hc:.2f}")

except ValueError:
    print("Iltimos, faqat sonlarni kiriting!")