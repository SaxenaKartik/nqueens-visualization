import pygame
import sys
from pygame.locals import * 
import time
import random
import subprocess
import math

pygame.init()
display = pygame.display.set_mode((700,700))
pygame.display.set_caption('NQUEENS')
clock = pygame.time.Clock()

boardLength=0
a=0
count=0
size = 40
white,black,red = (255,255,255),(0,0,0),(255,0,0)

def buildagain(p):

	if(p==0):
		for i in range(1,boardLength+1):
		    for z in range(1,boardLength+1):
		        #check if current loop value is even
		        if i%2==1:
			        if z % 2 == 1 :
			            pygame.draw.rect(display, white,[size*z,size*i,size,size])
			        else:
			            pygame.draw.rect(display, black, [size*z,size*i,size,size])
		        else:
		        	if z % 2 == 1 :
			            pygame.draw.rect(display, black,[size*z,size*i,size,size])
			        else:
			            pygame.draw.rect(display, white, [size*z,size*i,size,size])
		    #since theres an even number of squares go back one value
		    # cnt-=1
		#Add a nice boarder
		pygame.draw.rect(display,white,[size,size,boardLength*size,boardLength*size],1)

	else:
		print(a)
		for i in range(1,boardLength+1):
		    for z in range(1,boardLength+1):
		        #check if current loop value is even
		        if i%2==1:
			        if z % 2 == 1 :
			            pygame.draw.rect(display, white,[size*(z+boardLength*p+p),size*i,size,size])
			        else:
			            pygame.draw.rect(display, black, [size*(z+boardLength*p+p),size*i,size,size])
		        else:
		        	if z % 2 == 1 :
			            pygame.draw.rect(display, black,[size*(z+boardLength*p+p),size*i,size,size])
			        else:
			            pygame.draw.rect(display, white, [size*(z+boardLength*p+p),size*i,size,size])
		    #since theres an even number of squares go back one value
		    # cnt-=1
		#Add a nice boarder
		pygame.draw.rect(display,white,[size,size,boardLength*size,boardLength*size],1)


def buildboard():
	global boardLength 
	boardLength = int(input("Enter the value of N : "))
	f = open("input", "w")
	f.write(str(boardLength) + "\n")
	f.close()
	display.fill(black)
	cnt = 0
	for i in range(1,boardLength+1):
	    for z in range(1,boardLength+1):
	        #check if current loop value is even
	        if i%2==1:
		        if z % 2 == 1 :
		            pygame.draw.rect(display, white,[size*z,size*i,size,size])
		        else:
		            pygame.draw.rect(display, black, [size*z,size*i,size,size])
	        else:
	        	if z % 2 == 1 :
		            pygame.draw.rect(display, black,[size*z,size*i,size,size])
		        else:
		            pygame.draw.rect(display, white, [size*z,size*i,size,size])
	    #since theres an even number of squares go back one value
	    # cnt-=1
	#Add a nice boarder
	pygame.draw.rect(display,white,[size,size,boardLength*size,boardLength*size],1)
	pygame.display.update()



	
def nqueens():
	f = open("input", "r")
	of = open("output", "w")
	subprocess.call(["./nqueens1"],stdin = f, stdout = of)
	of.close()	

	first_x=60
	first_y=60

	global boardLength	
	print(boardLength)
	of = open("output","r")

	if(of.readlines()[-1]=="YES\n"):
		print("Possible solution")
	else:
		print("Impossible solution")
		display.fill(black)
		return 

	of.close()
	of = open("output", "r")

	plot_matrix = [[0 for x in range(boardLength)] for y in range(boardLength)]

	# for i in range (0, boardLength ):
	# 	for j in range(0, boardLength ):
	# 		plot_matrix[i][j] = (60,60);
	# 		# print(plot_matrix[i][j])
		# print("\n")

	for i in range (0, boardLength):
		for j in range(0, boardLength + 0):
			plot_matrix[i][j] = [60+j*40,60+i*40];


	queens = [[0 for x in range(boardLength)] for y in range(boardLength)]
	

	lines = of.readlines()
	lines = lines[:-1]
		

	i=0
	j=0
	for line in lines:
		# for i in range (0, boardLength):
		# 	for j in range(0, boardLength + 0):
		if(line.split() == []):
			global count
			count=0
			time.sleep(0.2)
			buildagain(0)
			# for i in range (0, boardLength):
			# 	for j in range(0, boardLength + 0):
			# 		print(queens[i][j],end=' ')
			# 	print("")
			# print("")
			for i in range(0,boardLength):
				for j in range(0, boardLength):
					if(queens[i][j]==1):
						x_pos,y_pos=plot_matrix[i][j]
						pygame.draw.circle(display, red, (x_pos, y_pos), 10)
						count+=1
						if(count==boardLength):
							global a
							a+=1
							buildagain(a)
							for i in range(0,boardLength):
								for j in range(0, boardLength):
									if(queens[i][j]==1):
										x_pos,y_pos=plot_matrix[i][j]
										pygame.draw.circle(display, red, (x_pos+200*a, y_pos), 10)
										time.sleep(0.01)
						pygame.display.update()
				# 		print(x_pos,y_pos,end=" ")
				# print("")
			

			i=0
			continue;

		

		j=0
		for num in line.split():
			queens[i][j] = int(num)
			j+=1
		i+=1

		# print("")

		
	# for line in of:
	# 	j=0
	# 	for num in line.split():
	# 		queens[i][j] = int(num)
	# 		j+=1
	# 	i+=1

	# for i in range (0, boardLength):
	# 	for j in range(0, boardLength + 0):
	# 		print(queens[i][j], " ")
	# 	print("\n")

		# for i in range (0, boardLength):
		# 	for j in range(0, boardLength + 0):
		# 		print(queens[i][j]," ")
		# 	print("\n")
	# for i in range (0, boardLength):
	# 	for j in range(0, boardLength):
	# 		# plot_matrix[i][j] = (60,60);
	# 		print([i,j],plot_matrix[i][j])
	# 	print("\n")



# while 1:
#     # 5 - clear the screen before drawing it again
#     # screen.fill(0)
#     # 6 - draw the screen elements
#     # screen.blit(player, (100,100))
#     # 7 - update the screen
#     pygame.display.flip()
#     # 8 - loop through the events
#     for event in pygame.event.get():
#         # check if the event is the X button
#         if event.type==pygame.QUIT:
#             # if it is quit the game
#             pygame.quit()
#             exit(0)

# crashed = False

# #board length, must be even
# boardLength = 8
# display.fill(black)

# cnt = 0
# for i in range(1,boardLength+1):
#     for z in range(1,boardLength+1):
#         #check if current loop value is even
#         if cnt % 2 == 0:
#             pygame.draw.rect(display, white,[size*z,size*i,size,size])
#         else:
#             pygame.draw.rect(display, black, [size*z,size*i,size,size])
#         cnt +=1
#     #since theres an even number of squares go back one value
#     cnt-=1
# #Add a nice boarder
# pygame.draw.rect(display,white,[size,size,boardLength*size,boardLength*size],1)

# pygame.display.update()


while 1:
	for event in pygame.event.get():
		pygame.draw.rect(display, (255, 255, 255), (100, 500, 120, 50))	
		mf = pygame.font.SysFont("monospace", 20)		
		label = mf.render("Start", 2, black)
		display.blit(label, (110, 512))

		pygame.draw.rect(display, (255, 255, 255), (400, 500, 200, 50))	
		# mf = pygame.font.SysFont("monospace", 20)
		label = mf.render("Place Queens", 2, black)
		display.blit(label, (410, 512))

		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		# print(event)
		elif event.type == MOUSEBUTTONDOWN:
			mouse_pos = list(pygame.mouse.get_pos())
			print (mouse_pos[0], mouse_pos[1])
			x, y = mouse_pos

			if 100<=x<=220 and 500<=y<=550:
				display.fill(black)
				buildboard()
			elif 400<=x<=600 and 500<=y<=550:
				a=0
				nqueens()


	pygame.display.update()
	# clock.tick(60)