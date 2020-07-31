#Note that this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
print('Amount of rainfall: {}'.format(rainfall))

# decrease the rainfall variable by 10% to account for runoff
rainfall -= rainfall * (10 / 100)
print('Amount of rainfall decreased by 10%: {}'.format(rainfall))


# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
print('Reservoir volume added to rainfall: {}'.format(reservoir_volume))


# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm
reservoir_volume += reservoir_volume * (5 / 100)
print('Reservoir volume increased by 5%: {}'.format(reservoir_volume))


# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume -= reservoir_volume * (5 / 100)
print('Reservoir volume decreased by 5%: {}'.format(reservoir_volume))


# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.
reservoir_volume -= (2.5e5)

# print the new value of the reservoir_volume variable
print('Reservoir Volume: {}'.format(reservoir_volume))
