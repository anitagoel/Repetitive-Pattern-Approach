import json

def lambda_handler(event, context):
    # TODO implemen
    N=event['Num']
    d=event['Jstring']
    print(type(d))
    if isinstance(d, str):
        jst=d
    else:
        jst=json.dumps(d)
        
    
    
    print("++++++++++++++++++++Alok++++++++++++++++++++++++")
    print(jst)
    print("++++++++++++++++++++Alok++++++++++++++++++++++++")
    N=int(N)
    R= N*N
    #print(N)
    returnData = '{'
    A=[]
    B=[]
    jarray=json.loads(jst)
    #print(jarray)
    
    for i in range(R):
        A.append('N'+str(i))
        B.append('M'+str(i))
         #temp[i]='N'
        #print(A[i])
        #print(B[i])
    
    #for i in range(R):
        #print(jarray[A[0]])
    k=0
    
    first_list = []   
    second_list = []
    result = []
    for i in range (0, N):                               
        new1 = []   
        new2 = []
        new3 = []
        for j in range (0, N):    
            new1.append(jarray[A[k]])
            new2.append(jarray[B[k]])
            new3.append(0)
            k=k+1
            #print(new[j])
        first_list.append(new1)  
        second_list.append(new2)
        result.append(new3)
    
    #print(first_list[1][1])  
    #print(second_list[1][1])
    
    for i in range(0, N):  
        for j in range(0, N): 
            for k in range(0, N):  
                result[i][j] +=first_list[i][k] * second_list[k][j]  
                
    for i in range(0, N):  
        for j in range(0, N):             
            #print(result[i][j])    
            if i == 0 and j == 0:
                returnData += ' N'+str(i)+str(j)+':'+str(result[i][j])
            else :
                returnData += ', N'+str(i)+str(j)+':'+str(result[i][j])
    
    returnData += '}'
    json_dump = json.dumps(returnData)
    #print(json_dump)
    
    return json_dump
