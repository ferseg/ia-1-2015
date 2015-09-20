from tkinter import *;

global UNDOARRAY;
UNDOARRAY = [];

global REDOARRAY;
REDOARRAY = [];

#---------------------------------------------MENÚ-------------------------------------------------#

global WIDTH;
WIDTH = 1000;
global HEIGHT;
HEIGHT= 700;

window = Tk();
window.title("Torre de Babilonia");
window.geometry(str(WIDTH) + "x" + str(HEIGHT));

canvas = Canvas(window, width = WIDTH, height = HEIGHT);
canvas.pack();
canvas.create_rectangle(0,0,WIDTH,HEIGHT, fill="white");

foptions = {};
foptions['defaultextension'] = '.txt';
foptions['filetypes'] = [('Todos los archivos','.*'),('Archivos de texto','.txt')];

def openFile():
#{
    filename = filedialog.askopenfilename(**foptions);
    print(filename);
#}

boptions = {};
boptions['background'] = 'white';
boptions['borderwidth'] = '0';
boptions['cursor'] = 'hand2';

boptions2 = boptions.copy();
boptions2['activebackground'] = 'white';
boptions2['activeforeground'] = '#545454';
boptions2['borderwidth'] = '1';
boptions2['padx'] = '5';
boptions2['pady'] = '5';
boptions2['relief'] = 'ridge';

open_file_btn = Button(window, text = "Abrir Archivo", command = lambda: openFile(), **boptions2);
open_file_btn.place(x = 75, y = 40);

undo_btn = Button(window, **boptions);
undo_img = PhotoImage(file = "imgs/undo.gif", width= 25, height = 25);
undo_btn.configure(image = undo_img);
undo_btn.place(x = WIDTH - 225, y = 40);

undo_lbl = Label(window, text="Deshacer", font=('Arial','8'), background='white');
undo_lbl.place(x = WIDTH - 240, y = 70);

redo_btn = Button(window, **boptions);
redo_img = PhotoImage(file = "imgs/redo.gif", width= 25, height = 25);
redo_btn.configure(image = redo_img);
redo_btn.place(x = WIDTH - 175, y = 40);

redo_lbl = Label(window, text="Rehacer", font=('Arial','8'), background='white');
redo_lbl.place(x = WIDTH - 183, y = 70);

reset_btn = Button(window, text="Reset", command = lambda: reset(), **boptions2);
reset_btn.place(x = WIDTH - 125, y = 40);


#-------------------------------------FILAS Y COLUMNAS--------------------------------------------#

canvas.create_rectangle(50,100,WIDTH - 50,HEIGHT - 100, fill="#fafafa", outline = 'white');

init_state_lbl = Label(window, text = "Estado Inicial",
                       font = ('Arial','17'), background='#fafafa');
init_state_lbl.place(x = 220, y = 150);
final_state_lbl = Label(window, text = "Estado Final",
                        font = ('Arial', '17'), background='#fafafa');
final_state_lbl.place(x = 640, y = 150);
boptions['background'] = '#fafafa';

arriba = PhotoImage(file = 'imgs/up.png');
abajo = PhotoImage(file = 'imgs/down.png');
izquierda = PhotoImage(file = 'imgs/left.png');
derecha = PhotoImage(file = 'imgs/right.png');

blanco = PhotoImage(file = 'imgs/blanco2.png');
azul = PhotoImage(file = 'imgs/azul2.png');
naranja = PhotoImage(file = 'imgs/naranja2.png');
rojo = PhotoImage(file = 'imgs/rojo2.png');
verde = PhotoImage(file = 'imgs/verde2.png');

colores = [azul, naranja, rojo, verde];

estados = [[],[], [-1,-1,-1]];  # 0 -> inicial, 1 -> final, 2 -> seleccionado
flechas = [[],[]];

xInicial = 150;
yInicial = 225;

def iniciarInterfaz():

    estados[0] = [];
    estados[1] = [];
    estados[2] = [-1,-1,-1];

    flechas[0] = [];
    flechas[1] = [];

    for y in range(0,7):
    #{
        filaI = [];
        filaF = [];
        noAgregar = False;
        
        for x in range(0,6):
        #{
            if 0 < x < 5 and 0 < y < 6:            
                bolaI = Button(window, command = lambda y = y,x = x: selectBtn(y,x - 1,0), **boptions);
                bolaF = Button(window, command = lambda y = y,x = x: selectBtn(y,x - 1,1), **boptions);
                if y != 1:
                    bolaI.configure(image = colores[x - 1]);
                    bolaF.configure(image = colores[x - 1]);                
                elif x == 1:
                    bolaI.configure(image = blanco);
                    bolaF.configure(image = blanco);                

                bolaI.place(x = (xInicial + (50 * x)), y = (yInicial + (50 * y)));
                bolaF.place(x = (xInicial + 415 + (50 * x)), y = (yInicial + (50 * y)));

                if(not noAgregar):
                    filaI.append(bolaI);
                    filaF.append(bolaF);            
                
            else:            
                isMuesca = False;
                flechaI = Button(window, **boptions);
                flechaF = Button(window, **boptions);
            
                if x == 0 and y != 0 and y != 6:
                    flechaI.configure(command = lambda y = y: moveH(y,1,0));
                    flechaI.configure(image = izquierda);
                    flechaF.configure(command = lambda y = y: moveH(y,1,1));
                    flechaF.configure(image = izquierda);
                elif x == 5 and y != 0 and y != 6:
                    flechaI.configure(command = lambda y = y: moveH(y,-1,0));
                    flechaI.configure(image = derecha);
                    flechaF.configure(command = lambda y = y: moveH(y,-1,1));
                    flechaF.configure(image = derecha);
                elif y == 0 and x != 0 and x != 5:
                    flechaI.configure(command = lambda x = x: moveV(x,-1,0));
                    flechaI.configure(image = arriba);
                    flechaF.configure(command = lambda x = x: moveV(x,-1,1));
                    flechaF.configure(image = arriba);
                    isMuesca = True;
                elif y == 6 and x != 0 and x != 5:
                    flechaI.configure(command = lambda x = x: moveV(x,1,0));
                    flechaI.configure(image = abajo);
                    flechaF.configure(command = lambda x = x: moveV(x,1,1));
                    flechaF.configure(image = abajo);
                    isMuesca = True;

                if(not isMuesca or isMuesca and x == 1 and y == 6):
                    flechaI.place(x = (xInicial + (50 * x)), y = (yInicial + (50 * y)));
                    flechaF.place(x = (xInicial + 415 + (50 * x)), y = (yInicial + (50 * y)));            
                if isMuesca:
                    flechas[0].append([flechaI,y,x]);
                    flechas[1].append([flechaF,y,x]);
                    
        #}       
        estados[0].append(filaI);
        estados[1].append(filaF);
        
    #}

def selectBtn(fila, col, estado):
#{
    #print(estados[-1]);
    if estados[-1][-1] != -1:
        res = moveBtn(fila, col, estado);        
        if res == 1:
            estados[-1] = [-1,-1,-1];
        return;        
    if(str(estados[estado][fila][col].cget('image')) != str(blanco)):
        estados[-1] = [fila, col, estado];
#}


def moveBtn(fila, col, estado):
#{
    if estados[-1][-1] == estado:
        #print("OK");
        filaAnt = estados[-1][0];
        colAnt = estados[-1][1];

        posActualMuesca = rowHasEmptySpace(filaAnt,estado);
        
        prevImg = estados[estado][filaAnt][colAnt].cget('image');
        currImg = estados[estado][fila][col].cget('image');

        if(str(currImg) == str(blanco)):
            return -1;
                                                  
        estados[estado][fila][col].configure(image = prevImg);
        estados[estado][filaAnt][colAnt].configure(image = currImg);

           
        
        return 1;
    else:
        print("ERROR");
        return -1;        
#}

def rowHasEmptySpace(fila, estado):
#{
    for col in range(0,4):        
        if str(estados[estado][fila][col].cget('image')) == str(blanco):
            return col;
    return -1;
#}

def colHasEmptySpace(col, estado):
#{    
    for fila in range(1,6):        
        if str(estados[estado][fila][col - 1].cget('image')) == str(blanco):
            return fila;
    return -1;
#}

def moveArrows(posMuesca, col, estado):
#{        
    if posMuesca >= 0:
        flechas[estado][posMuesca][0].place_forget();
        flechas[estado][posMuesca + 4][0].place_forget();
        
        flechas[estado][col][0].place(x = (xInicial+(415*estado)+(50 * flechas[estado][col][2])),
                                      y = (yInicial + (50 * flechas[estado][col][1])));
        flechas[estado][col + 4][0].place(x =(xInicial+(415*estado)+(50*flechas[estado][col+4][2])),
                                      y = (yInicial + (50 * flechas[estado][col + 4][1])));

    elif posMuesca == -100:
        for est in flechas:
            for flecha in est:
                flecha[0].place_forget();
        
        
        
#}

def updateMov(fila, col, estado):
#{
            
    if(fila != 1 and fila != 5 and str(estados[estado][fila-1][col].cget('image')) != ''):
        flechas[estado][col][0].place(x = (xInicial+(415*estado)+(50 * flechas[estado][col][2])),
                                      y = (yInicial + (50 * flechas[estado][col][1])));
        flechas[estado][col + 4][0].place(x = xInicial+(415*estado)+(50*flechas[estado][col+4][2]),
                                          y = (yInicial + (50 * flechas[estado][col+4][1])));
    elif(fila == 2):        
        flechas[estado][col][0].place_forget();
    else:
        print(fila);
        flechas[estado][col + (fila - 1)][0].place_forget();
            
#}

def getPosMuesca(estado):
#{
    for fila in range(1,7):
        for col in range(0,4):
            if(str(estados[estado][fila][col].cget('image')) == str(blanco)):
                return [fila,col];
#}

def moveH(fila, dire, estado):
#{
    estados[-1] = [-1,-1,-1];
    
    posActualMuesca = rowHasEmptySpace(fila, estado);

    currState = [];    
    
    for col in range(0,4):
        
        currState.append(estados[estado][fila][col].cget('image'));

    for col in range(0,4):

        pos = col + dire;
        if pos == 4:
            pos = 0;

        nextImg = currState[pos];
        estados[estado][fila][col].configure(image = nextImg);

    nuevaPos = rowHasEmptySpace(fila, estado);
    moveArrows(posActualMuesca, nuevaPos, estado);    
    
    if(nuevaPos != -1):
        updateMov(fila, nuevaPos, estado);
    else:
        posMuesca = getPosMuesca(estado);
        updateMov(posMuesca[0], posMuesca[1], estado);
        
    
#}

def moveV(col, dire, estado):
#{
    estados[-1] = [-1,-1,-1];
    
    posActualMuesca = colHasEmptySpace(col, estado);        

    posSiguiente = posActualMuesca + dire;
    
    if (posSiguiente) < 1:
        posSiguiente = 1;
    elif (posSiguiente) > 5:
        posSiguiente = 5;

    nextImg = estados[estado][posSiguiente][col - 1].cget('image');

    if(str(nextImg) != ''):
        estados[estado][posSiguiente][col - 1].configure(image = blanco);
        estados[estado][posActualMuesca][col - 1].configure(image = nextImg);

    updateMov(posSiguiente, col - 1, estado);

#}


#--------------------------------------FUNCIONES DEL MENÚ-----------------------------------------


def undo():
#{
    print("undo",UNDOARRAY);
#}

def redo():
#{
    print("redo",REDOARRAY);
#}

def action():
#{
    print("action");
#}

def reset():
#{
    if(messagebox.askokcancel("Alerta!","Desea reiniciar los estados?")):
        moveArrows(-100,0,0);
        iniciarInterfaz();        
#}


#--------------------------------------------MAIN-----------------------------------------------

iniciarInterfaz();


































