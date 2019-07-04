ones = ["", "واحد ", "اثنان ", "ثلاثة ", "اربعة ", "خمسة ", "ستة ", "سبعة ", "ثمانية ", "تسعة ", "عشرة ", "احدي عشرة ","اثنا عشرة ", "ثلاثة عشرة ", "أربعة عشرة ", "خمسة عشرة ", "ستة عشرة ", "سبعة عشرة ", "ثمانية عشرة ", "تسعة عشرة "]
ones_2 = ["", "", "", "ثلاث", "اربع", "خمس", "ست", "سبع", "ثماني", "تسع"]
twenties = ["", "", "عشرون ", "ثلاثون ", "اربعون ","خمسون ", "ستون ", "سبعون ", "ثمانون ", "تسعون "]
thousands = ["", "الف ", "مليون ", "بليون ", "تريليون "]


def num999(n):
    c = n % 10  # singles digit
    b = ((n % 100) - c) / 10  # tens digit
    a = ((n % 1000) - (b * 10) - c) / 100  # hundreds digit
    t = ""
    h = ""
    if a != 0 and b == 0 and c == 0:
        if ones[int(a)] == ones[1]:
            t = ones_2[int(a)] + "مائه "
        elif ones[int(a)] == ones[2]:
            t = "مئتان "
        else:
            t = ones_2[int(a)] + "مائه "

    elif a != 0:
        if ones[int(a)] == ones[1]:
            t = "مائه و "
        elif ones[int(a)] == ones[2]:
            t = "مئتان و "
        else:
            t = ones_2[int(a)] + "مائه و "
    if b <= 1:
        h = ones[n % 100]
    elif b > 1:
        if ones[int(c)]:
            h = ones[int(c)] + ' و ' + twenties[int(b)]
        else:
            h = twenties[int(b)]
    st = t + h
    return st


def num2word(input):
    num = int(input)
    if num == 0: return 'صفر'
    i = 3
    n = str(num)
    word = ""
    k = 0
    while(i == 3):
        nw = n[-i:]
        n = n[:-i]
        if int(nw) == 0:
            word = num999(int(nw)) + thousands[int(nw)] + word
        else:
            first_num = num999(int(nw))
            if num < 11:
                word = first_num
            elif first_num == ones[1]:
                if word:
                    word = ' و ' + word
                word = thousands[int(k)] + word
            elif first_num == ones[2]:
                if word:
                    word = ' و ' + word
                word = 'الفان ' + word
            elif first_num in ones[3:11]:
                if word:
                    word = ' و ' + word
                word = first_num + 'آلاف ' + word
            else:
                if word:
                    word = ' و ' + word
                word = first_num + thousands[int(k)] + word 
        if n == '':
            i = i+1
        k += 1

    input_fraction = input - num
    input_fraction = round(input_fraction,2)
    input_fraction = str(input_fraction)
    input_fraction = input_fraction[2:]
    word = ' فقط وقدرة ' + word[:-1] + ' جنيه مصري '
    if input_fraction and int(input_fraction) !=0:
        input_fraction = ' و ' + input_fraction + '\\100'
        return word + input_fraction
    else:
        return word
