from model import Note #получаем класс заметки
from datetime import date as dt #для дат

#контроллер для обработки списка заметок
class Controller:
    def __init__(self):
        self.list = []
        
    #добавление записки
    def insert(self,note):
        self.list.append(note)
        print('Заметка успешно добавлена')
    
    #удаление
    def remove(self):
        if(len(self.list) == 0):
            print('Список заметок пуст')
        else:
            try:
                id = int(input('Введите номер заметки: '))
                for i in range(len(self.list)):
                    if(self.list[i] == id):
                        del self.list[i]
                        print('Заметка успешно удалена')
                        return
                print('Не удалось удалить заметку')
            except Exception as e:
                print(str(e))
    
    #редактирование
    def edit(self):
        if(len(self.list) == 0):
            print('Список заметок пуст')
        else:
            try:
                id = int(input('Введите номер заметки: '))
                for i in range(len(self.list)):
                    if(self.list[i] == id):
                        self.list[i].edit()
                        print('Заметка успешно изменена')
                        return
                print('Не удалось отредактировать заметку')
            except Exception as e:
                print(str(e))
    
    #выборка данных по дате
    def find(self):
        if(len(self.list) == 0):
            print('Список заметок пуст')
        else:
            try:
                d, m, y = [int(x) for x in input("Укажите дату в формате (DD/MM/YYYY): ").split('/')]
                date = dt(y,m,d)
                result = []
                for i in range(len(self.list)):
                    if(self.list[i].date == date):
                        result.append(self.list[i])
                if(len(result) > 0):
                    print('Вот что удалось найти:')
                    for i in range(len(result)):
                        print(str(result[i].id) + ": " + result[i].title)
                else:
                    print('Не удалось найти заметок по указанной дате')
            except Exception as e:
                print(str(e))
        
    #вывод заметки по номеру
    def choice(self):
        if(len(self.list) == 0):
            print('Список заметок пуст')
        else:
            try:
                id = int(input('Введите номер заметки: '))
                for i in range(len(self.list)):
                    if(self.list[i] == id):
                        print()
                        self.list[i].show()
                        return
                print('Не удалось найти указанной заметки')
            except Exception as e:
                print(str(e))
    
    #вывод на консоль
    def show(self):
        if(len(self.list) == 0):
            print('Список заметок пуст')
        else:
            for i in range(len(self.list)):
                print()
                self.list[i].show()
            
    #сохранение списка в файл csv (разделение по точке с запятой)
    def save(self):
        try:
            if(len(self.list) == 0):
                print('Список заметок пуст')
            else:
                filename = input('Введите название файла: ')
                with open(filename, 'w') as f:
                    for i in range(len(self.list)):
                        f.write(str(self.list[i]) + "\n")
                    print('Заметки успешно записаны в файл ' + filename)
        except Exception as e:
            print(str(e))
    
    #загрузка из файла
    def load(self):
        try:
            filename = input('Введите название файла: ')
            
            #читаем с фильтрацией по дате
            d, m, y = [int(x) for x in input("Укажите дату с которой нужно читать в формате (DD/MM/YYYY): ").split('/')]
            date = dt(y,m,d)
            with open(filename, 'r') as f:
                Note.resetId()
                self.list = []
                for i in f.readlines():
                    words = i.split(';')
                    if(len(words) == 3):
                        d,m,y = [int(x) for x in words[2].split('/')]
                        date1 = dt(y,m,d)
                        if(date1 >= date):
                            note = Note(words[0],words[1],date1)
                            self.list.append(note)
                if(len(self.list) > 0):
                    print('Заметки успешно получены из файла ' + filename)
                else:
                    print('Не удалось получить заметки из файла')
        except Exception as e:
            print(str(e))