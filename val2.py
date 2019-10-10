class validate:
    def __init__(self):
        pass
    def check(self,myStr):
        open_list = ["[","{","("] 
        close_list =["]","}",")"] 
        stack=[]
        for i in myStr:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos=close_list.index(i)
                if ((len(stack)>0) and (open_list[pos]==stack[len(stack)-1])):
                   stack.pop()       
            else:
                print("invalid")
                   
        if not(stack):
            print("valid")
        else:
            print("invalid")
                   
str="({[()]})"
ob=validate()
ob.check(str)
            
        
