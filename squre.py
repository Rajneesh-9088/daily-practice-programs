li = [5,7,8,1,2,3,9,5,45,7,8,5]
dic = {}

out = [a for a in li if a%2==1]
for x in li:
       
    dic[x] = x*x

print(dic)