class time:
    def convert(self,sec):
        hours=sec//3600
        minutes=(sec % 3600)//60
        print(f'{hours}:{minutes}')
t=time()
t.convert(4800)