import copy

def build_house():
  print("Please enter the house file: ")
  house_file = input()
  housefp = open(house_file, "r")
  myhouse = [] 
  line = housefp.readline()
  while line:
    myhouse.append(list(line))
    line = housefp.readline()
  return myhouse

def main():
  house = build_house();
  startrow = 1 #   Set startrow to be indices of an empty space in the house
  startcol = 4 #   Set startcol to be indices of an empty space in the house
  num_treasures = 2 #   Set num_treasures to the number of t’s in the house
  tcount = 0  # how many treasures found so far
  unlocked = [False, False, False, False, False]
  num = num_treasures
  
  while(tcount < num_treasures):
    print_house(house, startrow, startcol) #display the house and an "@" showing where the player is. This function is given below.
    print("User can go (north, easth, south , west) unless there is a wall")
    command = input("Where do you want to go? ")
    north = 'w' 
    easth = 'd'
    south = 's'
    west = 'a'
    if (command == south):
      trow = startrow+1 
      tcol = startcol
    elif (command == easth ):
      trow = startrow
      tcol = startcol+1
    elif (command == north): 
      trow = startrow-1 
      tcol = startcol
    elif (command == west): 
      trow = startrow 
      tcol = startcol-1
    elif (command == 'q'): 
      break
    if (house[trow][tcol] == '*'):
      print("The user that they cannot go that way")
      continue
    if (get_treasure(house, trow, tcol)):
          
      house[trow][tcol] == ' ' #replace the “t” at index trow and tcol with a space if a treasure was found there
      tcount += 1
      num -= 1
    
      print("You found the treasure. There are", num, "left") 

    if is_door(house,trow,tcol):
      if(not can_unlock(house, unlocked, trow, tcol)):
        print("You can't move there")
        trow = startrow
        tcol = startcol
    elif get_key(house,unlocked,trow,tcol):
      print("You found a key!")
    if(tcount == num_treasures):
      print("Aye you won the game!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    startcol = tcol
    startrow = trow
    
#prints the house/map
def print_house(h,sr,sc):
  th = copy.deepcopy(h)
  th[sr][sc] = "@"
  for i in th:
    print(''.join(str(x) for x in i), end='')
#if index is at t(treasue) then it returns true    
def get_treasure(house, trow, tcol):
  if(house[trow][tcol] == 't'):
    house[trow][tcol] = ' '
    return True
  else:
    return False    
  
#function that checks for doors
def is_door(house, trow,tcol):
  if house[trow][tcol] == '5' or house[trow][tcol] == '6' or house[trow][tcol] == '7' or house[trow][tcol] == '8' or house[trow][tcol] == '9':
    return True
  else:
      return False
  
#function that checks if the door can be unlocked
def can_unlock(house,unlocked,trow,tcol):
  tmp = int ((house[trow][tcol])) - 5
  return unlocked[tmp]

def get_key(house, unlocked, trow, tcol):
  if house[trow][tcol] == '0' or house[trow][tcol] == '1' or house[trow][tcol] == '2' or house[trow][tcol] == '3' or house[trow][tcol] == '4':
    tmp = int(house[trow][tcol])
    unlocked[tmp] = True
    house[trow][tcol] = ' '
    return True
  else:
    return False


main()