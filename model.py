from datetime import date as dt #для получения текущей даты

#класс заметки
class Note:
    #уникальный номер заметки
    _id = 1
    
    def __init__(self,title,body,date=None):
        self.id = Note._id
        Note._id += 1
        self.title = title
        self.body = body
        if(date == None):
            self.date = dt.today()
        else:
            self.date = date
        
    #приведение к строке
    def __str__(self):
        return self.title + ";" + self.body + ";" + self.date.strftime("%d/%m/%Y")
    
    #для сравнения
    def __eq__(self,id):
        return self.id == id
    
    #вывод в удобном виде
    def show(self):
        print(str(self.id) + ": " + self.title)
        print(self.body)
        print(self.date)
        
    #редактирование заметки
    def edit(self):
        self.title = input('Введите заголовок заметки: ')
        self.body = input('Введите тело заметки: ')
        self.date = dt.today() #обновляем дату
        
    #сброс индексации
    def resetId():
        Note._id = 1