import random


words = [
    {"arabic": "في", "english": "in"},
    {"arabic": "من", "english": "from"},
    {"arabic": "إلى", "english": "to"},
    {"arabic": "على", "english": "on"},
    {"arabic": "و", "english": "and"},
    {"arabic": "أو", "english": "or"},
    {"arabic": "لكن", "english": "but"},
    {"arabic": "مع", "english": "with"},
    {"arabic": "عن", "english": "about"},
    {"arabic": "هذا", "english": "this"},
    {"arabic": "هذه", "english": "this (feminine)"},
    {"arabic": "ذلك", "english": "that"},
    {"arabic": "تلك", "english": "that (feminine)"},
    {"arabic": "هو", "english": "he"},
    {"arabic": "هي", "english": "she"},
    {"arabic": "أنا", "english": "I"},
    {"arabic": "أنت", "english": "you"},
    {"arabic": "نحن", "english": "we"},
    {"arabic": "هم", "english": "they"},
    {"arabic": "كان", "english": "was"},
    {"arabic": "يكون", "english": "is / be"},
    {"arabic": "ليس", "english": "is not"},
    {"arabic": "لدي", "english": "I have"},
    {"arabic": "عند", "english": "at / with"},
    {"arabic": "كل", "english": "every / all"},
    {"arabic": "بعض", "english": "some"},
    {"arabic": "أي", "english": "any"},
    {"arabic": "لا", "english": "no / not"},
    {"arabic": "نعم", "english": "yes"},
    {"arabic": "ما", "english": "what"},
    {"arabic": "من", "english": "who"},
    {"arabic": "متى", "english": "when"},
    {"arabic": "أين", "english": "where"},
    {"arabic": "لماذا", "english": "why"},
    {"arabic": "كيف", "english": "how"},
    {"arabic": "إذا", "english": "if"},
    {"arabic": "ثم", "english": "then"},
    {"arabic": "بعد", "english": "after"},
    {"arabic": "قبل", "english": "before"},
    {"arabic": "هنا", "english": "here"},
    {"arabic": "هناك", "english": "there"},
    {"arabic": "اليوم", "english": "today"},
    {"arabic": "غدًا", "english": "tomorrow"},
    {"arabic": "أمس", "english": "yesterday"},
    {"arabic": "الآن", "english": "now"},
    {"arabic": "دائمًا", "english": "always"},
    {"arabic": "أبدًا", "english": "never"},
    {"arabic": "كثير", "english": "many / much"},
    {"arabic": "قليل", "english": "few / little"},
    {"arabic": "واحد", "english": "one"},
    {"arabic": "اثنان", "english": "two"},
    {"arabic": "ثلاثة", "english": "three"},
    {"arabic": "أربعة", "english": "four"},
    {"arabic": "خمسة", "english": "five"},
    {"arabic": "كبير", "english": "big"},
    {"arabic": "صغير", "english": "small"},
    {"arabic": "جديد", "english": "new"},
    {"arabic": "قديم", "english": "old"},
    {"arabic": "جيد", "english": "good"},
    {"arabic": "سيئ", "english": "bad"},
    {"arabic": "طويل", "english": "long"},
    {"arabic": "قصير", "english": "short"},
    {"arabic": "أول", "english": "first"},
    {"arabic": "آخر", "english": "last / other"},
    {"arabic": "رجل", "english": "man"},
    {"arabic": "امرأة", "english": "woman"},
    {"arabic": "طفل", "english": "child"},
    {"arabic": "شخص", "english": "person"},
    {"arabic": "بيت", "english": "house"},
    {"arabic": "مدينة", "english": "city"},
    {"arabic": "بلد", "english": "country"},
    {"arabic": "طريق", "english": "road / way"},
    {"arabic": "عمل", "english": "work"},
    {"arabic": "مدرسة", "english": "school"},
    {"arabic": "كتاب", "english": "book"},
    {"arabic": "ماء", "english": "water"},
    {"arabic": "طعام", "english": "food"},
    {"arabic": "وقت", "english": "time"},
    {"arabic": "يوم", "english": "day"},
    {"arabic": "سنة", "english": "year"},
    {"arabic": "عين", "english": "eye"},
    {"arabic": "يد", "english": "hand"},
    {"arabic": "قلب", "english": "heart"},
    {"arabic": "اسم", "english": "name"},
    {"arabic": "حياة", "english": "life"},
    {"arabic": "عالم", "english": "world"},
    {"arabic": "حق", "english": "truth / right"},
    {"arabic": "شيء", "english": "thing"},
    {"arabic": "أحب", "english": "I love"},
    {"arabic": "أريد", "english": "I want"},
    {"arabic": "أعرف", "english": "I know"},
    {"arabic": "أفهم", "english": "I understand"},
    {"arabic": "أرى", "english": "I see"},
    {"arabic": "أسمع", "english": "I hear"},
    {"arabic": "أقول", "english": "I say"},
    {"arabic": "أذهب", "english": "I go"},
    {"arabic": "آتي", "english": "I come"},
    {"arabic": "آكل", "english": "I eat"},
    {"arabic": "أشرب", "english": "I drink"},
    {"arabic": "أقرأ", "english": "I read"},
    {"arabic": "أكتب", "english": "I write"},
    {"arabic": "أنظر", "english": "I look"},
    {"arabic": "أعطي", "english": "I give"},
    {"arabic": "آخذ", "english": "I take"}
]

def game(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the english translation of '{word['arabic']}'?")
        user_input = input('Your answer: ').strip().lower()
        correct_answer = word['english'].lower()
        if user_input == correct_answer:
            print('Amazin Correct answer!')
            score += 1
        else:
            print(f"Lol wrong answer, correct answer was '{word['english']}'")
        con = input('want to continue (y/n): ?').lower()

        if con == 'y':
            continue
        else:
            break
        
    print(f'Quiz complete, Your score is {score}/{len(words)}')


def main():
    print(' Welcome to the language app')
    input('Press enter to start..')
    game(words)

main()






























