a = float(input('сколько км пробежал спортсмен в первый день?'))
b = float(input('Ведите желаемый результат'))
d = 1

while a < b:
    d += 1
    a = a * 1.1
    print(d, '-й день:', round(a, 2))

print('На {}-й день спортсмен достиг результата — не менее {} км'.format(d, b))
