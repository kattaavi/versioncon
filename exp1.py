emp ={
    'Avinash':100000,
    'Rakesh':30000,
    'Ramesh':20000,
    'Suresh':50000,
    'Mallesh':40000
}
print(sum(emp.values()))

print("Minimum salary is :",min(emp.values()))
print("Maximum salary is :",max(emp.values()))

name=''
sal=0
for n,val in emp.items():
    if val > sal:
        sal = val
        name = n
print('Highest salary is drawn by',name)

print("hello world")


