
def split_text(text):
    splitted_text=[]
    for i in range(0,len(text),4):#?????????????????????????????????????
        try:
            splitted_text.append(text[i:i+4])#?????????????????????????????????
        except:
            splitted_text.append(text[i:])
            return splitted_text
    return splitted_text
        
def ASCII2text(nums:int):
    text=[]
    for i in range(0,len(nums),6):
        
        text.append(chr(int(nums[3:6])))
        nums=nums[6:]

        #text.append(chr(int(nums[i+3:i+6])))
    return text
           
    


# def text2ASCII(text:str)-> list:
#     nums=[]
#     for symb in text:
#         nums.append(str(ord(symb)))
    
#     lenghts=[len(i) for i in nums]
#     new_nums=[]
#     for num in nums:
#         while len(num)<max(lenghts):
#             num='0'+num
#         new_nums.append(num)
#     return new_nums,max(lenghts)


def text2ASCII(text:str)-> list:
    nums=[]
    for symb in text:
        nums.append(str(ord(symb)))
    new_nums=[]
    for num in nums:
        
        while len(num)<=5:
            
            num='1'+num
        new_nums.append(num)
    
    return new_nums,5