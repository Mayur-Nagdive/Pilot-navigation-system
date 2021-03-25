#Pilot navigation system
#you are the pilot and your plane is at the altitude of 3000ft which is safe for landing if the plane is above 3000ft and 6000ft atleast allow the pilot to try for landing
#if your plane is above 6000ft din't allow the  pilot to land the plane and ask to go around
#user will enter the altitude of the plane
#---------------------------------------------------------------------------------------------------
#Author: MAyur Nagdive
#Date:24 March 2021

#Pilot Navigation system
#Pilot Navigation system
a=int(input('Enter the altitude of the plane in fts \n'))

if a<=3000:
    
    print('your are safe to land')

    s=float(input('enter the speed of the plane in m/s \n'))
    if s<800:
      print('please increase your speed to 800m/s while landing')
    elif s==800:
      print('maintain your speed while landing')  
    else:
      print('Please lower your speed to 800 m/s')

elif 3000<=a<=6000:
    print('Be cautious but you can land at will')

    s=float(input('enter the speed of the plane in m/s \n'))
    if s<800:
      print('please increase your speed to 800m/s while landing')
    elif s==800:
      print('maintain your speed while landing')  
    else:
      print('Please lower your speed to 800 m/s')

else:
    print('please take a roundabout and lower your altitude')
