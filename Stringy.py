class CharSet:
    R = [0,0,0,0,0,0,0,0,
         1,1,1,1,1,1,1,1,
         0,0,0,1,0,0,0,1,
         0,0,0,1,0,0,0,1,
         0,0,0,1,0,0,0,1,
         0,0,1,0,1,0,0,1,
         1,1,0,0,0,1,1,0,
         0,0,0,0,0,0,0,0]
    
    I = [0,0,0,0,0,0,0,0,
         1,0,0,0,0,0,0,1,
         1,0,0,0,0,0,0,1,
         1,1,1,1,1,1,1,1,
         1,0,0,0,0,0,0,1,
         1,0,0,0,0,0,0,1,
         0,0,0,0,0,0,0,0]
        
    S = [0,0,0,0,0,0,0,0,
         0,1,0,0,0,1,1,0,
         1,0,0,0,1,0,0,1,
         1,0,0,0,1,0,0,1,
         1,0,0,0,1,0,0,1,
         0,1,1,1,0,0,1,0,
         0,0,0,0,0,0,0,0]
      
    H = [0,0,0,0,0,0,0,0,
         1,1,1,1,1,1,1,1,
         0,0,0,0,1,0,0,0,
         0,0,0,0,1,0,0,0,
         0,0,0,0,1,0,0,0,
         1,1,1,1,1,1,1,1,
         0,0,0,0,0,0,0,0]


def get_stringy(message):
    ' creates an array containing all the characters '
    stringy = []
    ' replaces each character from "message" into an string character '
    for i in range(0, len(message)-1):
        if message[i] == "H":
            stringy.extend(CharSet.H)
        if message[i] == "I":
            stringy.extend(CharSet.I)
        if message[i] == "R":
            stringy.extend(CharSet.R)
        if message[i] == "S":
            stringy.extend(CharSet.S)
            
    return stringy
