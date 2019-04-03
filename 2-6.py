#使用生成器表达式输出笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ('%s %s' %(c, s) for c in colors for s in sizes):
    print(tshirt)