hn = dict()
gn_node = dict()
gn = dict()

total = int(input("Enter total number of nodes: "))

for i in range(total):
    
    temp = dict()
    node = input("Enter node: ")
    hn_value = int(input("Enter value for hn: "))
    
    hn[node] = hn_value
    
    n = int(input("Enter num of neighbouring nodes: "))

    for j in range(n):

        neighbour = input("Enter neighbouring node: ")
        gn_value = int(input("Enter value for gn: "))

        temp[neighbour] = gn_value
        print("GN_NODE = ", j, " = ", temp)
        gn[node] = temp

print("HN = ", hn)
print("GN = ", gn)
start = input("Enter starting node: ")
goal = input("Enter goal node: ")
result = ''
import queue as Q


def get_fn(varstr): 
    var=varstr.split(" , ") 
    hn1=gn1=0
    for ctr in range(0, len(var)-1):
        gn1=gn1+dict_gn[var[ctr]][var[ctr+1]] 
        hn1=dict_hn[var[len(var)-1]] 
    return(hn1+gn1)

def expand(queue): 
    global result
    total, varstr, thisVar=queue.get() 
    if thisVar==goal:
        result=varstr+" : : "+str(total)
        return

    for cty in dict_gn[thisVar]:
        queue.put((get_fn(varstr+" , "+cty), varstr+" , "+cty, cty)) 
    expand(queue)


def main():
    queue=Q.PriorityQueue() 
    thisVar=start 
    queue.put((get_fn(start),start,thisVar)) 
    expand(queue)
    print("The A* path with the total is: ") 
    print(result)

main()
