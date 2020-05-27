"""

lec 6

"""

demo_str = "This is my string"
#for str_item in demo_str:
#   print(str_demo)

for word_item in demo_str.split():
    print(word_item)
    for str_item in word_item:
        print(str_item)
    
 # if word_item != "my":
     # print(word_item)
  
  #  print(word_item.upper())
  #  print(word_item.title())
    
#print(range(5))
for each_num in range(1,5):
    print(each_num)
    
num_list =[213,321,123,312]

max_item = num_list[0]

for num in num_list:
    if max_item <= num:
        max_item = num

print(max_item)