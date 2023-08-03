from .Data import game_table

game_name = "Manual_%s_%s" % (game_table["game"], game_table["player"])
filler_item_name = game_table["filler_item_name"] if "filler_item_name" in game_table else "Filler"
starting_items = game_table["starting_items"] if "starting_items" in game_table else None

# Programmatically generate starting indexes for items and locations based upon the game name and player name to aim for non-colliding indexes
# Additionally, make this use as many characters of the game name as possible to avoid accidental id pool collisions
# - It's assumed that the first two characters of a game and the last character *should* be fairly unique, but we use the remaining characters anyways to move the pool
# - The player name is meant to be a small differentiator, so we just apply a flat multiplier for that

# 100m + 70m + 10m, which should put all Manual games comfortably in the billions
starting_index = 867539000