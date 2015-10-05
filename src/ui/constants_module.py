B = 0
O = 1
G = 2
R = 3
H = 4
E = -1

TXT_NAME = "path.txt"
STEP = "Paso #"

COLOR_DIC = {}
COLOR_DIC[-1] = " Wall   "
COLOR_DIC[0]  = " Blue   "
COLOR_DIC[1]  = " Orange "
COLOR_DIC[2]  = " Green  "
COLOR_DIC[3]  = " Red    "
COLOR_DIC[4]  = " Notch  "



SHR_MESSAGE = "Rotación derecha fila %i."
SHL_MESSAGE = "Rotación izquierda fila %i."
NOTCH_DOWN_MESSAGE = "Mover muesca hacia abajo %i espacios."
NOTCH_UP_MESSAGE = "Mover muesca hacia arriba %i espacios."

NOTCH_SYMBOL = 4
UP = -1
DOWN = 1
RIGHT = 1
LEFT = -1

NODE = 0
LABEL = 1

COST = {}

COST[0] = 54/85
COST[1] = 18/85
COST[2] = 9/85
COST[3] = 3/85
COST[4] = 1/85
COST[5] = 1/16

C_COST = {}
C_COST[0] = 0
C_COST[1] = 3
C_COST[2] = 9
C_COST[3] = 18

R_COST = {}
R_COST[0] = 0
R_COST[1] = 6
R_COST[2] = 18
R_COST[3] = 36
R_COST[4] = 108

mat = ((E, H, E, E),
       (B, R, B, O),
       (O, G, O, G),
       (G, B, G, R),
       (R, O, R, B))

mat_swap_v = ((E, H, E, E),
              (B, R, B, O),
              (O, G, O, G),
              (R, B, G, R),
              (G, O, R, B))

mat_swap_h = ((E, H, E, E),
              (B, R, B, O),
              (O, G, O, G),
              (G, B, G, R),
              (O, R, R, B))

matZ = ((E, H, E, E),
        (B, O, G, R),
        (B, O, G, R),
        (B, O, G, R),
        (B, O, G, R))


mat_i = ((0, -1, -1, -1),
         (0, 1, 2, 3),
         (2, 3, 0, 1),
         (0, 1, 2, 3),
         (3, 4, 1, 2))

mat_f = ((-1, -1, -1, 2),
         (3, 0, 1, 0),
         (1, 2, 3, 3),
         (0, 1, 2, 4),
         (1, 2, 3, 0))




mm = ((-1,-1,-1,4),
 (0,0,0,0),
 (1,1,1,1),
 (2,2,2,2),
 (3,3,3,3))


mn = ((-1,-1,-1,4),
 (3,3,3,3),
 (2,2,2,2),
 (1,1,1,1),
 (0,0,0,0))

