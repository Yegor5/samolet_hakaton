SKIDKA = {'скидкам', 'скидках', 'скидка', 'скидкой', 'скидок', 'скидку', 'скидке', 'скидки', 'скидками'}
PERCENT = {'процента', 'процентами', 'процентов', 'проценту', 'процентам', 'процент', 'проценты', 'процентом'}

def text2num_fast(text: str) -> int:
    dictionary = {'два': 2,
        'двух': 2,
        'пятнадцать': 15,
        'три': 3,
        'триста': 300,
        'пятьдесят': 50,
        'тысяч': 1000,
        'один': 1,
        'пять': 5,
        'сто': 100,
        'десять': 10,
        'двести': 200,
        'четыре': 4,
        'пяти': 5,
        'восемь': 8,
        'двадцать': 20,
        'одного': 1,
        'девять': 9,
        'восемьсот': 800,
        'одну': 1,
        'девяти': 9,
        'шесть': 6,
        'шестьсот': 600,
        'шестьдесят': 60,
        'пятьсот': 500,
        'девяносто': 90,
        'две': 2,
        'восьми': 8,
        'девятьсот': 900,
        'тридцать': 30,
        'восемнадцать': 18,
        'шестнадцать': 16,
        'двенадцать': 12,
        'одиннадцать': 11,
        'ноль': 0,
        'семь': 7,
        'десяти': 10,
        'тринадцать': 13,
        'тысячи': 1000,
        'семьсот': 700,
        'пятнадцати': 15,
        'трех': 3,
        'одна': 1,
        'четырех': 4,
        'семи': 7,
        'семнадцать': 17,
        'тринадцати': 13,
        'шести': 6,
        'двенадцати': 12,
        'четыреста': 400,
        'трехсот': 300,
        'пятидесяти': 50,
        'двум': 2,
        'восемнадцати': 18,
        'сорока': 40,
        'сорок': 40,
        'четырнадцать': 14,
        'девятьнадцать': 19,
        'семьдесят': 70,
        'восемдесят': 80,
        'тысяча': 1000
    }
    try:
        return dictionary[text]
    except KeyError:
        return None