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
    
def check_stats():
    tool = tools[game["tool"]]
    print (f"You currently have {game['money']} and are using a {tool['name']}")
    
def upgrade():
    next_tool = tools[game["tool"] + 1]
    if (next_tool == None):
        print("There is no more tools")
        return 0
    if (game["money"] < next_tool["cost"]):
        print("not enough to buy the tool")
        return 0
    game["money"] -= next_tool["cost"]
    game["tool"] += 1
    
def win_check(){
    
}