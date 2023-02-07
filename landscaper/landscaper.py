## Landscaper

## Game State

game = {"tool": 0, "money": 0}

tools = [
    {"name": "Teeth", "profit": 1, "cost": 0},
    {"name": "Pair of Rusty Scissors", "profit": 5, "cost": 5},
    {"name": "Old-Timey Pushy Lawnmower", "profit": 50, "cost": 25},  
    {"name": "Fancy Battery Powered Lawnmower", "profit": 100, "cost": 250},
    {"name": "Team of Starving Student", "profit": 250, "cost": 500}  
]

## Game Option Functions

def cutGrass():
    tool = tools[game["tool"]]
    print(f'You cut the grass with you {tool["name"]} and make ${tool["profit"]}')
    game["money"] += tool["profit"]   
    
def check_Stats():
    tool = tools[game["tool"]]
    print (f"You currently have {game['money']} and are using a {tool['name']}")
    
def upgrade():
    if (game['tool'] >= len(tools) - 1):
        print("There are no more upgrades remaining")
        return 0
    next_tool = tools[game["tool"] + 1]
    if (next_tool == None):
        print("There is no more tools")
        return 0
    if (game["money"] < next_tool["cost"]):
        print("not enough to buy the tool")
        return 0
    print("You are upgrading your tool")
    game["money"] -= next_tool["cost"]
    game["tool"] += 1
    
def win_check():
    if(game["tool"] == 4 and game["money"] >= 1000):
        print("You win")
        return True
    return False

while (True): 
    
    i = input("[1] Cut Grass [2] Check Stats [3] Upgrade [4] Quit Game")
    i = int(i)
    
    if (i == 1):
        cutGrass()
    if (i == 2):
        check_Stats()
    if (i == 3):
        upgrade()
    if (i == 4):
        print("You quit the game")
        break
    if (win_check()):
        break