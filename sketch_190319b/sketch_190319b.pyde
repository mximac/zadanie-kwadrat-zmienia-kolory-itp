global pos1
global pos2
pos1=0
pos2=75  # lepiej stosować wartości uniwersalne stworzone w oparciu o wbudowane zmienne
def setup():
    size(200,200)
def draw():
    background(255)
    kolory=(100,255,0,125,199,130,150,59) #wartosci z ktorych program sobie jakas wylosuje i przypisze do zmiennej r1, potem to samo do r2 i r3
    r1=int(random(7))
    r2=int(random(7))
    r3=int(random(7))  # losowanie to trochę pójście na łątwiznę
    fill(kolory[r1],kolory[r2],kolory[r3]) #wylosowane z listy wartosci beda kolejno RGB r1=R r2=G r3=B wiec stworza jakis kolor
    global pos1
    global pos2
    rect(pos1,pos2,50,50)
    if mousePressed: #trzeba trzymac przycisk zeby kwadrat sie poruszal
        pos1+=1
        pos2-=1
    if pos1==75 and pos2==0: #sprawdzamy czy kwadrat jest na srodku gornego boku, jak tak to nie powtarzamy petli draw()
        noLoop()
