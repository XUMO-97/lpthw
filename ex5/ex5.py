# -- coding: utf-8 --
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky , try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)

# study drills 1
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky , try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
	
# study drills 2
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %r inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

# this line is tricky , try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
	age, height, weight, age + height + weight)
	
# study drills 3

# 'd'	Signed integer decimal.格式化整数
# 'i'	Signed integer decimal. 转成有符号十进制数
# 'o'	Signed octal value. 格式化无符号八进制数
# 'u'	Obsolete type – it is identical to 'd'. 格式化无符号整型
# 'x'	Signed hexadecimal (lowercase). 格式化无符号十六进制数
# 'X'	Signed hexadecimal (uppercase). 格式化无符号十六进制数（大写）
# 'e'	Floating point exponential format (lowercase). 用科学计数法格式化浮点数
# 'E'	Floating point exponential format (uppercase). 作用同%e，用科学计数法格式化浮点数
# 'f'	Floating point decimal format. 格式化浮点数字，可指定小数点后的精度
# 'F'	Floating point decimal format. 格式化浮点数字，可指定小数点后的精度
# 'g'	Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. %f和%e的简写
# 'G'	Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise. %f 和 %E 的简写
# 'c'	Single character (accepts integer or single character string). 格式化字符及其ASCII码
# 'r'	String (converts any Python object using repr()). %r用rper()方法处理对象
# 's'	String (converts any Python object using str()). 格式化字符串 %s用str()方法处理对象
# '%'	No argument is converted, results in a '%' character in the result. 输出% （格式化字符串里面包括百分号，那么必须使用%%）

# study drills 4
height = 100 #inches
weight = 100 #pounds
print "100 inchs = %s centimeters" % (2.54*height)
print "100 pounds = %r kilos" % (0.4535924*weight)