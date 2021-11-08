#Time, space complexity O(n)
class Solution:
    imp=0
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        #creating hashmap and mapping id to employees object
        map={}
        
        for i in employees:
            map[i.id]=i
        print(map)
#Creating queue and adding the id to it        
        q=deque()
        q.append(id)
#traversing queue to calculate the importance of the added id and its subordinates        
        while q:
            cur=q.popleft()
            cur=map[cur]   
            self.imp+=cur.importance        
            for i in cur.subordinates:
                q.append(i)
                
        return self.imp
 
