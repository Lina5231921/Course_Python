sec1 = int(input('Сколько секунд Вы хотите перевести в часы? '))

sec = sec1 % 60
hour = sec1 // 3600
min = (sec1 - hour * 3600) // 60
print(sec1, f'секунд это {hour:02}:{min:02}:{sec:02}')
