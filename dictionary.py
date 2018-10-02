plant={}  
plant[1]='Ravi'  
plant[2]='Manoj'  
plant['name']='Hari'  
plant[4]='Om'  
print (plant[2])
print (plant['name'])
print (plant[1])  
print (plant)
print ("first  element is :" , plant[1])
print ("first  element is :" , plant['name'])
plant['location']='Jaipur'
print (plant)
print(len(plant))
print (str(plant))
print ( plant.keys() )
print ( plant.items() )
data2={103:'Sanjay'}
plant.update(data2)
print (plant)
print (data2)
data2.clear()
print (data2)
sequence=('Id' , 'Number' , 'Email')  
data={}  
data1={}  
data=data.fromkeys( sequence )  
print (data)
data1=data1.fromkeys(sequence,100)  
print (data1 )


data3={'Id':100 , 'Name':'Aakash' , 'Age':23}  
data4=data3.copy()

print (data4)  

data5={'Id':100 , 'Name':'Aakash' , 'Age':23}  
print ('Age' in data5)
print ('Email' in data5)




data6={'Id':100 , 'Name':'Aakash' , 'Age':23}  
print (data6.get('Age'))  
print (data6.get('Email'))

