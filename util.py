#!/usr/bin/python3
#encoding:utf-8
 #生成器，for循环时会依次返回每一行，它只在文件的最后追加了一个空行\n
import sys
  def lines(file):
      for line in file:yield line
     yield '\n'
 #生成器，for循环时会依次返回文本块组成的函数
 def blocks(file):
     block = []
     for line in lines(file):
        if line.strip():
             block.append(line)
         elif block:
             yield ''.join(block).strip()
             block = []