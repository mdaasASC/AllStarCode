from winsound import *
from random import *

wives = ["Kanye", "Kanye", "Kanye"]

music = ["Kanye"]

job = ["Kanye"]

food = ["Kanye"]

x = raw_input("Wife: ")

y = raw_input("Music genre: ")

z = raw_input("Job: ")

i = raw_input("Food: ")

print("Your wife is " + choice(wives) + "\nYour favorite music is " + choice(music) + "\nYour job is " + choice(job) + "\nYour only food is " + choice(food)) 
PlaySound("ILoveKanye.mp3")