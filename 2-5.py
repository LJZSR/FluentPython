#使用生成器表达式初始化元组和数组
symbols = '@#$%&'
tuple(ord(symbol) for symbol in symbols)
import array
array.array('I', (ord(symbol) for symbol in symbols))

