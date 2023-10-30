import time
import csv
import json

def print_story(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)  

story = "Добро пожаловать в игру висилица....."
story_wod = "Смотри не повесься"
print_story(story)
print(" ")
print(" ")
print_story(story_wod)
print(" ")
print(" ")




import random

def print_hangman(lives):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    print(stages[lives])

import random

def select_word(category):
    words = {
        "фрукты": {
            "яблоко":   "Красный фрукт съедобный",
            "банан": "Желтый фрукт, который растет на дереве",
            "вишня": "Маленький красный фрукт с косточкой",
            "дуриан": "Фрукт с сильным запахом",
            "ежевика": "Фрукт сочного черного цвета с маленькими колючками"
        },
        "животные": {
            "собака": "Домашнее животное, лает",
            "кошка": "Домашнее животное, мурлычет",
            "тигр": "Большой хищник с полосатой шерстью",
            "слон": "Крупное млекопитающее с длинным хоботом",
            "крокодил": "Рептилия с длинными челюстями и острыми зубами"
        },
        "машины": {
            "спорткар": "Очень быстрый автомобиль",
            "фура": "большой автомобиль с прицепом",
            "автобус": "Государственный автомобиль, перевозящий людей",
            "легковая": "на этом автомобиле ездиют большинство людей",
            "мерс": "один из лучший автомобилей на земле"
        },
        "техника": {
            "телефон": "мобильник, а если по другому?",
            "телевизор": "огромный цифровой ящик",
            "планшет": "есть вот телефон, только это побольше чем телефон",
            "ноутбук": "есть ПК а есть....",
        },
        "спорт": {
            "футбол": "вид спорта где пинают мяч ногами",
            "баскетбол": "вид спорта где кидают мяч в кальцо",
            "волейбол": "вид спорта где мяч кидают через сетку",
            "хоккей": "вид спорта где есть шайа и клюшка",
        }
    }
    
    if category in words:
        word = random.choice(list(words[category].keys()))
        question = words[category][word]
        return word, question
    else:
        return None, None

def get_guess():
    guess = input("Введите букву: ")
    return guess.lower()

def update_word(word, guessed_letters):
    updated_word = ""
    for letter in word:
        if letter in guessed_letters:
            updated_word += letter
        else:
            updated_word += "_"
    return updated_word


#счетчик отгаадаанных слов
def count_guessed_words(words, guessed_letters):
    count = 0
    for word in words:
        if update_word(word, guessed_letters):
            count += 1
    return count
 

# выбор категории игры 

def play_game():
    while True:
        category = input("Выберите категорию (фрукты/животные/машины/техника/спорт): ")
        word, question = select_word(category)
        if word is None:
            print("Выбранная категория не существует.")
            restart = input("Хотите ли вы выбрать категорию заново? (да/нет): ")
            if restart == "да":
                continue
            else:
                break
    

        guessed_letters = set()
        lives = 6
        score = 0

        while True:
            print_hangman(lives)
            print(f"Слово: {update_word(word, guessed_letters)}")
            print(" ")
            print(f"Угаданные буквы: {', '.join(sorted(guessed_letters))}")
            print(f"Вопрос: {question}")
            print(" ")
            print(f"Очки: {score}")

            if "_" not in update_word(word, guessed_letters):
                score += 50
                print("Поздравляю! Вы угадали слово.")
                print(f"Ваш счет: {score}")
                break

            if lives == 0:
                print(f"Игра окончена! Слово было {word}.")
                print(f"Ваш счет: {score}")
                break
# количество очков 
            guess = get_guess()

            if guess in guessed_letters:
                print("Вы уже угадали эту букву. Попробуйте еще раз.")
            elif guess in word:
                guessed_letters.add(guess)
                score += 10
                print("Правильная буква!")
            else:
                guessed_letters.add(guess)
                lives -= 1
                print()
                print("Неправильная буква!")
                if lives > 0:
                    play_again = input("Хотите сыграть еще раз? (да/нет): ")
                    if play_again.lower() != "да":
                        break
                else: 
                    print("ты проиграл")
                    break
                 

if __name__ == "__main__":
            play_game()



           
filename = "usersohrn.txt"
myfile = open (filename, mode='w')
#сохранение в json файл 
game_data = {
    'USER': "ИГРОК",
    'WORDS': count_guessed_words,
    'SCORE': #  я не понимаю как сделать чтобы он выводил очки 
}

with open('game_data.json', 'w') as f:
    json.dump(game_data, f) 
myfile.close()

#сохраняем в csv файл 
with open ("game_data.csv","w",newline="") as f:
    write = csv.writer(f)
    writer.writerow(["ИГРОК","ОТГАДАННОЕ СЛОВО","ОЧКИ"])
    for player in game_data["ИГРОК"]:
        writer.writerow([player,game_data["ИГРОК"][player] ["ОТГАДАННОЕ СЛОВО"], game_data["ИГРОК"][player]["ОЧКИ"]])
        
delete_save = input("Хотите удолить? (да/нет): ")
if delete_save == "да":
    # удаляем данные из json файла
    with open ("game_data.json", "w") as f:
        json.dump({}, f)
    # удаляем данные из csv файла
    with open("game_data.csv", "w", newline="") as f:
        pass
    
    
        
        
