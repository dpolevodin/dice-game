import random
import time


user_score = 0
admin_score = 0

print()
print ("Привет, Друг, напиши свое имя:")
Name = input('Задайте ваше имя: ')
To_repeat = "Сыграем еще разок? Введи 'да', если согласен или 'нет', если не готов больше проигрывать"
print ("Рад знакомству, ", Name, ", давай сыграем в игру. Бросаем кубик по очереди. Выигрывает тот, у кого выпадет большее число от 1 до 6")

def roll():
    """функция запускает процесс броска с подведением результата и записью результата в словарь"""
    while True:
        Roll_user = random.randint(1,6)
        Roll_admin = random.randint(1,6)
        global user_score
        global admin_score
        print ("Твой бросок - первый. Нажми 'Enter', как будешь готов бросить кубик")
        Roll = input ()
        time.sleep(2)
        
        if Roll_user == 6:
            print ('Ого, да тебе сегодня везет. ','У тебя на кубике выпало - ', Roll_user,'. Ну может хотя-бы ничьей закончим?')
        else:
            print ("У тебя на кубике выпало - ", Roll_user, ". Теперь мой бросок...")        
        time.sleep(3)
        print ("У меня выпало - ", Roll_admin)
        time.sleep(2)
        if Roll_user > Roll_admin:
            print ("Поздравляю , ", Name, "!, Победа за тобой! :)", To_repeat)
            user_score +=1
        elif Roll_user < Roll_admin:
                print ("Ахах, сегодня удача мне благоволит, я победил!!!", To_repeat)
                admin_score +=1
        else: print ("Кажется у нас - ничья...", To_repeat)
        print ('текущий счет:', user_score, ' : ', admin_score)
        Repeat_Game2 = input ('Введите ответ: ')
        if Repeat_Game2 == 'нет':
            print ("Было приятно с тобой играть! Надеюсь, еще увидимся ;)")
            break
        else: continue
roll()
