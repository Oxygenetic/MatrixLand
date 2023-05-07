'''
Created on 28 Nov 2022

@author: FHentsch-Cowles24
'''




class Matrix:
    '''
    Arg1: row entries - ie. [[1,2,3],[4,5,6]]
    '''
    def __init__(self, row_entries):
        self.row_entries = row_entries
        self.rows = len(row_entries)
        self.columns = len(row_entries[0])
    
    def describe_properties(self):
        print(f"{self.rows} x {self.columns} matrix:")
    
    def print(self):
        self.describe_properties()
        for i in self.row_entries:
            print(i)
        print()
    
    def plus(self, m2):
        if self.rows == m2.rows and self.columns == m2.columns:
            row_entries = []
            r = 0
            h = m2.row_entries
            
            for i in self.row_entries:
                row = []
                c = 0
                for j in i:
                    row.append(j + h[r][c])
                    c += 1
                row_entries.append(row)
                r += 1
            return Matrix(row_entries)
        else:
            pass
        
    def minus(self, m2):
        if self.rows == m2.rows and self.columns == m2.columns:
            row_entries = []
            r = 0
            h = m2.row_entries
            
            for i in self.row_entries:
                row = []
                c = 0
                for j in i:
                    row.append(j - h[r][c])
                    c += 1
                row_entries.append(row)
                r += 1
            return Matrix(row_entries)
        else:
            pass
    
    def times(self, m2):
        if self.columns == m2.rows:
            row_entries = []
            r = 0
            h = m2.row_entries
            for i in self.row_entries:
                c = 0
                row = []
                for j in h[0]:
                    p = 0
                    element_sum = 0
                    while p < m2.rows:
                        element_sum += (i[p]*h[p][c])
                        p += 1
                    row.append(element_sum)
                    c += 1
                row_entries.append(row)
                r += 1
            return Matrix(row_entries)
        else:
            pass
    
    def scalarTimesRow(self, scalar, row_number):
        row_entries = []
        r = 1
        for i in self.row_entries:
            if r == row_number:
                row = []
                for j in i:
                    row.append(j * scalar)
                row_entries.append(row)
            else:
                row_entries.append(i)              
            r += 1
        return Matrix(row_entries)
    
    def switchRows(self, first_row, second_row):
        row_entries = []
        r = 1
        for i in self.row_entries:
            if r == first_row:
                row_entries.append(self.row_entries[second_row-1])
            elif r == second_row:
                row_entries.append(self.row_entries[first_row-1])
            else:
                row_entries.append(i)
            r += 1
        return Matrix(row_entries)
    
    def linearCombRows(self, scalar, first_row, second_row):
        row_entries = []
        r = 0
        for i in self.row_entries:
            if (r+1) == second_row:
                row = []
                c = 0
                q = first_row-1
                for j in i:
                    #might need to fix 0 to 1 thingy
                    row.append(j + (scalar * self.row_entries[q][c]))
                    c += 1
                row_entries.append(row)
            else:
                row_entries.append(i)
            r += 1
        return Matrix(row_entries)
    
    def rowReduce(self):
        aug_entries = []
        for pos, row in enumerate(self.row_entries):
            aug_entries.append(row+self.identity().row_entries[pos])
        row_entries = Matrix(aug_entries)
        
        row_entries = row_entries.switchRows(1,3)
        
        row_entries.print()
        
        
        
        
        for pos, row in enumerate(row_entries.row_entries):
            
            
        
            
            multiple = row_entries.row_entries[pos][pos]
            row_entries = row_entries.scalarTimesRow(1/multiple, pos+1)
            row_entries.print()
            
            
            for o in range(0,pos):
                ding = -row_entries.row_entries[pos][o]
                print(ding)
                row_entries = row_entries.linearCombRows(ding, o+1, pos+1)
            
            
            #uhoh
        
        pass
        #return Matrix(row_entries)

    def invert(self):
        if self.rows == self.columns:
            pass
            
        
        pass

    def identity(self):
        row_entries = []
        c = 0
        for i in self.row_entries:
            row = []
            e = 0
            for j in i:
                if e == c:
                    row.append(1)
                else:
                    row.append(0)
                e += 1
            row_entries.append(row)
            c += 1
        
        return Matrix(row_entries)



'''print('mob1:')
mob1 = Matrix([[9,2,3],[4,5,6],[7,8,9]])
mob1.print()'''
print('mob2:')
mob2 = Matrix([[2,2,1],[3,1,0],[1,2,3]])
mob2.print()
'''
print('plus:')
plusmob = mob1.plus(mob2)
plusmob.print()

print('minus:')
minusmob = mob1.minus(mob2)
minusmob.print()

print('times:')
timesmob = mob1.times(mob2)
timesmob.print()

print('scalarTimesRow')
scalarmob = mob1.scalarTimesRow(2,2)
scalarmob.print()

print('switchRows')
switchmob = mob2.switchRows(1, 3)
switchmob.print()

print('linearCombRows')
linearmob = mob1.linearCombRows(2, 1, 2)
linearmob.print()'''

print('rowReduce')
reducedmob = mob2.rowReduce()
reducedmob.print()