#-----import statements-----

import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----

#leaderboard
leaderboard_file_name = "a122_leaderboard.txt"
leader_names = []
leader_scores = []
player_name = input("Please enter your name: ")
print("Difficulty Settings = Easy, Normal, Impossible, Cheating")
difficulty = input("Difficulty Setting = ")
if difficulty == "Easy":
  bcolors = ["orange red", "crimson", "blue", "green", "yellow", "purple", "pink", "orange", "royal blue", "brown", "chartreuse", "azure", "white", "teal", "moccasin", "maroon", "violet", "gold", "cyan", "gray", "gainsboro", "silver", "indigo", "medium spring green", "dark green"]
  btcolor = "black"
  stcolor = "black"
  ctcolor = "black"
  tsize = 4.5
  timer = 31
  def t_clicked(x, y):
    global timer
    if(timer > 0):
      update_score()
      change_position()
    if(timer == 0):
      t.color("red")
      t.setheading(270)
if difficulty == "Normal":
  bcolors = ["orange red", "crimson", "blue", "green", "yellow", "purple", "pink", "orange", "royal blue", "brown", "chartreuse", "azure", "white", "teal", "moccasin", "maroon", "violet", "gold", "cyan", "gray", "gainsboro", "silver", "indigo", "medium spring green", "dark green"]
  btcolor = "black"
  stcolor = "black"
  ctcolor = "black"
  tsize = 4
  timer = 31
  def t_clicked(x, y):
    global timer
    if(timer > 0):
      decrease_size()
      update_score()
      change_position()
    if(timer == 0):
      t.color("red")
      t.setheading(270)
if difficulty == "Impossible":
  bcolors = ["black"]
  btcolor = "white"
  stcolor = "white"
  ctcolor = "white"
  tsize = 5
  timer = 46
  def t_clicked(x, y):
    global timer
    if(timer > 0):
      decrease_size()
      update_score()
      change_position()
    if(timer == 0):
      t.color("red")
      t.setheading(270)
if difficulty == "Cheating":
  bcolors = ["orange red", "crimson", "blue", "green", "yellow", "purple", "pink", "orange", "royal blue", "brown", "chartreuse", "azure", "white", "teal", "moccasin", "maroon", "violet", "gold", "cyan", "gray", "gainsboro", "silver", "indigo", "medium spring green", "dark green"]
  btcolor = "black"
  stcolor = "black"
  ctcolor = "black"
  tsize = 4
  timer = 1000000
  def t_clicked(x, y):
    global timer
    if(timer > 0):
      update_score()
    if(timer == 0):
      t.color("red")
      t.setheading(270)
if difficulty == "easy":
  bcolors = ["orange red", "crimson", "blue", "green", "yellow", "purple", "pink", "orange", "royal blue", "brown", "chartreuse", "azure", "white", "teal", "moccasin", "maroon", "violet", "gold", "cyan", "gray", "gainsboro", "silver", "indigo", "medium spring green", "dark green"]
  btcolor = "black"
  stcolor = "black"
  ctcolor = "black"
  tsize = 4.5
  timer = 31
  def t_clicked(x, y):
    global timer
    if(timer > 0):
      update_score()
      change_position()
    if(timer == 0):
      t.color("red")
      t.setheading(270)
if difficulty == "normal":
  bcolors = ["orange red", "crimson", "blue", "green", "yellow", "purple", "pink", "orange", "royal blue", "brown", "chartreuse", "azure", "white", "teal", "moccasin", "maroon", "violet", "gold", "cyan", "gray", "gainsboro", "silver", "indigo", "medium spring green", "dark green"]
  btcolor = "black"
  stcolor = "black"
  ctcolor = "black"
  tsize = 4
  timer = 31
  def t_clicked(x, y):
    global timer
    if(timer > 0):
      decrease_size()
      update_score()
      change_position()
    if(timer == 0):
      t.color("red")
      t.setheading(270)
if difficulty == "impossible":
  bcolors = ["black"]
  btcolor = "white"
  stcolor = "white"
  ctcolor = "white"
  tsize = 5
  timer = 46
  def t_clicked(x, y):
    global timer
    if(timer > 0):
      decrease_size()
      update_score()
      change_position()
    if(timer == 0):
      t.color("red")
      t.setheading(270)
if difficulty == "cheating":
  bcolors = ["orange red", "crimson", "blue", "green", "yellow", "purple", "pink", "orange", "royal blue", "brown", "chartreuse", "azure", "white", "teal", "moccasin", "maroon", "violet", "gold", "cyan", "gray", "gainsboro", "silver", "indigo", "medium spring green", "dark green"]
  btcolor = "black"
  stcolor = "black"
  ctcolor = "black"
  tsize = 4
  timer = 1000000
  def t_clicked(x, y):
    global timer
    if(timer > 0):
      update_score()
    if(timer == 0):
      t.color("red")
      t.setheading(270)
player_score = 0
font_setup = ("Arial", 40, "normal")
counter_interval = 1000
timer_up = False
bcolor = rand.choice(bcolors)

#-----initialize turtle-----

background_t = trtl.Turtle()
background_t.ht()
background_t.speed(0)
background_t.color(bcolor)
background_t.pensize(10000)
background_t.circle(1)

t = trtl.Turtle()
t.penup()
t.speed(0)
t.shape("turtle")
t.shapesize(tsize)
t.setheading(90)

box_t = trtl.Turtle()
box_t.pensize(2)
box_t.ht()
box_t.pencolor(btcolor)
box_t.speed(0)
box_t.penup()
box_t.setheading(270)
box_t.goto(360, 400)
box_t.pendown()
box_t.forward(110)
box_t.left(90)
box_t.forward(150)

score_t = trtl.Turtle()
score_t.ht()
score_t.pencolor(stcolor)
score_t.speed(0)
score_t.penup()
score_t.goto(390, 320)
score_t.pendown()

counter_t = trtl.Turtle()
counter_t.ht()
counter_t.pencolor(ctcolor)
counter_t.speed(0)
counter_t.penup()
counter_t.goto(230, -370)

#-----game functions--------

def update_score():
  global player_score
  player_score += 1
  score_t.clear()
  score_t.write(player_score, font=font_setup)
def decrease_size():
  global tsize
  if(tsize > 1):
    tsize -= 0.075
    t.shapesize(tsize)
def change_position():
  new_xpos = rand.randint(-400,  400)
  new_ypos = rand.randint(-300, 300)
  t.goto(new_xpos, new_ypos)
def countdown():
  global timer, timer_up
  counter_t.clear()
  if timer  <= 6 and timer > 0:
    if timer % 2 == 0:
      counter_t.pencolor("red")
    if timer % 2 == 1:
      counter_t.pencolor("black")
  if timer == 1:
    timer_up == True
    timer -= 1
    counter_t.write("Time's Up", font=font_setup)
    manage_leaderboard()
  if timer > 1:
    counter_t.write("Time: " + str(timer - 1), font=font_setup)
    timer -= 1
    counter_t.getscreen().ontimer(countdown, counter_interval)

#-----events----------------

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores
  global leader_names
  global player_score
  global t

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names, leader_scores)

  # TODO
  if (len(leader_scores) < 5 or player_score > leader_scores[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names, leader_scores, player_name, player_score)
    lb.draw_leaderboard(leader_names, leader_scores, True, t, player_score)
  else:
    lb.draw_leaderboard(leader_names, leader_scores, False, t, player_score)
t.onclick(t_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
