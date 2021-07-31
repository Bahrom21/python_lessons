"""qiymatlarni o'zgartirish"""
talaba = {
    "ism": "Nurbek",
    "kurs": "3-kurs",
    "baho": 5,
    "yoshi": 14}
talaba["millati"]="qozoq"   # millat qo'shish
print(talaba)

talaba["ism"]="Nurbek"      #ism o'zgartirish

if talaba["yoshi"]>15:      # 15 dan kichik bo'lsa, ...
   print("20 dan katta")
else:
   print("talaba 20 dan kichik")
