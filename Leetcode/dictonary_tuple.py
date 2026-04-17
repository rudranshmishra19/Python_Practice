t=(1,'a',[3,5])  #Tuple
try:

   dt={t:'1'} #Attempt to use tuple as dict key
   print("Dictonary created sucessfully :",dt)
except TypeError as e:
   print("Error",e)
   print("Cannot use this tuple as a dictonary key because it contains mutable elements.")
   