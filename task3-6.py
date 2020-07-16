# Дан словарь, состоящий из элементов типа: слово-синоним. 
# Все слова в словаре различны. 
# Выведите синоним для последнего слова.

a = {'White':'Black','Yellow':'Brown'}
values = a.values()
values_list = list(values)
a_value = values_list[-1]
print(a_value)
