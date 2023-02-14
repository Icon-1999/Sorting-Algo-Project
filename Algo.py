import pygame, sys, time
import random

pygame.init()
clock = pygame.time.Clock()

#screen (w, h)
screen = pygame.display.set_mode((850, 500))

#make arrays from 1-100
array = [0] * 101
array_color = [0]*101
line_color =[(65,105,225), (250,128,114), 
(250,128,114), (255, 102, 0)]
num_switch = 0

header_font = pygame.font.SysFont("strong", 30)
common_font = pygame.font.SysFont("strong", 20)

#randomize array
def NewArray():
    for i in range (0, 101):
        array_color[i]= line_color[0]
        array[i] = i+1
    random.shuffle(array)
NewArray()

def update_model():
    screen.fill((255, 255, 255))
    draw()
    pygame.display.update()
    pygame.time.delay(20)

#insertion sort array
def insertionSort(array, ascending=True):
    for i in range(1, len(array)):
        tmp = array[i]
        j = i-1
        while j >= 0 and tmp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = tmp
        array_color[i]= line_color[1]
        update_model()

#selection sort array
def selectionSort(array, ascending=True):
    for i in range(len(array)):
        min_idx = i
        array_color[i]= line_color[1]
        update_model()
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j    
        array[i], array[min_idx] = array[min_idx], array[i]

def switch(num_switch):
    if (num_switch == 0):
        return 1

    if (num_switch == 1):
        return 0

def draw():
    screen.fill((255, 255, 255))

    if (num_switch == 0):
        header_txt = header_font.render("Algo Visualizer - Insertion Sort", 1, (0, 0, 0))
        screen.blit(header_txt, (20, 10))
    if (num_switch == 1):
        header_txt = header_font.render("Algo Visualizer - Selection Sort", 1, (0, 0, 0))
        screen.blit(header_txt, (20, 10))

    common_txt1 = common_font.render("Press 'space' to start sorting", 1, (0, 0, 0))
    screen.blit(common_txt1, (20, 40))

    common_txt2 = common_font.render("Press 'n' for new Array", 1, (0, 0, 0))
    screen.blit(common_txt2, (20, 60))

    common_txt3 = common_font.render("Press 'c' to change Sort", 1, (0, 0, 0))
    screen.blit(common_txt3, (20, 80))

    width = (800-150)//150
    boundry_arr = 850 / 100
    boundry_grp = 500 / 130
    #black line
    pygame.draw.line(screen, (192,192,192), 
                    (0, 100), (900, 100), 6)
    #bg grid
    for i in range(1, 101):
        pygame.draw.line(screen, (224, 225, 224), (0, boundry_grp * i + 100), (900, boundry_grp * i + 100), 1)
      
    # Drawing the array values as lines
    for i in range(1, 101):
        pygame.draw.line(screen, array_color[i], (boundry_arr * i-3, 800),(boundry_arr * i-3, 400 - array[i]*boundry_grp + 100), width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                NewArray()
            if event.key == pygame.K_c:
                NewArray()
                num_switch = switch(num_switch)
                print(num_switch)
            if event.key == pygame.K_SPACE:
                if (num_switch == 0):
                    insertionSort(array)
                if (num_switch == 1):
                    selectionSort(array)
    draw()
    pygame.display.update()

    pygame.display.update()
    clock.tick(60)