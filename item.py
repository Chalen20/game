from random import *
class ItemController:
    possibleItem=[Food(getImage("img/food/Food_varenics.png",False))]
    def getLoot(self):
        item=possibleItem[randint(0,len(possibleItem)-1)]
        return item
    def getImage(self,name,big):
        img = Image.open(name)
        if big:
            img = img.resize((200, 200), Image.ANTIALIAS)
            
        else:
            img = img.resize((100, 100), Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)   
       
        

class Item:
    def __init__(self,skin,value,bigSkin,name)
        self.skin=skin
        self.value=value
        self.bigSkin=name
        self.name=name
    

class Food(Item):
    def __init__(self,skin,value,bigSkin,name,satiety,*args):
        Item(self,skin,value,bigSkin,name)
        self.rottness=100
        self.satiety=satiety
        if(len(args)>0):
            self.canRott=True
            self.rotteRate=args[0]
            #self.rottness=100
        else:
            self.canRott=False
            
    def rotten(self):
        if(self.canRott):
            self.rottness-=self.rotteRate
        if(self.rottness<=0):
            return True
        return False
    def use(self,pers):
        pers.hunger-=self.satiety
        if(pers.hunger<0):
            pers.hunger=0
        return True
#class Armor(Item):
class Weapon(Item):
class Poitions(Item):
    
