# Дан список стран и городов каждой страны. 
# Затем даны названия городов. Для
# каждого города укажите, в какой стране он находится.
Cities = {'Bishkek':'Kyrgyzstan', 'Madrid':'Spain', 'Rome':'Italy'}
print(Cities)
print("Gde ty hochesh jit ?")
country = input()

if country in Cities:
    print('This city of country', Cities(country))
