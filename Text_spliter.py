
def split_text(text):
    splitted_text=[]
    for i in range(0,len(text),4):
        try:
            splitted_text.append(text[i:i+4])
        except:
            splitted_text.append(text[i:])
            return splitted_text
    return splitted_text
        
def ASCII2text(nums:int,step:int):
    text=[]
    for i in range(0,len(nums),step+1):

        word=int(nums[i:i+step+1])
        bigger=len(str(word))-(step)
        print(word)
        
        word=int(str(word)[bigger:])
        while (200>word>80)==False and (1095>word>1001)==False and (2000>word>1200)==False:

            word=int(str(word)[1:])
        #print(word)
       # [11092]


        text.append(chr(word))
    return text
           
    


def text2ASCII(text:str)-> list:
    nums=[]
    for symb in text:
        nums.append(str(ord(symb)))

    lenghts=[len(txt) for txt in nums]
    new_nums=[]
    for num in nums:
        
        while len(num)<=max(lenghts):
            
            num='9'+num#была 1
        new_nums.append(num)
    
    return new_nums,max(lenghts)