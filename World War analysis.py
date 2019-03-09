from collections import Counter
import nltk
def download(WW):
    text = ''
    for line in WW:
        if line != '\n':
            text = text + line.replace('п»ї', '')
    return text


def shorties(text):
    textnew = ''
    textnew = textnew+text.replace('It\'s', 'It is').replace('that\'s', 'that is').replace('won\'t', 'will not').replace('n\'t', ' not').replace('\'ll', ' will').replace('\'re', ' are').replace('there\'s', 'there is').replace('it\'s', 'it is').replace('\'m', ' am').replace('She\'s', 'She is').replace('\'d', 'would').replace('\'ve', ' have').replace('That\'s', 'That is').replace('he\'s', 'he is').replace('Who\'s', 'Who is').replace('He\'s', 'He is')
    return textnew


def signs(text, Results):
    sign = '.,?!;:\'\"-'
    amount = {}
    sum = 0
    for chara in sign:
        amount[chara] = 0
        for letter in text:
            if chara == letter:
                amount[chara] = amount[chara]+1
    for chara in sign:
        sum = sum + amount[chara]
    for chara in sign:
        Results.write(chara+5*' '+str("%.5f" % (amount[chara]*100/sum))+'\n')
    Results.write('\n')


def clear(text):
    sent = ''
    for line in text:
        sent = sent + line.replace('\n', ' ').replace('  ', ' ').replace('-', '').replace(',', '').replace(';', '').replace('\'', '').replace('?', '').replace('.', '').replace(':', '').replace('!', '').replace('"', '')
    sent = sent.replace('  ', ' ')
    sent = sent.lstrip()
    return sent


def freque(text, Results):
    words = text.split(' ')
    freq = Counter(word.lower() for word in words)
    for word, count in freq.most_common():
        Results.write(('{}'+(20-len(word))*' '+"%.5f" % (count/len(freq))+'\n').format(word))
    Results.write('\n')

def morph(text, Results):
    collection = nltk.pos_tag(text)
    amount = []
    for item in collection:
      amount.append(item[1])
    freq = Counter(dunno for dunno in amount)
    for word, count in freq.most_common():
        Results.write(('{}' + (20 - len(word)) * ' '+'{}\n').format(word, count))
    Results.write('\n')


WW1 = open('WW1 songs.txt', 'r')
WW2 = open('WW2 songs.txt', 'r')
Results = open('Results.txt', 'w')
text1 = download(WW1)
text2 = download(WW2)
text1 = shorties(text1)  # Убираем всякие непонятные сокращения
text2 = shorties(text2)
signs(text1, Results)  # Рассчитыаем количество знаков в предложениях и их частоту использования
signs(text2, Results)
text1 = clear(text1)  # Убираем знаки из текстов
text2 = clear(text2)
freque(text1, Results)  # Рассчитываем частоту слов в текстах
freque(text2, Results)
morph(text1, Results)  # Рассчитываем частоту использования частей речи
morph(text2, Results)
