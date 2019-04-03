#将元组用作记录
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
travels_ids = [('USA','31195855'), ('BRA','CE342567'), ('ESP','XDA205856')]
for passport in sorted(travels_ids):
    print('%s %s' % passport)
for country, _ in travels_ids:
    print(country)

#元组拆包
latitude, longitude = lax_coordinates
print(latitude, longitude)

#交换a，b
a = 3
b = 4
print(a, b)
a, b = b, a
print(a, b)

#用*运算符将一个可迭代对象拆开作为函数的参数
t = (20, 8)
print(divmod(*t))
