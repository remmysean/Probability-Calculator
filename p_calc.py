import copy
import random


class Hat:
  def __init__(self,**group):
    self.contents=[]
    for key,value in group.items():
        for itr in range(value):
          self.contents.append(key)
  
  #  get random n number of hats from contents
def draw(self, amount):
    if amount > len(self.contents):
      return self.contents
    draw_list = []
    for _ in range(amount):
      choice = random.randrange(len(self.contents))
       draw_list.append(self.contents.pop(choice))
    return  draw_list


  
  #  probability
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    final_count=0
    for _ in range(num_experiments):
      copyhat = copy.deepcopy(hat)
      temp_list = copyhat.draw(num_balls_drawn)
      success = True
      for key,value in expected_balls.items():
        if temp_list.count(key) < value:
          success = False
          break
      if success:
        final_count+=1
    return final_count/num_experiments
