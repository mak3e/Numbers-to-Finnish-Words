basic={"0": "nolla", "1": "yksi", "2": "kaksi", "3": "kolme", "4": "neljä", "5": "viisi", "6": "kuusi", "7": "seitsemän", "8": "kahdeksan", "9": "yhdeksän"}
tens={1: ("kymmentä", "kymmenen", "toista"), 2: ("sataa", "sata"), 3: ("tuhatta", "tuhat")}


# generate finnish words for number num (str)    
def numtowords(num):
    if num in basic.keys():
        return basic[num]
    nums=list(num)
    words=[]
    for n in nums:
        if n != "0":
            words.append(numtowords(n))
    for i in range(len(words)):
        if i > 0:
           ext=tens[(i-1)%3+1]
           if words[-i-1] != numtowords("1"):
               words[-i-1]+=ext[0]
           else:
               if i==1:
                   words[-1]+=ext[2]
                   words[-i-1]=""
               else:
                   words[-i-1]=ext[1]
    return "".join(words)


# number letter count sequence for https://youtu.be/LYKn0yUTIU4
def main():
    for start in range(1,1000):
        num=start
        nums=[]
        while(num not in nums):
            print(str(num)+" - "+numtowords(str(num)))
            nums.append(num)
            num=len(numtowords(str(num)))
        print("loops: " + str(num))
        
if __name__ == "__main__":
    main()
    