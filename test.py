s = "output\\伊利牛奶京东自营旗舰店-2017-12-06-京东超市伊利 无菌砖高钙低脂奶250ml*24盒".replace('*','x')
print(s)
filename = s+".txt"
with open(filename, "w+") as f:
    f.write("这是个测试！")