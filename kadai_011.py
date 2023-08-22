#for文を使って繰り返す
list = ["水","金","地","火","木","土","天","海","冥"]

for i in list[0:9]:
  print(i)


#while文を使って繰り返す

list = ["水","金","地","火","木","土","天","海","冥"]
index=0
while index<len(list):
  print(list[index])
  index+=1
