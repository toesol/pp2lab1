
n = int(input())  #ex:n = 12
           
x = bin(n)   #ex:0b1100
y = x.lstrip('0b')  #ex:1100

s = int()  
s = (y[::-1])   #ex:0011

k = ('0b') + s  #ex: 0b0011

c = int(k,2)    #ex: 3







