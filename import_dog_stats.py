from pprint import pprint
import zach_stats as zs

pprint(zs.__dict__)

#direct printing method
print('height is', zs.height)
# printing method using dunder __dict__
print('Height is also', zs.__dict__['height'])
print(zs.dog_stats)
