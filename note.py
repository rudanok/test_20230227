from model import Note
from controller import Controller

#пользовательский интерфейс
def main():
    ctrl = Controller()
    while(True):
        cmd = input('Введите команду: ')
        
        #добавление
        if(cmd == 'add'):
            note = Note('','')
            note.edit()
            ctrl.insert(note)
        
        #удаление
        elif(cmd == 'remove'):
            ctrl.remove()
        
        #редактирование
        elif(cmd == 'edit'):
            ctrl.edit()
        
        #выборка заметок по дате
        elif(cmd == 'find'):
            ctrl.find()
        
        #вывод заметки по номеру
        elif(cmd == 'choice'):
            ctrl.choice()
        
        #вывод всех записей
        elif(cmd == 'print'):
            ctrl.show()
        
        #сохранение заметок в указанный файл
        elif(cmd == 'save'):
            ctrl.save()
        
        #чтение данных из файла с фильтрацией по дате
        elif(cmd == 'load'):
            ctrl.load()
        
        #помощь по интерфейсу
        elif(cmd == 'help'):
            print('add - добавление заметки')
            print('remove - удаление заметки')
            print('edit - редактирование заметки')
            print('find - выборка заметок по дате')
            print('choice - вывод выбранной заметки')
            print('print - вывод всех заметок')
            print('save - сохранение заметок в файл')
            print('load - чтение заметок из файла')
            print('exit - выход из программы')
        
        #выход из программы
        elif(cmd == 'exit'):
            break
        
        else:
            print('Воспользуйтесь командой help, чтобы узнать какие команды доступны...')
            
#запуск программы
if __name__ == '__main__':
    main()