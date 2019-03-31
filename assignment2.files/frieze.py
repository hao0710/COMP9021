from copy import deepcopy
import os 
import sys


class FriezeError(Exception):
    def __init__(self,message):
        self.message=message
    

class Frieze:
    def __init__(self,filename):
        self.filename=filename
        with open(self.filename,'r',encoding='utf-8' ) as text_file:
            try:
                self.original_matrix=[]
                lines=text_file.read()
                x=lines.split("\n")
                for i in x:
                    if i=='':
                        continue
                    else:
                        j=i.split(" ")
                        self.original_matrix.append(list(filter(lambda a: a != "", j)))
                for i in range(len(self.original_matrix)):
                    for j in range(len(self.original_matrix[i])):
                        self.original_matrix[i][j] = int(self.original_matrix[i][j])
            except ValueError:
                raise FriezeError('Incorrect input.')
                        
            count = self.original_matrix.count([])
            for i in range(count):
                self.original_matrix.remove([])
        self.lenth=len(self.original_matrix[0])-1
        self.height=len(self.original_matrix)
        self.repetition,self.period=self.checkFriezePeriod()
        

        #top and bottom line
        for i in self.original_matrix[0]:
            if 1<=i<=3 or 5<=i<11 or i>12 or self.original_matrix[0].count(0)>1:
                raise FriezeError('Input does not represent a frieze.')
        for i in self.original_matrix[-1]:
            if i>8 or self.original_matrix[-1].count(0)>1:
                raise FriezeError('Input does not represent a frieze.')
        #check last column
        if self.original_matrix[0][-1]!=0:
            raise FriezeError('Input does not represent a frieze.')
        for i in self.original_matrix:
            if i[-1]>1 or i[-1]<0:
                raise FriezeError('Input does not represent a frieze.')

        for i in range(len(self.original_matrix)-1):
            #height range
            if len(self.original_matrix)<3 or len(self.original_matrix)>17:
                raise FriezeError('Incorrect input.')
            #lenth range
            elif len(self.original_matrix[i])<5 or len(self.original_matrix[i])>51:
                raise FriezeError('Incorrect input.')
            #equal lenth
            elif len(self.original_matrix[i])!=len(self.original_matrix[i+1]):
                raise FriezeError('Incorrect input.')
            for j in self.original_matrix[i]:
                if j<0 or j>15:
                    raise FriezeError('Incorrect input.')
        for i in range(len(self.original_matrix)):
            for j in range (len(self.original_matrix[i])):
                if self.original_matrix[i][j] not in range(0,16):
                    raise FriezeError('Incorrect Input.')


        #check cross
        for i in range(1,len(self.original_matrix)):
            for j in range(len(self.original_matrix[i])):
                if self.original_matrix[i][j]>8:
                    if self.original_matrix[i+1][j] in [2,3,6,7,10,11,14,15]:
                        raise FriezeError('Input does not represent a frieze.')
        if self.period<2:
            raise FriezeError('Input does not represent a frieze.')
        if self.repetition<2:
            raise FriezeError('Input does not represent a frieze.')
        for i in range(len(self.original_matrix)):
            if self.original_matrix[i][-1]==1 and self.original_matrix[i][0]%2==0:
                raise FriezeError('Input does not represent a frieze.')
                            	
    def getBinaryDigit(self,x):
        binaryList = list()
        while True:
            binaryList.append(x % 2)
            if len(binaryList) == 4:
                break
            x //= 2
        return binaryList
    def N(self,x, y):
        global original_matrix
        bi = self.getBinaryDigit(self.original_matrix[x][y])
        if bi[0] == 1:
            return True
        else:
            return False
    def NE(self,x, y):
        global original_matrix
        bi = self.getBinaryDigit(self.original_matrix[x][y])
        if bi[1] == 1:
            return True
        else:
            return False
    def E(self,x, y):
        global original_matrix
        bi = self.getBinaryDigit(self.original_matrix[x][y])
        if bi[2] == 1:
            return True
        else:
            return False
        
    def SE(self,x, y):
        global original_matrix
        bi = self.getBinaryDigit(self.original_matrix[x][y])
        if bi[3] == 1:
            return True
        else:
            return False



    def checkFriezePeriod(self):
        global original_matrix
        n = deepcopy(self.original_matrix)
        for i in range(len(n)):
            n[i] = n[i][:-1]
        for temp_period in range(1, len(n[0]) // 2 + 1):
            if len(n[0]) % temp_period != 0:
                continue
            else:
                flag = [False] * len(n)
                temp_repetition = len(n[0]) // temp_period
                for row in range(len(n)):
                    if n[row] == n[row][:temp_period]*temp_repetition:
                        flag[row] = True
                if False not in flag:
                    return temp_repetition, temp_period
                else:
                    continue
        return 0, 0
    
    def checkHorizontal(self,p):
        global original_matrix
        global height
        
        for i in range(self.height):
            for j in range(p):
                
                if self.N(i, j):
                    if not self.N(self.height - i, j):
                       
                        return False
                if self.NE(i, j):
                    if not self.SE(self.height - i - 1, j):
                        return False
                if self.E(i, j):
                    if not self.E(self.height - i - 1, j):
                        return False
                if self.SE(i, j):
                    if not self.NE(self.height - i - 1, j):
                        return False
        return True

    def checkVertical(self,start, p):
        global original_matrix
        global height
        
        for i in range(self.height):
            for j in range(start, start+p):
                if self.N(i, j):
                    if not self.N(i, start+p+1-j):
                        return False
                if self.NE(i, j):
                    if not self.SE(i-1, start+p-j):
                        return False
                if self.E(i, j):
                    if not self.E(i, start+p-j):
                        return False
                if self.SE(i, j):
                    if not self.NE(i+1, start+p-j):
                        return False
        return True
    
    def checkGlidedHorizontal(self,p):
        global original_matrix
        global height
        for i in range(self.height):
            for j in range(p):
                if self.N(i, j):
                    if j < p//2:
                        if not self.N(self.height - i, j + p//2):
                            return False
                    else:
                        if not self.N(self.height - i, j - p//2):
                            return False
                if self.NE(i, j):
                    if j < p // 2:
                        if not self.SE(self.height - i - 1, j + p//2):
                            return False
                    else:
                        if not self.SE(self.height - i - 1, j - p//2):
                            return False
                if self.E(i, j):
                    if j < p // 2:
                        if not self.E(self.height - i - 1, j + p//2):
                            return False
                    else:
                        if not self.E(self.height - i - 1, j - p//2):
                            return False
                if self.SE(i, j):
                    if j < p // 2:
                        if not self.NE(self.height - i - 1, j + p//2):
                            return False
                    else:
                        if not self.NE(self.height - i - 1, j - p//2):
                            return False
        return True


    def checkRotation(self,start, p):
        global original_matrix
        global height
        for i in range(self.height):
            for j in range(start, start+p):
                if self.N(i, j):
                    if not self.N(self.height-i, start+p-(j-start)):
                        return False
                if self.NE(i, j):
                    if not self.NE(self.height-i, start+p-1-(j-start)):
                        return False
                if self.E(i, j):
                    if not self.E(self.height-1-i, start+p-1-(j-start)):
                        return False
                if self.SE(i, j):
                    if not self.SE(self.height-2-i, start+p-1-(j-start)):
                        return False
        return True
    def analyse(self):
        hr=0
        vr=0
        ro=0
        ghr=0
        period=self.period
        for i in range(self.period):
            if self.checkRotation(i,period)==True:
                ro=1
                break
            else:
                ro=0
        for i in range(self.period):
            if self.checkVertical(i,period)==True:
                vr=1
                break
            else:
                vr=0
        for i in range(self.period):
            if self.checkHorizontal(period)==True:
                hr=1
                break
            else:
                hr=0
        for i in range(period):
            if self.checkGlidedHorizontal(period)==True:
                ghr=1
                break
            else:
                ghr=0
        if hr==0 and  vr==0 and  ro==0 and ghr==0:
            print("Pattern is a frieze of period %s that is invariant under translation only."%period)
        elif vr==1 and  hr==0 and ro==0 and  ghr==0:
            print("Pattern is a frieze of period {} that is invariant under translation\n        and vertical reflection only.".format(period))
        elif hr==1 and vr==0 and ro==0 and ghr==0:
            print("Pattern is a frieze of period %s that is invariant under translation\n        and horizontal reflection only."%period)
        elif ghr==1 and hr==0 and vr==0  and ro==0:
            print("Pattern is a frieze of period %s that is invariant under translation\n        and glided horizontal reflection only."%period)
        elif ro==1 and hr==0 and vr==0 and ghr==0:
            print("Pattern is a frieze of period %s that is invariant under translation\n        and rotation only."%period)
        elif ghr==1 and vr==1 and ro==1 and hr==0:
            print("Pattern is a frieze of period %s that is invariant under translation,\n        glided horizontal and vertical reflections, and rotation only."%period)
        elif hr==1 and vr==1 and ro==1 and ghr==0:
            print("Pattern is a frieze of period %s that is invariant under translation,\n        horizontal and vertical reflections, and rotation only."%period)
        else:
            print("Pattern is a frieze of period %s that is invariant under translation,\n        glided horizontal and vertical reflections, and rotation only."%period)
            
    def display(self):
              
        pass
       
frieze=Frieze('frieze_1.txt')
#repetition, period = frieze.checkFriezePeriod()

#period

#frieze=Frieze('incorrect_input_zimu.txt')

