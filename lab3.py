#lab3

#3.1
str_list = ['a','d','e','b','c']
str_list.sort()
print(str_list)

#3.2
str_list.append('f')
print(str_list)

#3.3
str_list.remove('d')
print(str_list)

#3.4
print(str_list[2:3])

#3.5
my_list = ['a','123',123,'b','B','False',False, 123, None, "None"]
print(my_list)
print(set(my_list))

my_unique_leters = set(my_list)
print(len(my_unique_leters))

#3.6
thirdlab = str("This is my third python lab")
print(thirdlab)
words = thirdlab.split()
number_of_words = len(words)
print(number_of_words)

#3.7
num_list = [12,32,43,35]
num_list.sort(reverse = True)
print(num_list[:1])
print(num_list[3:])

#3.8
game_board = [ 
             [0,0,0],
             [0,0,0],
             [0,0,0],
                    ]
game_board[1][1]=1
print(game_board)