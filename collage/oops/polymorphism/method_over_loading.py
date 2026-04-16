class methodover:
    def add(self,datatype,*arg):
        if(datatype=='int'):
            answer=0
            for x in arg:
                answer=answer+x
        if(datatype=='str'):
            answer=''
            for x in arg:
                answer=answer+' '+x
        print(answer)
a=methodover()
a.add('int',5,15,20)
a.add('str','computer','science','is','core')