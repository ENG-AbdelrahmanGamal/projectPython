

weight =int(input("Weight : " ))

kind=input("(L) bs or (K)g: ")
if(kind== 'k' or kind=='K'):
    print(f"You are '  {weight*0.45} 'Kilos")
elif(kind=='l' or kind=="L"):
    print(f"You are '  {weight/0.45}  'pounds.")
