import os


class SatFile() :

    def __init__(self, filename): 
        try: 
            filename=open(filename)
        except Exception as ex: 
            print(ex)
            print('File {} not found.'.format(filename))
     
        else: 

            try: 
                line= filename.readline().split(" ")
                if line[0]== 'p'and line[1]=='cnf' and int(line[2]) > 1 and int(line[3]) > 1: 
                    pass 
                else: 
                    raise Exception
            except Exception as ex2: 
                print ('{} is not a DIMACS format file.'.format(filename.name))
                #todo: Garantizar que no se cree la instancia, o no se considere. 
            else: 
                self.content=''
                for x in range(int(line[3])-1): 
                    self.content+= filename.read()
                

    def __clean(self): 
        self.clauses = []
        for clause in self.content.split('\n')[:-1] : #El -1 elimina el ultimo elemento.
            clause = clause[:-2] ##Con el -2 se elimina tambien el espacio en blanco.
            self.clauses.append(clause)
        return self.clauses


    def to_sat(self): 
        self.__clean()



if __name__== "__main__":
    print ('este es el main')    
    
    files = []
    file = SatFile('sat.txt')