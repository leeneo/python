what_he_does='plays '
his_instrument='guitar'
his_name='Robert Johnson '
artist_intro=his_name+what_he_does+his_instrument
print(artist_intro)

words='word'*3
print(words)

word='a long long word'
num=12 
onestr='bang!' 
total=onestr*(len(word)-num)    # 等价于字符串'bang!'*4
print(total)
print(len(word))    # len() 取字符串长度，不能用于非字符类型

name='My name is Mikcal'
print('\n字符串分割 类似于 chars.slice()')
print(name[0])
print(name[2])
print(name[-4]) # 倒数第4个
print(name[11:14]) #=>slice(11,14):不含14
print(name[11:15])  #=>slice(11,15):不含15
print(name[5:]) # 省略前5个字符
print(name[:5]) # 截取前5个字符

word='friends'
find_the_evil=word[0]+' '+word[2:4]+' '+word[-3:-1]
print('\n'+find_the_evil)