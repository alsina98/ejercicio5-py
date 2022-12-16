def bisiesto(año):
    if not año % 4 and (año % 100 or not año % 400):
        print("bisiesto")
    else:
        print("no bisiesto")
        
año = int(input('Escribe un año...'))

bisiesto(año) 

# 2020 -> bisiesto
# 2022 -> no bisiesto
# 2024 -> bisiesto