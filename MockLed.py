def show_led(matrix):

    ' append missing items to prevent list index out of range '
    while len(matrix) < 64:
        matrix.extend([0])

    col1 = matrix[0:8]
    col2 = matrix[8:16]
    col3 = matrix[16:24]
    col4 = matrix[24:32]
    col5 = matrix[32:40]
    col6 = matrix[40:48]
    col7 = matrix[48:56]
    col8 = matrix[56:64]

    col2.reverse()
    col4.reverse()
    col6.reverse()
    col8.reverse()

        
    ' mimic zig zag lights from bottom left '
    print("---seperator----")
    print(col1[7],col2[0],col3[7],col4[0],col5[7],col6[0],col7[7],col8[0])
    print(col1[6],col2[1],col3[6],col4[1],col5[6],col6[1],col7[6],col8[1])
    print(col1[5],col2[2],col3[5],col4[2],col5[5],col6[2],col7[5],col8[2])
    print(col1[4],col2[3],col3[4],col4[3],col5[4],col6[3],col7[4],col8[3])
    print(col1[3],col2[4],col3[3],col4[4],col5[3],col6[4],col7[3],col8[4])
    print(col1[2],col2[5],col3[2],col4[5],col5[2],col6[5],col7[2],col8[5])
    print(col1[1],col2[6],col3[1],col4[6],col5[1],col6[6],col7[1],col8[6])
    print(col1[0],col2[7],col3[0],col4[7],col5[0],col6[7],col7[0],col8[7])
