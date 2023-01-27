import collections
import re

fukaka = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'] #алфавіт                        
dovzhyna_fu = len(fukaka)

keyList = ['да', 'три', 'гора', 'панда', 'лопата', 'литература', 'архитектоника', 'диакритический', 'авторизационный', 'автопутеводитель', 'автокомплектующие', 'благоприобретенный', 'бактериостатический', 'автоматизированность']

with open("text.txt", 'r', encoding='utf-8') as task1:
    opent = re.sub(r'[^а-яё]', '', task1.read().replace("\n","").replace(" ","").lower().replace("ё", "е"))

with open("var11.txt", 'r', encoding='utf-8') as var11:
	opent2 = var11.read()
	opent2 = opent2.replace('\n',"")

print(opent)


def Index(text): #обчислюємо індекс відповідності 
    x = dict(collections.Counter(text))
    i = []
    for key in list(x.keys()):
        i.append(x[key]*(x[key]-1))
    I = 1/(len(text)*(len(text)-1))*sum(i)
    return(I)


def DecodeTxt(chipertxt, keys): #здійснюємо розшифрування шифротексту 
    h=0
    txt = ''
    for i in chipertxt:
        txt += fukaka[(fukaka.index(i) - fukaka.index(keys[h]))%32]
        h+=1
        if (h >= len(keys)):
            h = 0
    return(txt)  
    
    
def EncodeTxt(txt, keys): 
    chipertxt = ''
    h=0
    for j in txt:
        chipertxt += fukaka[(fukaka.index(j) + fukaka.index(keys[h]))%32]
        h+=1
        if (h >= len(keys)):
            h = 0
    return(chipertxt)   


def Block(text, r): #розбиваємо текст на блоки
	blc=list()
	for i in range(r):
		blc.append('')
		j=i
		while(j<len(text)):
			blc[i] = blc[i]+text[j]
			j+=r
	return blc



def IndEachBl(txt, l): #шукаємо індекс відповідності для кожного блоку, щоб порівняти їхні значення між собою.
    parts = Block(txt, l) 
    index = 0
    for j in range(len(parts)):
        index = index + Index(parts[j])
    index = index/l
    return index


def FindKey(txt, l, letter): #пошук ключів для декодування, спираючись на проведений криптоаналіз (отримані значення індексу відповідності)
    parts = Block(txt, l)
    bukva = ''
    i = 0
    while i < len(parts):
        lba = collections.Counter(parts[i]).most_common(1)[0]
        bukva += fukaka[(fukaka.index(lba[0]) -fukaka.index(letter))%32]
        i += 1
    print(bukva)


def FirstTask(text): 
    print('---------------Завдання №1---------------')
    print("Iндекс відповідності для відкритого тексту:",Index(text), "\n")
    for i in keyList:
    	print("Довжина ключа",len(i),":",Index(EncodeTxt(text, i)))


def SecondTask(text):
	print('---------------Завдання №2---------------') 
	for i in range(2, len(fukaka)):   
		print("Довжина ключа", i,':', IndEachBl(text, i))
	print('-----------------------------------')
	for letter in 'оеа':
    		FindKey(opent2, 17, letter)  # довжина ключа, що має необхідний індекс збіжності
	print("-----------------------------------")
	print(DecodeTxt(text, 'венецианскийкупец'))
	
FirstTask(opent)
print('-----------------------------------')
print(EncodeTxt(opent, 'авторизационный'))
SecondTask(opent2)
