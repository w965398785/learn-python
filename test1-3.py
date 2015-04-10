# -*- coding:utf-8 -*-
s1='姓名: 王本松'
s2='学号: 1403050120'
s3='班级: 通风一班'
#file:quadratic.py 
import math
a=1
b=-4
c=4
disRoot = math.sqrt(b*b - 3*a*c)
x1 = (-b + discRoot) / (2 * a)
x2 = (-a - discRoot) / (2 * a)
print"第1个解x1=",x1
print"第2个解x2=",x2