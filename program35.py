
# # # # # # # # # # # # # # # # # # # # # 
#                                       #
#  Name :- Kardile Siddharth Satish     #
#  sub  :- Python Code Practice         #
#                                       #
# # # # # # # # # # # # # # # # # # # # # 

def CountFour(no):
    temp = 0
    flag = 0 
    
    if no < 0:
        no = -no
    
    while no != 0:
        temp = no%10
        no = no/10
        no = int(no)
        if temp == 4:
            flag += 1
            
    if no == 4:
        flag += 1
        
    return flag
        
def main():
    print("Enter a number : ")
    num = int(input())
    
    result = CountFour(num)
    
    print("Frequency of 4 is : ",result)
    
if __name__ == "__main__":
    main()

