
def labyrinth(lab):
    rod_pos=[(0,0),(0,1),(0,2)]
lab =[[".",".",".","."],[".",".",".","."],[".",".",".","."],[".",".",".","."]]
rod_pos=[[0,0],[0,1],[0,2]]

def move_right(rod_pos,lab):
    if rod_pos[2][0]+1<len(lab[1]): 
        match comprobar_lados(rod_pos,lab,"r"):
            case 1:
                rod_pos=[rod_pos[1],rod_pos[2],[rod_pos[2][0],rod_pos[2][1]+1]]
                return rod_pos
            case 2:
                rod_pos=[[rod_pos[0][0],rod_pos[0][1]+1],[rod_pos[1][0],rod_pos[1][1]+1],[rod_pos[2][0],rod_pos[2][1]+1]]
                return rod_pos
            case -1:
                return -1
    else:
        return -1
        
def move_left(rod_pos,lab):
    if rod_pos[0][0]-1>=0: 
        match comprobar_lados(rod_pos,lab,"l"):
            case 1:
                rod_pos=[[rod_pos[0][0],rod_pos[0][1]-1],rod_pos[0],rod_pos[1]]
                return rod_pos
            case 2:
                rod_pos=[[rod_pos[0][0],rod_pos[0][1]-1],[rod_pos[1][0],rod_pos[1][1]-1],[rod_pos[2][0],rod_pos[2][1]-1]]
                return rod_pos
            case -1:
                return -1
    else:
        return -1
        
def move_up(rod_pos,lab):
    if rod_pos[0][1]-1>=0:
        match comprobar_altura(rod_pos,lab,"u"):
            case 1:
                rod_pos=[[rod_pos[0][0]-1,rod_pos[0][1]],rod_pos[0],rod_pos[1]]
                return rod_pos
            case 2:
                rod_pos=[[rod_pos[0][0]-1,rod_pos[0][1]],[rod_pos[1][0]-1,rod_pos[1][1]],[rod_pos[2][0]-1,rod_pos[2][1]]]
                return rod_pos
            case -1:
                return -1
    else:
        return -1
        
def move_down(rod_pos,lab):
    if rod_pos[2][0]+1<len(lab):
        match comprobar_altura(rod_pos,lab,"d"):
            case 1:
                rod_pos=[rod_pos[1],rod_pos[2],[rod_pos[2][0]+1,rod_pos[2][1]]]
                return rod_pos
            case 2:
                rod_pos=[[rod_pos[0][0]+1,rod_pos[0][1]],[rod_pos[1][0]+1,rod_pos[1][1]],[rod_pos[2][0]+1,rod_pos[2][1]]]
                return rod_pos
            case -1:
                return -1
    else:
        return -1
        
def rotar(rod_pos,lab):
    ini_x=rod_pos[1][0]-1
    ini_y=rod_pos[1][1]-1
    fin_x=rod_pos[1][0]+1
    fin_y=rod_pos[1][1]+1
    if ini_x>=0 and ini_y>=0 and fin_x<len(lab) and fin_y<len(lab[1]):
        for i in range(0,3):
            for j in range(0,3):
                if lab[ini_x+i][ini_y+j]=="#":
                    return -1
        return 1
    else:
        return -1
    
def comprobar_lados(rod_pos,lab,lado):
    if lado=="r":
        sum=1
    else:
        sum=-1
    if rod_pos[1][0]==rod_pos[2][0]:
            if lab[rod_pos[1][0]][rod_pos[1][1]+sum+sum]==".":
                return 1
            else:
                return -1
    else:
        if lab[rod_pos[0][0]][rod_pos[0][1]+sum]=="."and lab[rod_pos[1][0]][rod_pos[1][1]+sum]=="." and lab[rod_pos[2][0]][rod_pos[2][1]+sum]==".":
            return 2
        else:
            return -1

def comprobar_altura(rod_pos,lab,lado):
    if lado=="d":
        sum=1
    else:
        sum=-1
    if rod_pos[1][0]==rod_pos[2][0]:
        if lab[rod_pos[0][0]+sum][rod_pos[0][1]]=="."and lab[rod_pos[1][0]+sum][rod_pos[1][1]]=="." and lab[rod_pos[2][0]+sum][rod_pos[2][1]]==".":
            return 2
        else:
            return -1
    else:
        if lab[rod_pos[1][0]+sum+sum][rod_pos[1][1]]==".":
            return 1
        else:
            return -1