from pprint import pprint
import zach_stats as zs

pprint(zs.__dict__)

#direct printing method
print('height is', zs.height)
# printing method using dunder __dict__
print('Height is also', zs.__dict__['height'])
print(zs.dog_stats)

# attempt to change value of zs.height
embellished_height = zs.__dict__['height'] = 6969

print(embellished_height)

