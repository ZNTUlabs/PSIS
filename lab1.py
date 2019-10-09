import math

class Sample:
    middle=0
    size=int(0)
    rangge=int(0)
    sqrtt=int(0)
    def __init__(self,siz):#Конструктор
        self.size=siz
        self.items=list()
        i=0
        while i<self.size:
            add=int(input("Введите элемент выборки "))
            self.items.append(add)
            i=i+1
            
        
            

    def output(self):#Вывод
       
        print(self.items)
        

    def middle(self):#Среднее
        summ=int(0)
        i=int(0)
        while i<self.size:
            summ=summ+self.items[i]
            i=i+1
        self.middle=summ/self.size
        return self.middle

    def summ(self):#Сумма
        summ=int(0)
        i=int(0)
        while i<self.size:
            summ=summ+self.items[i]
            i=i+1
        return summ

    def rangge(self):#Размах
        self.rangge=max(self.items)-min(self.items)
        return self.rangge

    def sqrtt(self):#Среднеквадратическое отклонение
        i=int(0)
        summ=int(0)
        while i<self.size:
            summ=summ+math.pow(self.items[i]-self.middle,2)
            i=i+1
        self.sqrtt=math.sqrt(summ/self.size)
        return self.sqrtt

    def disperce(self):#Дисперсия
        mathaw=int(0)
        mathaw2=int(0)
        i=int(0)
        while i<self.size:
            mathaw=mathaw+(self.items[i]*(1/self.size))
            i=i+1
        i=int(0)
        while i<self.size:
            mathaw2=mathaw2+(pow(self.items[i],2)*(1/self.size))
            i=i+1

        return(mathaw2-pow(mathaw,2))


def Kohren(samples):#Критерий Кохрена

    dsprc=list()

    i=0
    while i<len(samples):
        dsprc.append(samples[i].disperce())
        i=i+1
    
    maxim=max(dsprc)
    
    sumd=sum(dsprc)

    if sumd!=0:
        return(maxim/sumd)
    else:
        return ("Невозможно вычислить критерий Кохрена")

def values(smp):#Значения
    smp.output()
    print("Среднее арифметическое ",smp.middle())
    print("Размах ",smp.rangge())
    print("Среднеквадратическое отклонение ",smp.sqrtt())
    print("Дисперсия ",smp.disperce())
    return 0


amount=int(input("Введите количество выборок "))
samples=list()
size=int(input("Введите размер выборок "))
i=0
while i<amount:#Создание выборок
    smpl=Sample(size)
    values(smpl)
    samples.append(smpl)
    i=i+1

print("Критерий Кохрена ",Kohren(samples))

    
