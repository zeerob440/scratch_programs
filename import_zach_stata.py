# This program serves as the destination for zach_stats.py
# since this is a demo, the import command is on line 3 but typically imports are on line 1.
import zach_stats as zs
# import vars from other files with dot notation such that (file.nameOfVarInFile)
moved_name = (zs.name)
moved_height = (zs.height)

combined: str = f' {moved_name} is {moved_height} inches tall!'

print(combined)
 

