#bottleneck problem

ls=list(map(int,input().split()))
new_ls=[]
for i in ls:
    if i not in new_ls:
        new_ls.append(ls.count(i))
print(max(new_ls))    
     
