#Quiz: Calculate
#In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

#1. How many tiles are needed?
#2. You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?
tiles_per_package = 6
packages_bought = 17
total_tiles = packages_bought * tiles_per_package
part_one = 9, 7
width, length = part_one
part_two = 5, 7
width, length = part_two
part_one_tiles = part_one[0] * part_one[1]
part_two_tiles = part_two[0] * part_two[1]
required_tiles = part_one_tiles + part_two_tiles

left_over_tiles = total_tiles - required_tiles



# Fill this in with an expression that calculates how many tiles are needed.
print("The number of tiles needed is: {}".format(required_tiles))

# Fill this in with an expression that calculates how many tiles will be left over.
print("The number of tiles needed is: {}".format(left_over_tiles))
