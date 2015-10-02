from tkinter import *;
from DataFile import *;
from graph import *;


global UNDOARRAY;
UNDOARRAY = [];

global REDOARRAY;
REDOARRAY = [];

#---------------------------------------------MENÚ-------------------------------------------------#

global WIDTH;
WIDTH = 1280;
global HEIGHT;
HEIGHT= 700;

window = Tk();
window.title("Torre de Babilonia");
window.geometry(str(WIDTH) + "x" + str(HEIGHT));

canvas = Canvas(window, width = WIDTH, height = HEIGHT);
canvas.pack();
canvas.create_rectangle(0,0,WIDTH,HEIGHT, fill="white");

title_lbl = Label(window, text = "I Proyecto I.A, Torre de Babilonia",
                  font = ('Arial','17'), background = 'white');
title_lbl.place(x = 270, y = 50);

foptions = {};
foptions['defaultextension'] = '.txt';
foptions['filetypes'] = [('Todos los archivos','.*'),('Archivos de texto','.txt')];

boptions = {};
boptions['background'] = 'white';
boptions['borderwidth'] = '0';


boptions2 = boptions.copy();
boptions2['activebackground'] = 'white';
boptions2['activeforeground'] = '#545454';
boptions2['borderwidth'] = '1';
boptions2['padx'] = '5';
boptions2['pady'] = '5';
boptions2['relief'] = 'ridge';
boptions2['cursor'] = 'hand2';

undo_btn = Button(window, **boptions);
undo_img = PhotoImage(file = "imgs/undo.gif", width= 25, height = 25);
undo_btn.configure(image = undo_img);
#undo_btn.place(x = WIDTH - 225, y = 40);

undo_lbl = Label(window, text="Deshacer", font=('Arial','8'), background='white');
#undo_lbl.place(x = WIDTH - 240, y = 70);

redo_btn = Button(window, **boptions);
redo_img = PhotoImage(file = "imgs/redo.gif", width= 25, height = 25);
redo_btn.configure(image = redo_img);
#redo_btn.place(x = WIDTH - 175, y = 40);

redo_lbl = Label(window, text="Rehacer", font=('Arial','8'), background='white');
#redo_lbl.place(x = WIDTH - 183, y = 70);

reset_btn = Button(window, text="Reiniciar", command = lambda: reset(), **boptions2);
reset_btn.place(x = 400, y = 140);

save_btn = Button(window, text=" Guardar", command = lambda: save(), **boptions2);
save_btn.place(x = 400, y = 180);

save_btn = Button(window, text=" Ejecutar", command = lambda: execute(), **boptions2);
save_btn.place(x = 400, y = 220);

#-------------------------------------FILAS Y COLUMNAS--------------------------------------------#

canvas.create_rectangle(25, 100, 825,HEIGHT - 50, fill="#fafafa", outline = 'white');

init_state_lbl = Label(window, text = "Estado Inicial",
                       font = ('Arial','17'), background='#fafafa');
init_state_lbl.place(x = 160, y = 150);

final_state_lbl = Label(window, text = "Estado Final",
                        font = ('Arial', '17'), background='#fafafa');
final_state_lbl.place(x = 585, y = 150);

init_state_file_btn = Button(window, text = "Cargar estado inicial desde archivo", command = lambda: openFile(0), **boptions2);
init_state_file_btn.place(x = 130, y = 190);

final_state_file_btn = Button(window, text = "Cargar estado final desde archivo", command = lambda: openFile(1), **boptions2);
final_state_file_btn.place(x = 560, y = 190);

arriba = PhotoImage(file = 'imgs/up.png');
abajo = PhotoImage(file = 'imgs/down.png');
izquierda = PhotoImage(file = 'imgs/left.png');
derecha = PhotoImage(file = 'imgs/right.png');

blanco = PhotoImage(file = 'imgs/blanco2.png');
azul = PhotoImage(file = 'imgs/azul2.png');
naranja = PhotoImage(file = 'imgs/naranja2.png');
rojo = PhotoImage(file = 'imgs/rojo2.png');
verde = PhotoImage(file = 'imgs/verde2.png');

blancoA = PhotoImage(file = 'imgs/blanco3.png');
azulA = PhotoImage(file = 'imgs/azul3.png');
naranjaA = PhotoImage(file = 'imgs/naranja3.png');
rojoA = PhotoImage(file = 'imgs/rojo3.png');
verdeA = PhotoImage(file = 'imgs/verde3.png');

colores = [azul, naranja, verde, rojo, blanco, azulA, naranjaA, verdeA, rojoA, blancoA];
colores_lbl = ["Azul(B)", "Naranja(O)","Verde(G)","Rojo(R)","Vacío(H)"];


for c in range(0, 5):
#{
    ball = Label(window, **boptions);
    ball.configure(image = colores[c]);
    ball.place(x = 180 + (100 * c), y = 600);

    lbl = Label(window, text = colores_lbl[c], font=('Arial','8'), background='#fafafa');
    lbl.place(x = 215 + (100 * c), y = 605);
#}
    

boptions['background'] = '#fafafa';
boptions['cursor'] = 'hand2';

estados = [[],[], [-1,-1,-1]];  # 0 -> inicial, 1 -> final, 2 -> seleccionado
flechas = [[],[]];

xInicial = 75;
yInicial = 250;

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

def toggleBtn(fila, col, estado, action):
#{
    for color in range(0,len(colores)):
        if(str(colores[color]) == str(estados[estado][fila][col].cget('image'))):
            estados[estado][fila][col].configure(image = colores[color + (5 * action)]);
            return;
            
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
        toggleBtn(fila, col, estado, 1);
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

        toggleBtn(fila, col, estado, -1);
        
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
        #print(fila);
        flechas[estado][col + (fila - 1)][0].place_forget();
            
#}

def getPosMuesca(estado):
#{
    for fila in range(1,6):
        for col in range(0,4):
            if(str(estados[estado][fila][col].cget('image')) == str(blanco)):
                return [fila,col];
    return -1;
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
        if posMuesca != -1:
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

#------------------------------------------ERRORES------------------------------------------------#

canvas.create_line(840, 75 , 840, HEIGHT - 25, fill="#777777")

canvas.create_rectangle(855, 100, 1255, HEIGHT - 50, fill="#efefef", outline = 'white');

errors_lbl = Label(window, text = "Log de Errores",
                   font=('Arial','13'), background='#efefef');
errors_lbl.place(x = 990, y = 115);

scrollbar = Scrollbar(window);

errors_listbox = Listbox(window, width = 45, height = 24, bd = 0,
                         font = ('Arial','11'),
                         yscrollcommand = scrollbar.set);
errors_listbox.place(x = 875, y = 150);

scrollbar.config(command = errors_listbox.yview);

error_help = Button(window, text = "Explorar error",
                    command = lambda : explore_error() ,**boptions2);
error_help.place(x = 1020, y = HEIGHT - 100);

def printErrorMsg(msg):
#{
    errors_listbox.insert(END, msg);
    errors_listbox.see("end");
#}

def explore_error():
#{
    selected_index = errors_listbox.curselection();
    if(len(selected_index) == 0):
        printErrorMsg("Seleccione primero un error para ver más detalles");
    else:
        error = errors_listbox.get(selected_index);
        explanation = "";
        if(error == "Seleccione primero un error para ver más detalles"):
            explanation = "Para poder ver la información respecto a un error, es necesario hacer click al texto del error";
        elif(error == "Muesca mal colocada o cantidad incorrecta de bolitas"):
            explanation = "En el archivo de texto se colocó una cantidad menor o mayor que 4 bolitas de colores o más de 1 muesca vacía.\nRecuerde que el máximo número de bolitas de colores permitido es de 4 para cada color y solamente una muesca o espacio vacío";
        else:
            explanation = "En el archivo de texto se ingresaron incorrectamente las filas, ya sea porque hay filas repetidas o tienen asignado un número mayor o inferior para la fila.\nRecuerde que el formato para las filas es F1, F2, F3 y F4";

        
        messagebox.showinfo("Detalles del error", error + ":\n\n" + explanation);
#}



#--------------------------------------FUNCIONES DEL MENÚ-----------------------------------------

color_value = ["Blue","Orange","Green","Red","Space"];

def openFile(state):
#{
    filename = filedialog.askopenfilename(**foptions);
    #print(filename, state);
    matrix = load_matrix(filename);

    if isinstance(matrix, str):
        printErrorMsg(matrix);
    else:
        matrizTranspuesta(matrix,state);

    
    clear_variables();
#}

def reset_state():
#{
    for estado in range(0,2):
            for fila in range (1,6):
                for col in range(0,4):
                    #print(estados[estado][fila][col]);
                    estados[estado][fila][col].place_forget();
    moveArrows(-100,0,0);
    iniciarInterfaz(); 
#}

def reset():
#{
    if(messagebox.askokcancel("Alerta!","Desea reiniciar los estados?")):
        global matrix_tuple;
        matrix_tuple = ();
        reset_state();
        errors_listbox.delete(0, END);
#}

def get_index(btn):
#{
    for i in range(0, len(colores)):
        if( str(colores[i]) == btn ):
            return i;
    return -1;
            
#}

def write_file(state):
#{
    filenames = ["est_inicial.txt","est_final.txt"];
    file = open(filenames[state], mode = 'w');
    letters = ["B","O","G","R","H"];

    for col in range(0,4):
        file.write("F" + str(col + 1) + "=");
        for row in range(5,0,-1):                        
            index = get_index(str(estados[state][row][col].cget('image')));
            if index != -1:                
                if row > 1:
                    file.write(letters[index]);
                if row > 2:
                    file.write(',');
                elif row == 1:
                    file.write(',' + letters[index]);
                                    
        file.write("\n");
    
    file.close();                
#}

def save():
#{
    if(messagebox.askokcancel("Alerta!","Desea guardar los estados?" +
                              "\nEl archivo anterior sera sobreescrito")):
        for state in range(0,2):
            write_file(state);
    
#}

def tuplify(state):
#{    
    new_tuple = ();

    for row in range(1,6):
        new_row = ();
        for col in range(0,4):
            index = get_index(str(estados[state][row][col].cget('image')));
            new_row += (index,);

        new_tuple += (new_row,);        

    return new_tuple;
#}

def execute():
#{
    if(messagebox.askokcancel("Alerta!","Desea ejecutar el algoritmo?" +
                              "\nNo podrá volver a modificar los estados")):
    #{
        initial_state_tuple = tuplify(0);
        final_state_tuple = tuplify(1);        
        start = time.time();
        parents,cost_so_far = a_star_search(initial_state_tuple, final_state_tuple);
        end = time.time();
        reconstruct_path(parents,initial_state_tuple, final_state_tuple);

    #}
#}

def matrizTranspuesta(matrix, state):
#{
    new_matrix = [];

    for row in range(4,-1,-1):
    #{
        new_row = [];        
        for col in range(0,4):            
            value = matrix[col][row]; 
            if row != 4:                                
                new_row.append(value);
            elif value != -1:                
                new_row.append([value,col]);            
    
        new_matrix.append(new_row);
    #}
    loadState(new_matrix.copy(), state);
#}

def loadState(new_matrix, state):
#{    
    for row in range(0,5):    
        for col in range(0,len(new_matrix[row])):
            if(row != 0):
                value = new_matrix[row][col];
                if(value == 4):                    
                    moveArrows(0, col, state);
                    updateMov(row + 1,col,state);
                estados[state][row + 1][col].configure(image = colores[value]);
            else:                
                value = new_matrix[0][0][0];
                ball_pos = new_matrix[0][0][1];                
                estados[state][1][0].configure(image = colores[value]);
                for x in range(0,ball_pos):
                    moveH(1,-1,state);    
#}                    
                    
#--------------------------------------------MAIN-----------------------------------------------

iniciarInterfaz();






























