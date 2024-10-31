
rejestracje_samochodowe = {
    "Ford": "abC1234",
    "Audi": "XY Z5678",
    "Citroen": "KL-m9101",
    "Honda": "NOP2345"
}

for key, val in rejestracje_samochodowe.items():
    rejestracje_samochodowe[key] = val.upper().replace(" ", "").replace("-", "")

print(rejestracje_samochodowe)