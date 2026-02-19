def task1():
    words = ['elephant', 'fly', 'computer', 'planet', 'guitar', 'dog',
             'box', 'car', 'keyboard', 'sky', 'ant', 'ocean', 'street',
             'cat', 'window', 'river', 'forest', 'sun', 'giraffe', 'mountain']

    n = 0
    for word in words:
        if len(word) == 3:
            n += 1

    print(f'В этой строке {n} слов из трех букв ')

def task2():
    words = ['elephant', 'fly', 'computer', 'planet', 'guitar', 'dog',
             'box', 'car', 'keyboard', 'sky', 'ant', 'ocean', 'street',
             'cat', 'window', 'river', 'forest', 'sun', 'giraffe', 'mountain']

    # index_list = []
    # for i in range(len(words)):
    #     print(i, end=' ')
    #     if len(words[i]) == 3:
    #         index_list.append(i)
    # print(index_list)

    index_list = []
    for i in words:
        if len(i) == 3:
            ind_ = words.index(i)
            index_list.append(ind_)
    print(index_list)

def task3():
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [2, 3, 4, 5, 6]
    sum_list = []

    for i, j in zip(list_1, list_2):
        sum_list.append(i + j)
    print(sum_list)

def task4():
    names = ['Александр', 'Наполеон', 'Лао']
    surnames = ['Македонский', 'Бонапарт', 'Цзы']
    fio = []

    for i, j in zip(names, surnames):
        fio.append(i + ' ' + j)
    for k in fio:
            print(k)

def task5():
    pass
# Нfйдем минимум функции y = x^2 - 6x +4
# Переберем значения x на достаточно большом множестве и для каждого
# вычислим значение функции. Сложим все значение в список и выберем наименьшее.
    y_list = []
    for x in range(-100,100):
        y = x**2 - 6*x +4
        y_list.append(y)
    print(y_list[:10])
    print(min(y_list))

def task6():
    text = """После гибели своего отца, Филиппа II, Александр в возрасте 20 лет был объявлен царём. Он подавил
               восстание фракийцев и заново подчинил Грецию, где были разрушены мятежные Фивы. В 334 году до н. э.
               Александр переправился в Малую Азию, начав таким образом войну с Персидской державой.
               При Гранике он разгромил сатрапов, а при Иссе (333 год до н. э.) — самого царя Дария III, после чего подчинил Сирию,
               Палестину и Египет. В 331 году до н. э. при Гавгамелах в Месопотамии Александр одержал решающую победу. Дарий позже был
               убит; Александр, заняв внутренние районы Персии, принял титул «царь Азии», окружил себя представителями восточной знати
                и начал думать о завоевании мира. За три года (329—326 годы до н. э.) он завоевал Среднюю Азию, а потом вторгся в Индию,
                но утомлённое войско отказалось идти дальше. Александр повернул назад и в 324 году до н. э. прибыл в Вавилон, ставший его
                столицей. В следующем году, во время подготовки к походу в Аравию, Александр умер в возрасте тридцати двух лет."""

    text = text.replace('(', ' ').replace('-', ' ')
    count1 = 0
    text_tokenize = text.split()
    num_text = []
    for i in text_tokenize:
        if i.isdigit():
            num_text.append(i)
            count1 += 1

    print(num_text, count1)


task6()



