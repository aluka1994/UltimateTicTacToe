import sys
import random
import signal
#Timer handler, helper function
class TimedOutExc(Exception):
        pass
def handler(signum, frame):
    #print 'Signal handler called with signal', signum
    raise TimedOutExc()
class Manual_player:
	def __init__(self):
		pass
	def move(self, temp_board, temp_block, old_move, flag):
		print 'Enter your move: <format:row column> (you\'re playing with', flag + ")"	
		mvp = raw_input()
		mvp = mvp.split()
		return (int(mvp[0]), int(mvp[1]))

class Player1:
	
	def __init__(self):
		pass

	def move(self,temp_board,temp_block,old_move,flag):
#		while(1):
#			pass
		for_corner = [0,2,3,5,6,8]

		#List of permitted blocks, based on old move.
		blocks_allowed  = []

		if old_move[0] in for_corner and old_move[1] in for_corner:
			## we will have 3 representative blocks, to choose from

			if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
				## top left 3 blocks are allowed
				blocks_allowed = [0, 1, 3]
			elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
				## top right 3 blocks are allowed
				blocks_allowed = [1,2,5]
			elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
				## bottom left 3 blocks are allowed
				blocks_allowed  = [3,6,7]
			elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
				### bottom right 3 blocks are allowed
				blocks_allowed = [5,7,8]
			else:
				print "SOMETHING REALLY WEIRD HAPPENED!"
				sys.exit(1)
		else:
		#### we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
			if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
				## upper-center block
				blocks_allowed = [1]
	
			elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
				## middle-left block
				blocks_allowed = [3]
		
			elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
				## lower-center block
				blocks_allowed = [7]

			elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
				## middle-right block
				blocks_allowed = [5]
			elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
				blocks_allowed = [4]

	# We get all the empty cells in allowed blocks. If they're all full, we get all the empty cells in the entire board.
		cells = get_empty_out_of(temp_board, blocks_allowed)
		return cells[random.randrange(len(cells))]

class Player2:
	
	def __init__(self):
		pass
	def move(self,temp_board,temp_block,old_move,flag):
		for_corner = [0,2,3,5,6,8]

		#List of permitted blocks, based on old move.
		blocks_allowed  = []

		if old_move[0] in for_corner and old_move[1] in for_corner:
			## we will have 3 representative blocks, to choose from

			if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
				## top left 3 blocks are allowed
				blocks_allowed = [0, 1, 3]
			elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
				## top right 3 blocks are allowed
				blocks_allowed = [1,2,5]
			elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
				## bottom left 3 blocks are allowed
				blocks_allowed  = [3,6,7]
			elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
				### bottom right 3 blocks are allowed
				blocks_allowed = [5,7,8]
			else:
				print "SOMETHING REALLY WEIRD HAPPENED!"
				sys.exit(1)
		else:
		#### we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
			if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
				## upper-center block
				blocks_allowed = [1]
	
			elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
				## middle-left block
				blocks_allowed = [3]
		
			elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
				## lower-center block
				blocks_allowed = [7]

			elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
				## middle-right block
				blocks_allowed = [5]
			elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
				blocks_allowed = [4]
	# We get all the empty cells in allowed blocks. If they're all full, we get all the empty cells in the entire board.
		cells = get_empty_out_of(temp_board,blocks_allowed)
		return cells[random.randrange(len(cells))]

class Player72:
	def __init__(self):
		pass
	def move(self,temp_board,temp_block,old_move,flag):
		a = -100000
		b = 100000
		return self.alphabeta(temp_board[:],temp_block[:] ,4 , a , b, True,old_move,flag)
	
	def alphabeta(self,board ,block ,depth , a , b,maximizingPlayer,old_move,flag):
		if(depth == 0):
			#print flag
			return self.heu(board,block,flag,old_move)

		if maximizingPlayer:
			v = -100000
			cells = get_empty_out_of(board,self.blocks_allowed(old_move))
			print block
			for i in cells:
				temp_block = ['-']*9
				for j  in range(0,len(block)):
					temp_block[j] = block[j]

				temp_board = []
				for j in range(9):
					row = ['-']*9
					temp_board.append(row)
				for j in range(0,9):
					for k in range(0,9):
						temp_board[j][k] = board[j][k]
				
				update_lists(temp_board,temp_block,i,flag)
				vtemp = self.alphabeta(temp_board,temp_block,depth - 1, a , b , False,i,flag)				
				#print vtemp, i, depth, old_move , 0 , a , b
				if(vtemp > v):
					v = vtemp
					temp = i
				a = max(a,v)
				if(b <= a):
				#	print vtemp, temp_block, i, depth, 0
					break

			if(depth == 4):
				return temp
			else:
				return v
		else:
			v = 100000
			cells = get_empty_out_of(board,self.blocks_allowed(old_move))
			print block
			for i in cells:
		
				temp_block = ['-']*9
				for j in range(0,9):
					temp_block[j] = block[j]

				temp_board = []
				for j in range(9):
					row = ['-']*9
					temp_board.append(row)
				
				for j in range(0,9):
					for k in range(0,9):
						temp_board[j][k] = board[j][k]
				flag1 = ''
				if flag == 'x':
					flag1 = 'o'
				elif flag == 'o':
					flag1 = 'x'
				
				update_lists(temp_board , temp_block , i ,flag1 )
				vtemp = self.alphabeta(temp_board,temp_block,depth - 1, a , b , True,i,flag1)
			#	print vtemp, i, depth , old_move , a, b  , -1
			
				if(vtemp < v):
					v = vtemp
					temp = i

				b = min(b,v)
			#	print a, b, old_move
				if(b <= a):
			#		print vtemp, temp_block, i, depth, -1
					break
			return v

	def heu(self,board,block,flag,old_move):
		countX = 0
		countO = 0
		for i in block:
			if i == 'x':
				countX += 1 
			elif i == 'o':
				countO +=  1
		if (block[4] == flag):
			if(flag == 'X'):
				countX += 200
    		elif(flag == 'o'):
				countO += 200 
		for i in range(0,9):
			if(block[i] == flag):
				if((i+1 >=0 and i+1 <=8) and (i+2 >=0 and i+2 <=8)):
					if(block[i+1] == flag or block[i+2] == flag):
						if (flag == 'x'):
							countX +=30 					
						elif(flag == 'o'):
							countO +=30  
				if((i+1 >=0 and i+1 <=8) and (i-1 >=0 and i-1 <=8)):
					if(block[i+1] == flag or block[i-1] == flag):
						if (flag == 'x'):
							countX +=30 					
						elif(flag == 'o'):
							countO +=30
				if((i+1 >=0 and i+1 <=8) and (i-1 >=0 and i-1 <=8)): 
					if(block[i-1] == flag or block[i-2] == flag ):
						if (flag == 'x'):
							countX +=30 					
						elif(flag == 'o'):
							countO +=30
				if((i+1 >=0 and i+1 <=8) and (i-1 >=0 and i-1 <=8)):
					if(block[i-3] == flag or block[i+3] == flag):
						if (flag == 'x'):
							countX +=40 					
						elif(flag == 'o'):
							countO +=40		
				if((i+3 >=0 and i+3 <=8) and (i+6 >=0 and i+6 <=8)):
					if(block[i+3] == flag or block[i+6] ==flag):
						if (flag == 'x'):
							countX +=40 					
						elif(flag == 'o'):
							countO +=40
				if((i-3 >=0 and i-3 <=8) and (i-6 >=0 and i-6 <=8)):			
					if(block[i-3] == flag or block[i-6] == flag):
						if (flag == 'x'):
							countX +=40 					
					elif(flag == 'o'):
							countO +=40
				if((i+4 >=0 and i+4 <=8) and (i+8 >=0 and i+8 <=8)):					
					if(block[i+4] == flag or block[i+8] ==flag ):
						if (flag == 'x'):
							countX += 50 
						if (flag == 'o'):
							countO += 50
				if((i-4 >=0 and i-4 <=8) and (i+4 >=0 and i+4 <=8)):					
					if(block[i+4] == flag or block[i-4] ==flag ):
						if (flag == 'x'):
							countX += 50 
						if (flag == 'o'):
							countO += 50
				if((i-4 >=0 and i-4 <=8) and (i-8 >=0 and i-8 <=8)):					
					if(block[i-4] == flag or block[i-8] ==flag ):
						if (flag == 'x'):
							countX += 50 
						if (flag == 'o'):
							countO += 50
		#bloc_heuristic(num,board,flag,old_move)								        	 
		if (flag == 'o'):
			return countO-countX			
		return countX-countO

	def bloc_heuristic(self,num,board,flag,old_move):
		l= []
		if num == 1:
			r =  heu(board,block,flag,old_move)
			l.append(r)
		if num == 2:
			r =  heu(board,block,flag,old_move)
			l.append(r)
               	if num == 3:
			r =  heu(board,block,flag,old_move)
			l.append(r)


		print "heyyy"
		print l

			
			
		
		
		
		
		
	def block_hue(num,board):
		a = []
		for i in range(3):
			row = ['-']*3
			board.append(row)
		
		row = (num/3)*3
		column = (num%3)*3
		for i in range(0,3):
			for j in range(0,3):
				a[i][j] = board[row+i][column+j]

		for i in range(0,3):
			count1 = 0
			count2 = 0
			if(a[i][0]=='X'):
				count1 += 1
						
			if(a[i][1]=='X'):
				count1 += 1
			else:
				count2 += 1
			if(a[i][2]=='X'):
				count1 += 1
	
	def blocks_allowed(self,old_move):
		blocks_allowed  = []
		for_corner = [0,2,3,5,6,8]

		if old_move[0] in for_corner and old_move[1] in for_corner:
			## we will have 3 representative blocks, to choose from

			if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
				## top left 3 blocks are allowed
				blocks_allowed = [0, 1, 3]
			elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
				## top right 3 blocks are allowed
				blocks_allowed = [1,2,5]
			elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
				## bottom left 3 blocks are allowed
				blocks_allowed  = [3,6,7]
			elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
				### bottom right 3 blocks are allowed
				blocks_allowed = [5,7,8]
			else:
				print "SOMETHING REALLY WEIRD HAPPENED!"
				sys.exit(1)
		else:
		#### we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
			if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
				## upper-center block
				blocks_allowed = [1]
	
			elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
				## middle-left block
				blocks_allowed = [3]
		
			elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
				## lower-center block
				blocks_allowed = [7]

			elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
				## middle-right block
				blocks_allowed = [5]
			elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
				blocks_allowed = [4]

		return blocks_allowed


#Initializes the game
def get_init_board_and_blockstatus():
	board = []
	for i in range(9):
		row = ['-']*9
		board.append(row)
	
	block_stat = ['-']*9
	return board, block_stat

# Checks if player has messed with the board. Don't mess with the board that is passed to your move function. 
def verification_fails_board(board_game, temp_board_state):
	return board_game == temp_board_state	

# Checks if player has messed with the block. Don't mess with the block array that is passed to your move function. 
def verification_fails_block(block_stat, temp_block_stat):
	return block_stat == temp_block_stat	

#Gets empty cells from the list of possible blocks. Hence gets valid moves. 
def get_empty_out_of(gameb, blal):
	cells = []  # it will be list of tuples
	#Iterate over possible blocks and get empty cells
	for idb in blal:
		id1 = idb/3
		id2 = idb%3
				
		for i in range(id1*3,id1*3+3):
			for j in range(id2*3,id2*3+3):
				if gameb[i][j] == '-':
					cells.append((i,j))

	# If all the possible blocks are full, you can move anywhere
	if cells == []:
		for i in range(9):
			for j in range(9):
				if gameb[i][j] == '-':
					cells.append((i,j))	
		
	return cells


		
# Note that even if someone has won a block, it is not abandoned. But then, there's no point winning it again!
# Returns True if move is valid
def check_valid_move(game_board, current_move, old_move):

	# first we need to check whether current_move is tuple of not
	# old_move is guaranteed to be correct
	if type(current_move) is not tuple:
		return False
	
	if len(current_move) != 2:
		return False

	a = current_move[0]
	b = current_move[1]	

	if type(a) is not int or type(b) is not int:
		return False
	if a < 0 or a > 8 or b < 0 or b > 8:
		return False

	#Special case at start of game, any move is okay!
	if old_move[0] == -1 and old_move[1] == -1:
		return True


	for_corner = [0,2,3,5,6,8]

	#List of permitted blocks, based on old move.
	blocks_allowed  = []

	if old_move[0] in for_corner and old_move[1] in for_corner:
		## we will have 3 representative blocks, to choose from

		if old_move[0] % 3 == 0 and old_move[1] % 3 == 0:
			## top left 3 blocks are allowed
			blocks_allowed = [0, 1, 3]
		elif old_move[0] % 3 == 0 and old_move[1] in [2, 5, 8]:
			## top right 3 blocks are allowed
			blocks_allowed = [1,2,5]
		elif old_move[0] in [2,5, 8] and old_move[1] % 3 == 0:
			## bottom left 3 blocks are allowed
			blocks_allowed  = [3,6,7]
		elif old_move[0] in [2,5,8] and old_move[1] in [2,5,8]:
			### bottom right 3 blocks are allowed
			blocks_allowed = [5,7,8]

		else:
			print "SOMETHING REALLY WEIRD HAPPENED!"
			sys.exit(1)

	else:
		#### we will have only 1 block to choose from (or maybe NONE of them, which calls for a free move)
		if old_move[0] % 3 == 0 and old_move[1] in [1,4,7]:
			## upper-center block
			blocks_allowed = [1]
	
		elif old_move[0] in [1,4,7] and old_move[1] % 3 == 0:
			## middle-left block
			blocks_allowed = [3]
		
		elif old_move[0] in [2,5,8] and old_move[1] in [1,4,7]:
			## lower-center block
			blocks_allowed = [7]

		elif old_move[0] in [1,4,7] and old_move[1] in [2,5,8]:
			## middle-right blockupdate
			blocks_allowed = [5]

		elif old_move[0] in [1,4,7] and old_move[1] in [1,4,7]:
			blocks_allowed = [4]


	# We get all the empty cells in allowed blocks. If they're all full, we get all the empty cells in the entire board.
	cells = get_empty_out_of(game_board, blocks_allowed)

	#Checks if you made a valid move. 
	if current_move in cells:
		return True
	else:
		return False

def update_lists(game_board, block_stat, move_ret, fl):
	#move_ret has the move to be made, so we modify the game_board, and then check if we need to modify block_stat
	game_board[move_ret[0]][move_ret[1]] = fl


	#print "@@@@@@@@@@@@@@@@@"
	#print block_stat

	block_no = (move_ret[0]/3)*3 + move_ret[1]/3	
	id1 = block_no/3
	id2 = block_no%3
	mg = 0
	mflg = 0
	if block_stat[block_no] == '-':

		### now for diagonals
		## D1
		# ^
		#   ^
		#     ^
		if game_board[id1*3][id2*3] == game_board[id1*3+1][id2*3+1] and game_board[id1*3+1][id2*3+1] == game_board[id1*3+2][id2*3+2] and game_board[id1*3+1][id2*3+1] != '-':
			mflg=1
			mg=1
			#print "SEG: D1 found"

		## D2
		#     ^
		#   ^
		# ^
		############ MODIFICATION HERE, in second condition -> gb[id1*3][id2*3+2]
		# if game_board[id1*3+2][id2*3] == game_board[id1*3+1][id2*3+1] and game_board[id1*3+1][id2*3+1] == game_board[id1*3+2][id2*3] and game_board[id1*3+1][id2*3+1] != '-':
		if game_board[id1*3+2][id2*3] == game_board[id1*3+1][id2*3+1] and game_board[id1*3+1][id2*3+1] == game_board[id1*3][id2*3 + 2] and game_board[id1*3+1][id2*3+1] != '-':
			mflg=1
			mg=1
			#print "SEG: D2 found"

		### col-wise
		if mflg != 1:
                    for i in range(id2*3,id2*3+3):
                        #### MODIFICATION HERE, [i] was missing previously
                        # if game_board[id1*3]==game_board[id1*3+1] and game_board[id1*3+1] == game_board[id1*3+2] and game_board[id1*3] != '-':
                        if game_board[id1*3][i]==game_board[id1*3+1][i] and game_board[id1*3+1][i] == game_board[id1*3+2][i] and game_board[id1*3][i] != '-':
                                mflg = 1
				#print "SEG: Col found"
                                break

                ### row-wise
		if mflg != 1:
                    for i in range(id1*3,id1*3+3):
                        ### MODIFICATION HERE, [i] was missing previously
                        #if game_board[id2*3]==game_board[id2*3+1] and game_board[id2*3+1] == game_board[id2*3+2] and game_board[id2*3] != '-':
                        if game_board[i][id2*3]==game_board[i][id2*3+1] and game_board[i][id2*3+1] == game_board[i][id2*3+2] and game_board[i][id2*3] != '-':
                                mflg = 1
				#print "SEG: Row found"
                                break

	
	if mflg == 1:
		block_stat[block_no] = fl

	#print 
	#print block_stat
	#print "@@@@@@@@@@@@@@@@@@@@@@@"	
	return mg

#Check win
def terminal_state_reached(game_board, block_stat,point1,point2):
	### we are now concerned only with block_stat
	bs = block_stat
	## Row win
	if (bs[0] == bs[1] and bs[1] == bs[2] and bs[1]!='-') or (bs[3]!='-' and bs[3] == bs[4] and bs[4] == bs[5]) or (bs[6]!='-' and bs[6] == bs[7] and bs[7] == bs[8]):
		print block_stat
		return True, 'W'
	## Col win
	elif (bs[0] == bs[3] and bs[3] == bs[6] and bs[0]!='-') or (bs[1] == bs[4] and bs[4] == bs[7] and bs[4]!='-') or (bs[2] == bs[5] and bs[5] == bs[8] and bs[5]!='-'):
		print block_stat
		return True, 'W'
	## Diag win
	elif (bs[0] == bs[4] and bs[4] == bs[8] and bs[0]!='-') or (bs[2] == bs[4] and bs[4] == bs[6] and bs[2]!='-'):
		print block_stat
		return True, 'W'
	else:
		smfl = 0
		for i in range(9):
			for j in range(9):
				if game_board[i][j] == '-':
					smfl = 1
					break
		if smfl == 1:
			return False, 'Continue'
		
		else:
			##### check of number of DIAGONALs


			if point1>point2:
				return True, 'P1'
			elif point2>point1:
				return True, 'P2'
			else:
				return True, 'D'	


def decide_winner_and_get_message(player,status, message):
	if status == 'P1':
		return ('P1', 'MORE DIAGONALS')
	elif status == 'P2':
		return ('P2', 'MORE DIAGONALS')
	elif player == 'P1' and status == 'L':
		return ('P2',message)
	elif player == 'P1' and status == 'W':
		return ('P1',message)
	elif player == 'P2' and status == 'L':
		return ('P1',message)
	elif player == 'P2' and status == 'W':
		return ('P2',message)
	else:
		return ('NONE','DRAW')
	return


def print_lists(gb, bs):
	print '=========== Game Board ==========='
	for i in range(9):
		if i > 0 and i % 3 == 0:
			print
		for j in range(9):
			if j > 0 and j % 3 == 0:
				print " " + gb[i][j],
			else:
				print gb[i][j],

		print
	print "=================================="

	print "=========== Block Status ========="
	for i in range(0, 9, 3):
		print bs[i] + " " + bs[i+1] + " " + bs[i+2] 
	print "=================================="
	print
	

def simulate(obj1,obj2):
	
	# game board is a 9x9 list, block_stat is a 1D list of 9 elements
	game_board, block_stat = get_init_board_and_blockstatus()

	#########
	# deciding player1 / player2 after a coin toss
	pl1 = obj1 
	pl2 = obj2

	### basically, player with flag 'x' will start the game
	pl1_fl = 'x'
	pl2_fl = 'o'

	old_move = (-1, -1) ### for the first move

	WINNER = ''
	MESSAGE = ''
	TIMEALLOWED = 12000


	### These points will not keep track of the total points of both the players.
	### Instead, these variables will keep track of only the blocks won by DIAGONALS, and these points will be used only in cases of DRAW....
	p1_pts=0
	p2_pts=0

	#### printing
	print_lists(game_board, block_stat)

	while(1):
		###################################### 
		########### firstly pl1 will move
		###################################### 
		
		## just for checking that the player1 does not modify the contents of the 2 lists
		temp_board_state = game_board[:]
		temp_block_stat = block_stat[:]
	
		signal.signal(signal.SIGALRM, handler)
		signal.alarm(TIMEALLOWED)
		# Player1 to complete in TIMEALLOWED secs. 
		try:
			ret_move_pl1 = pl1.move(temp_board_state, temp_block_stat, old_move, pl1_fl)
			#print ret_move_pl1, "Pratik"
		except TimedOutExc as e:
			WINNER, MESSAGE = decide_winner_and_get_message('P1', 'L',   'TIMED OUT')
			break
			### MODIFICATION!!
		signal.alarm(0)
	
		#### check if both lists are the same!!
		if not (verification_fails_board(game_board, temp_board_state) and verification_fails_block(block_stat, temp_block_stat)):
			##player1 loses - he modified something
			WINNER, MESSAGE = decide_winner_and_get_message('P1', 'L',   'MODIFIED CONTENTS OF LISTS')
			break
		
		### now check if the returned move is valid
		if not check_valid_move(game_board, ret_move_pl1, old_move):
			## player1 loses - he made the wrong move.
			WINNER, MESSAGE = decide_winner_and_get_message('P1', 'L',   'MADE AN INVALID MOVE')
			break
			

		print "Player 1 made the move:", ret_move_pl1, 'with', pl1_fl
		######## So if the move is valid, we update the 'game_board' and 'block_stat' lists with move of pl1
		p1_pts += update_lists(game_board, block_stat, ret_move_pl1, pl1_fl)

		### now check if the last move resulted in a terminal state
		gamestatus, mesg =  terminal_state_reached(game_board, block_stat,p1_pts,p2_pts)
		if gamestatus == True:
			print_lists(game_board, block_stat)
			WINNER, MESSAGE = decide_winner_and_get_message('P1', mesg,  'COMPLETE')	
			break

		
		old_move = ret_move_pl1
		print_lists(game_board, block_stat)
		print old_move
		############################################
		### Now player2 plays
		###########################################
		
                ## just for checking that the player2 does not modify the contents of the 2 lists
                temp_board_state = game_board[:]
                temp_block_stat = block_stat[:]


		signal.signal(signal.SIGALRM, handler)
		signal.alarm(TIMEALLOWED)
		# Player2 to complete in TIMEALLOWED secs. 
		try:
                	ret_move_pl2 = pl2.move(temp_board_state, temp_block_stat, old_move, pl2_fl)
		except TimedOutExc as e:
			WINNER, MESSAGE = decide_winner_and_get_message('P2', 'L',   'TIMED OUT')
			break
		signal.alarm(0)

                #### check if both lists are the same!!
                if not (verification_fails_board(game_board, temp_board_state) and verification_fails_block(block_stat, temp_block_stat)):
                        ##player2 loses - he modified something
			WINNER, MESSAGE = decide_winner_and_get_message('P2', 'L',   'MODIFIED CONTENTS OF LISTS')
			break
			

                ### now check if the returned move is valid
                if not check_valid_move(game_board, ret_move_pl2, old_move):
                        ## player2 loses - he made the wrong move...
			WINNER, MESSAGE = decide_winner_and_get_message('P2', 'L',   'MADE AN INVALID MOVE')
			break


		print "Player 2 made the move:", ret_move_pl2, 'with', pl2_fl
                ######## So if the move is valid, we update the 'game_board' and 'block_stat' lists with the move of P2
                p2_pts += update_lists(game_board, block_stat, ret_move_pl2, pl2_fl)

                ### now check if the last move resulted in a terminal state
		gamestatus, mesg =  terminal_state_reached(game_board, block_stat,p1_pts,p2_pts)
                if gamestatus == True:
			print_lists(game_board, block_stat)
                        WINNER, MESSAGE = decide_winner_and_get_message('P2', mesg,  'COMPLETE' )
                        break
		### otherwise CONTINUE	
		old_move = ret_move_pl2
		print_lists(game_board, block_stat)

	######### THESE ARE NOT THE TOTAL points, these are just the diagonal points, (refer to the part before the while(1) loop
	####### These will be used only in cases of DRAW
	print p1_pts
	print p2_pts

	
	print WINNER
	print MESSAGE
#	return WINNER, MESSAGE, p1_pt2, p2_pt2

if __name__ == '__main__':
	## get game playing objects

	if len(sys.argv) != 2:
		print 'Usage: python simulator.py <option>'
		print '<option> can be 1 => Random player vs. Random player'
		print '                2 => Human vs. Random Player'
		print '                3 => Human vs. Human'
		sys.exit(1)
 
	obj1 = ''
	obj2 = ''
	option = sys.argv[1]	
	if option == '1':
		obj1 = Player1()
		obj2 = Player2()

	elif option == '2':
		obj1 = Player72()
		obj2 = Manual_player()
	elif option == '3':
		obj1 = Manual_player()
		obj2 = Manual_player()


        #########
        # deciding player1 / player2 after a coin toss
        num = random.uniform(0,1)
	interchange = 0
        if num > 0.5:
		interchange = 1
		simulate(obj2, obj1)
	else:
		simulate(obj1, obj2)
		
	
