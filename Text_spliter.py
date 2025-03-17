
def split_text(text):
    splitted_text=[]
    for i in range(0,len(text),28):
        try:
            splitted_text.append(text[i:i+28])
        except:
            splitted_text.append(text[i:])
            return splitted_text
    return splitted_text
        
def ASCII2text(nums:int,step:int):
    text=[]
    for i in range(0,len(nums),step):
        text.append(chr(int(nums[i:i+step])))
    return text
           
    


def text2ASCII(text:str)-> list:
    nums=[]
    for symb in text:
        nums.append(str(ord(symb)))
    
    lenghts=[len(i) for i in nums]
    new_nums=[]
    for num in nums:
        while len(num)<max(lenghts):
            num='0'+num
        new_nums.append(num)
    return new_nums,max(lenghts)