from BFS import bfs

start=[[0,0],[0,1],[0,2]]
print("test 1:")
lab =[[".",".",".",".",".",".",".",".","."],
["#",".",".",".","#",".",".",".","."],
[".",".",".",".","#",".",".",".","."],
[".","#",".",".",".",".",".","#","."],
[".","#",".",".",".",".",".","#","."]]
solucion1=bfs(lab,start)
print(f"El laberinto:\n {lab}\n La solucion es :  {solucion1}\n ")

print("test 2:")
lab =[[".",".",".",".",".",".",".",".","."],
["#",".",".",".","#",".",".","#","."],
[".",".",".",".","#",".",".",".","."],
[".","#",".",".",".",".",".","#","."],
[".","#",".",".",".",".",".","#","."]]

solucion2=bfs(lab,start)
print(f"El laberinto:\n {lab}\n La solucion es :  {solucion2}\n ")

print("test 3:")
lab =[[".",".","."],
[".",".","."],
[".",".","."]]

solucion2=bfs(lab,start)
print(f"El laberinto:\n {lab}\n La solucion es :  {solucion2}\n ")

print("test 4:")
lab =[[".",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".","#",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".","#",".",".",".","#",".",".",".","."],
[".",".",".",".",".",".","#",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."]]
solucion2=bfs(lab,start)
print(f"El laberinto:\n {lab}\n La solucion es :  {solucion2}")