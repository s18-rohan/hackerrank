
def max_frequency_word_counter(data):
    # break the string into list of words  
    str =data.split()          
    str2 = [] 
    for i in str:              
        if i not in str2: 
            str2.append(i) 
    j=[]
    n=[]
    ma=0
    for i in range(0, len(str2)): 
        #print('Frequency of', str2[i], 'is :',(str.count(str2[i])))
        m=(str.count(str2[i]))
        if(ma<m):
            ma=m
        j.append((str.count(str2[i])))
        #print(str2[i])
    print(str2[m],max(j))
    
    
    
        
#Provide different values for data and test your program.
data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)
