#Time, space complexity O(n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
  #Creating queue      
        f=0
        q=deque()
   #Traversing through grid if we find rotten oranges calling dfs otherwise counting fresh oranges     
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    f+=1
                    
        c=0
    #Traversing through the queue until we have fresh oranges
        while q and f>0:
    #For maintaining level
            for i in range(len(q)):
                x,y=q.popleft()
                
                for i,j in [(0,-1),(0,1),(1,0),(-1,0)]:
                    xx=x+i
                    yy=y+j
                    
                    if xx<0 or xx>=len(grid) or yy<0 or yy>=len(grid[0]) or grid[xx][yy]==2 or grid[xx][yy]==0:
                        continue
                    q.append([xx,yy])
                    grid[xx][yy]=2
                    f-=1
  #incrementing time after each level                  
            c+=1
            
        return c if f==0 else -1
                    
