num=1
sum='9'

# type() 取变量数据类型
a=type(num)
b=type(sum)
print(a)
print(b)

#print(num+sum)  # 报错，字符串不能连接非字符串类型

# 类型字符串
mid=str(num)
print(mid+' '+sum)

# 类型转数值
mid=int(sum)
print(mid+num)