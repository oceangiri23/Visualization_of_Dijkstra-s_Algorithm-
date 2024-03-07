from  tkinter import messagebox, Tk   #  GUI toolkit
import pygame
import sys
from Not_Found import show_message_box

window_height = 600
window_width = 600
pygame.init()

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Visualization of Dijkstra's algorithm")


count = 0
columns = 30
rows = 30
box_width =  window_width / columns
box_height = window_height / rows

grid = []
queue = []
path = []


class Box:
    def __init__(self,i,j):
        self.x=  i
        self.y = j 
        self.start = False
        self.wall = False
        self.target = False
        self.queued = False
        self.visited = False
        self.neighbours = []
        self.prior = None


    def draw(self, win, color):
        pygame.draw.rect(win, color, (self.x * box_width, self.y * box_height , box_width-2, box_height-2))

    def set_neighbours(self):
        if self.x>0:
            self.neighbours.append(grid[self.x-1][self.y])
        if self.x <columns-1:
            self.neighbours.append(grid[self.x +1][self.y])
        if self.y >0:
            self.neighbours.append(grid[self.x][self.y-1])
        if self.y < rows-1:
            self.neighbours.append(grid[self.x][self.y +1])


#creating grid which will be the array of array 
 #each column will be an array 
for i in range(columns):
    arr=[]
    for j in range(rows):
        arr.append(Box(i,j))
    grid.append(arr)

# set neighbours
for i in range(columns):
    for j in range(rows):
        grid[i][j].set_neighbours()

start_box = grid[0][0]
start_box.start = True
start_box.visited = True
queue.append(start_box)

def main():
    begin_search = False
    target_box_set = False
    searching = True
    target_box = None

    while True:
        for event in pygame.event.get():

            # to quit the box 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==pygame.MOUSEMOTION:
                # x = pygame.mouse.get_pos()[0]
                # y = pygame.mouse.get_pos()[1]
                x, y = pygame.mouse.get_pos()

                #draw wall when left button is clicked
                if event.buttons[0]:
                    i = int (x // box_width)
                    j = int (y// box_height)
                    grid[i][j].wall = True
                # to set the target box
                # if event.buttons[2] and not target_box_set:
                #     i = int(x // box_width)
                #     j = int (y // box_height)
                #     target_box = grid[i][j]
                #     target_box.target = True
                #     target_box_set = True
                # # Start Searching Algorithm
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and not target_box_set :
                    print("Final Box Selected")
                    i = int (x // box_width)
                    j = int (y// box_height)
                    target_box = grid[i][j]
                    target_box.target = True
                    target_box_set = True
 
                if event.key == pygame.K_RETURN and target_box_set :
                    print("Finding the shortest route.....")
                    begin_search = True

        if begin_search :
            if len(queue) > 0 and searching :
                current_box = queue.pop(0)
                current_box.visited = True
                if current_box == target_box:
                    searching = False
                    while current_box.prior != start_box:
                        path.append(current_box.prior)
                        current_box = current_box.prior
                    print("The shortest number of Box to reach to Destination be: "+ str(len(path) +1))
                else:
                    for neighbour in current_box.neighbours:
                        if not neighbour.queued and not neighbour.wall:
                            neighbour.queued = True
                            neighbour.prior = current_box # this defines prior box for each box 
                            queue.append(neighbour)

            
            else:
                if searching:
                    show_message_box("Error !", "Path Not Found.")

                    


        window.fill((64,64,64))

        #now we need to draw the boxes 
        for i in range(columns):
            for j in range(rows):
                Box = grid[i][j]
                Box.draw(window,(200,200,200))

                if Box.queued:
                    Box.draw(window,(0,255,0))
                if Box.visited:
                    Box.draw(window,(0,200,200))
                if Box in path :
                    Box.draw(window, (0,0,204))

                if Box.start:
                    Box.draw(window, (0,0,200))
                if Box.wall:
                    Box.draw(window, (90,90,90))
                if Box.target:
                    Box.draw(window,(255,0,0))
        
        pygame.display.flip()


main()



