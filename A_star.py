def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a_star(grid , start, goal):
    open_list=[(0+heuristic(start,goal),0,start,[start])]
    visited=set()

    while open_list:
        open_list.sort()

        _,cost,curr,path=open_list.pop(0)

        if curr in visited:
            continue
        visited.add(curr)

        if curr==goal:
            return path
        
        x,y=curr

        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny=x+dx,y+dy

            if 0<=nx< len(grid) and 0<=ny<len(grid[0]):
                if grid[nx][ny]==0 and (nx,ny) not in visited:
                    open_list.append((cost+1+heuristic((nx,ny),goal),cost+1,(nx,ny),path+[(nx,ny)]))

    return None

grid=[
    [0,1,0],
    [0,1,0],
    [0,0,0]
]

start=(0,0)
goal=(2,2)

print(a_star(grid,start,goal))