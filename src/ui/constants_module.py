B = 0
O = 1
G = 2
R = 3
H = 4
E = -1



NOTCH_SYMBOL = 4
UP = -1
DOWN = 1
RIGHT = 1
LEFT = -1

COST = {}

COST[0] = 54
COST[1] = 18
COST[2] = 9
COST[3] = 3
COST[4] = 1




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
