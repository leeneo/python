#!/usr/bin/python3
# #!/usr/bin/python3,这句话仅仅在linux或unix系统下有作用，在windows下无论在代码里加什么都无法直接运行一个文件名后缀为.py的脚本，因为在windows下文件名对文件的打开方式起了决定性作用

# linux =>./hello.py
# windows =>python hello.py
x = "Hello Python!";
print(x);
file = open('./test.txt', 'w')
file.write('hello world!')
