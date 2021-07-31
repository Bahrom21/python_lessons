# topshiriq 1. yoshi degan kiy bormi yo'qmi?
"""shaxs = {
  "ism": "Bunyod",
  "yoshi": 22,
  "kasbi": "o`qituvchi",
  "millati": "tatar"
}
if "yoshi" in shaxs.keys():
  print("bor")
else:
  print("yo`q")"""
#2-usul
shaxs = {
  "ism": "Bunyod",
  "yoshi": 22,
  "kasbi": "o`qituvchi",
  "millati": "tatar"
}
for i in shaxs:
  if i == "yoshi":
    print("bor")
  #break
else:
  print("yo`q")