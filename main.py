#name=input("What is your name?")
#print("Hello"+ name)
#import random
#number = int(input("enter a number"))

#if number > 10:
 # print("the number is too big")
#elif number < 10:
 # print(" the number is less than 10")
#else:
 # print("the number is 10")

#list = [1, 2, 3, 4, 5]
#for num in list:
  #print (num)
#i=0
#num = []
#for i in range(10):
  #num.append(random.randint(1,100))
#print (num)
#num_list=[]
#def take_average():
  #total = 0
  #for num in num_list:
    #total+=num
  #average = total/len(num_list)
  #print("the average of the numbers"+str(average))
#while True:
  #answer = input("enter a number. type 'stop' to take average ")
  #if answer == 'stop':
    #take_average()
    #break
  #else:
    #num_list.append(int(answer))
  
word_list = [] 
def split_word():
  for letter in answer:
    print(letter)
while True:
  answer = input("enter a word. type 'stop' to stop")
  if answer == 'stop':
    break
  else:
    word_list.append(answer)
    split_word()
  