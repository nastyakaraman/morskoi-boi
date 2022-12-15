# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:22:41 2022

@author: ADMIN
"""

import random
import copy
import sys 

class Point:
    def __init__(self,x=1,y=1):
        self.x=x
        self.y=y
        self.num=(y-1)*6+x
        
    def set_xy(self):
        #стандартный сеттер
        X=int(input('Введите номер ячейки по оси Х: '))
        Y=int(input('Введите номер ячейки по оси Y: '))
        self.x=X
        self.y=Y
        self.num=(Y-1)*6+X
      
    def random_set_xy (self,lst):
        #создает рандомную точку на поле и проверяет, есть ли она в списке 
        while True:
            X=random.randrange(1, 7, 1)
            Y=random.randrange(1, 7, 1)
            NUM=(Y-1)*6+X
            if NUM not in lst and (NUM-1) not in lst and (NUM+1) not in lst:
                if(NUM-6) not in lst and (NUM+6) not in lst:
                    break
        self.x=X
        self.y=Y
        self.num=NUM
        
       
    @staticmethod
    def num_from_pt(obj_list):
        num_list=[]
        for obj in obj_list:
            num_list.append(obj.num)
        return num_list 
        

list_pts=[1,5,7]
pt1=Point(1,1)
pt2=Point(1,2)
pt3=Point() #инициализирую 
pt3.random_set_xy(list_pts) # Изменяю параметры на рандомные
nnn=Point.num_from_pt([pt1,pt2])

class Ship:
    #на входе список заполненных кораблем ячеек (номер от 1 до 36)
    def __init__(self, name=1, pts_obj=[]):
        self.name=name
        self.pts_obj=pts_obj
        self.dlina=len(self.pts_obj)
        self.pts=Point.num_from_pt(self.pts_obj)
        if self.dlina>1:
            if abs(self.pts[0]-self.pts[1])==1:
                self.position='horizontal'
            else:
                self.position='vertical'
    
    #функция спрашивает координаты с консоли и создает корабль
    @staticmethod
    def points_for_ship(name_,num):
         pt_list=[]
         s=1
         for i in range (num):
             print('Задаем координаты ' + str(s) + '-й клетки')
             p=Point()
             p.set_xy()
             pt_list.append(copy.copy(p))
             s+=1
         return Ship(name=name_, pts_obj=pt_list)
    
    #функция задает большие и средние корабли для питона
    @staticmethod
    def points_for_pyship(name_,num, lst):
         pt_list=[]
         if num==3:
            X=random.randrange(1, 5, 1)
            Y=random.randrange(1, 5, 1)
         elif num==2:
             while True:
                 X=random.randrange(1, 6, 1)
                 Y=random.randrange(1, 6, 1)
                 NUM=(Y-1)*6+X
                 if NUM not in lst and (NUM-1) not in lst and (NUM+1) not in lst:
                     if(NUM-6) not in lst and (NUM+6) not in lst:
                         break
         dop=0
         randomizer=random.randrange(1, 100000, 1)
         for i in range (num):
             if randomizer%2==0:
                 p=Point(X+dop,Y)
             else:
                 p=Point(X,Y+dop)
             pt_list.append(copy.copy(p))
             dop+=1
         return Ship(name=name_, pts_obj=pt_list)
      
    
    
class Random1Ship(Ship):
    #создает корабль размером в одной ячейку в рандомном свободном месте
    def __init__(self, name=4, dlina=1, lst=[]):
        self.name=name
        self.dlina=dlina
        
        rndm_pt=Point()
        rndm_pt.random_set_xy(lst)
        
        self.pts_obj=[rndm_pt]
        self.pts=Point.num_from_pt(self.pts_obj)
        
ship2=Ship(2,[pt1,pt2])
ship1=Random1Ship(name=4,dlina=1,lst=list_pts)
               
class Doska:
    def __init__(self,rows=6,lines=6, ships=[]): #на вход список объектов кораблей
        self.rows=rows
        self.lines=lines
        self.ships=ships
        
        self.num_all=self.rows*self.lines
        self.alll=list(range(1,self.num_all+1))
                
        self.busy=[]
        if ships:
            for boat in ships:
                self.busy=self.busy+boat.pts
                 
        val='0'
        self.display=[val]*self.num_all
        if self.busy:
            for num in self.busy:
                self.display[num-1]='█'
            
        self.killed=0 #счетчик сбитых кораблей
    
    '''@staticmethod    
    def print_empty():
        str1=' '
        cherta=str(20*'_')
        itog='\n' + cherta + '\n' + '\n'
        for i in range (6):
            str1=str1 + '|' + '0' + '|'
        for i in range (6):
            itog=itog + str1 + '\n'
        itog=itog+cherta + '\n'
        return print(itog)'''
    
    def set_ships(self,shiplist):
        if shiplist:
            for boat in shiplist:
                self.ships.append(boat)
                self.busy=self.busy+boat.pts
        for num in self.busy:
            self.display[num-1]='█'
        
    
    def __str__(self):
        a=0
        s=1
        str1=str(s) + ' '
        str_start='  '
        cherta=str(20*'_')
        itog='\n' + cherta + '\n' + '\n'
        
        for k in range(1,7):
            str_start=str_start+'|' + str(k) + '|'
            
        str_start+='\n'    
        itog+=str_start
        for j in range(6):
            for i in range(6):
                str1+='|' + self.display[i+a] + '|'
            itog=itog+str1+'\n'
            s+=1
            str1=str(s) + ' '
            a+=6
        itog=itog+cherta + '\n'
        return itog   
      
    
    #функция преобразовывает игровую доску поcле выстрела
    def after_shot (self, Pt):
        if Pt.num in self.busy:
            self.display[Pt.num]='X'
            self.killed+=1
        else:
            self.display[Pt.num]='T'
            
def Python_board():
    Human_d=Doska()  
        
if __name__ == "__main__":
    print ('\n'+'Приветствую игрок! Сегодня играем в морской бой'+'\n'+'Твой соперник по игре - Питон')
    Human_d=Doska()
    print ('Ознакомься с игровым полем:')
    print(Human_d)
    print ('Твой флот состоит из 7 кораблей:'+'\n'+ '1 корабль на 3 клетки' + '\n' + '2 корабля на 2 клетки' + '\n' + '4 корабля на 1 клетку')
    print ('Давай начнем с большого корабля'+'\n') 
    
    Human_d.set_ships([Ship.points_for_ship(1,3)]) #запускаем функцию, которая спрашивает с консоли координаты, создает корабль и добавляет его на игровое поле
    name_count=2 #счетчик имен, чтобы нумеровать последовательно
    print(Human_d)
    print ('Теперь зададим 2 средних корабля размером 2 клетки'+'\n')
    print('Первый корабль среднего размера')
    for i in range(2):
        Human_d.set_ships([Ship.points_for_ship(name_count,2)])
        print(Human_d)
        if i==0:
            print('И еще один корабль по 2 клетки')
        name_count+=1
    usl1=input('Устал? Нужно еще 4 корабля по 1 клетке. Давай зададим их рандомно в свободные поля? Напиши да или нет: ')
    for i in range(4):
        r_ship=Random1Ship(name=name_count,dlina=1, lst=Human_d.busy)
        Human_d.set_ships([copy.copy(r_ship)])
        name_count+=1
    print(Human_d)
    print('Прости, выбора не было(')
    