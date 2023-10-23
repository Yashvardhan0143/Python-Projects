"""
Z_max --> finding
GIVEN:
    > 2 inequalities (eqns)
    > variables: x1, x2
    > Slag (S) --> add if '<'
               --> subtract if '>'

"""

#function to calculate Cj
def Cj_calc(mat):
    cj = list([None, None])
    for i in range(2, len(mat[0])):
        val = mat[1][0]*mat[1][i] + mat[2][0]*mat[2][i]
        cj.append(val)
    return cj



inequalities = ['<', '>', '<=', '>=']   # possible inequalites in the I/P equation

Zmax = [1, 3, 0, 0]   # represents : Zmax = 1*x1 + 3*x2 + 0*s1 + 0*s2   [s1 and s2value doesnt change at the beginning no matter what]
eqn1 = [3, 6, 8, 2]     # [x1, x2, Xb, inequality] -> represents : 3*x1 + 6*x2 <= 8
eqn2 = [5, 2, 10, 2]    # [x1, x2, Xb, inequality] -> represents : 5*x1 + 2*x2 <= 10


# Eqn1: adding slag variable 
if eqn1[3] == 0 or eqn1[3] == 2:
    eqn1.insert(2, 1)
    eqn1.insert(3, 0)
elif eqn1[3] == 1 or eqn1[3] == 3:
    eqn1.insert(2, -1)
    eqn1.insert(3, 0)

# Eqn2: adding slag variable 
if eqn2[3] == 0 or eqn2[3] == 2:
    eqn2.insert(2, 0)
    eqn2.insert(3, 1)
elif eqn2[3] == 1 or eqn2[3] == 3:
    eqn2.insert(2, 0)
    eqn2.insert(3, -1)


# TABLE

# mat = [[Bv, Bv_char, Xb, X1, X2, S1, S2, Xb/key], ...] --> mat[0] will be Zj values
#                                                       -- --> mat[n-1] will be Cj values
#                                                        --> mat[n] will ne Cj - Zj

mat_header = ['Bv', 'Bv_char', 'Xb', 'X1', 'X2', 'S1', 'S2']
mat = [[None, None, None, Zmax[0], Zmax[1], Zmax[2], Zmax[3]], [Zmax[2], 'S1', eqn1[4], eqn1[0], eqn1[1], eqn1[2], eqn1[3]], [Zmax[3], 'S2', eqn2[4], eqn2[0], eqn2[1], eqn2[2], eqn2[3]]]

Cj = Cj_calc(mat)
Cj_Zj = [None for i in range(len(mat[0]))]
mat.append(Cj)
mat.append(Cj_Zj)

print(mat)

negative_flag = True
while negative_flag == True:

    # Cj - Zj calculations
    Cj_Zj = list([None, None, None])
    for i in range(3, len(mat[0])):
        val = mat[3][i] - mat[0][i]
        Cj_Zj.append(val)
    mat[4] = Cj_Zj

    # checking updated table
    print(mat)


    for i in mat[4]:
        if i == None:
            continue
        elif i < 0:
            break
        else:
            negative_flag = False

    input()
    if negative_flag == True:
        # finding key column
        min_val = min(Cj_Zj[3:])
        col_min_val_index = Cj_Zj.index(min_val)

        print("key col :", col_min_val_index)

        # finding key row
        row_decider = list()
        for i in range(1, 3):
            val = mat[i][2] / mat[i][col_min_val_index]
            row_decider.append(val)

        print(row_decider) 

        min_positive = None
        for i in row_decider:
            if i >= 0:
                if min_positive == None:
                    min_positive = i
                elif i < min_positive:
                    min_positive = i

        row_min_positive_index = row_decider.index(min_positive)

        print("key row :", row_min_positive_index)

        key_value = mat[row_min_positive_index+1][col_min_val_index]
        print("key_value: ", key_value)

        new_Bv_char = mat_header[col_min_val_index]
        new_Bv = mat[0][col_min_val_index]

        print("new Bv character: {}\nnew Bv value: {}".format(new_Bv_char, new_Bv))

        mat[row_min_positive_index+1][0] = new_Bv
        mat[row_min_positive_index+1][1] = new_Bv_char

        new = list()

        for i in range(1, 3):
            new_values = list()
            new_values.append(mat[i][0])
            new_values.append(mat[i][1])
            if i == row_min_positive_index+1:
                for j in range(2, len(mat[i])):
                    val = mat[i][j]/ key_value
                    new_values.append(val)
            else:
                for j in range(2, len(mat[i])):
                    #breakpoint()
                    val = mat[i][j] - (mat[i][col_min_val_index] * mat[row_min_positive_index+1][j] / key_value)
                    new_values.append(val)
        
            new.append(new_values) 

        for i in range(len(new)):
            mat[i+1] = new[i]

        Cj = Cj_calc(mat)
        mat[3] = Cj

        print(mat)
        input()

