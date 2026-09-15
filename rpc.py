
import random

Rock="x"
Scissors="y"
Paper="z"

Choices=[Rock,Paper,Scissors]

Player1Choice=(random.choice(Choices))
Player2Choice=(random.choice(Choices))


print(Player1Choice)
print(Player2Choice)

if (Player1Choice == Player2Choice):print(WIN)


Win=(Rock == Scissors),(Scissors == Paper),(Paper == Rock)

WIN=["YOU WIN"]
LOSE=["YOU LOSE"]

if Win:=True:print(WIN)
if Win:=False:print(LOSE)