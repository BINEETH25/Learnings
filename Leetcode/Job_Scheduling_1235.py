def Job_Scheduling(startTime, endTime, profit):
    
    Jobs = sorted(zip(startTime, endTime, profit), key = lambda x : x[1])
    result_map = {}
    profit = Jobs[0][2]
    last_job = Jobs[0][1]
    
    for i in range(1, len(Jobs)):
        if Jobs[i][0] >= last_job:
            last_job = Jobs[i][1]
            profit += Jobs[i][2]
    return profit
    

startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]

print(Job_Scheduling(startTime, endTime, profit))