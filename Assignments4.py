name=input("Enter a name:")
namekhanevadegi=input("Enter a namekhanevadegi:")

nomre1=int(input("Enter a number1 :"))
nomre2=int(input("Enter a number2 :"))
nomre3=int(input("Enter a number3 :"))

if nomre1>20 or nomre2>20 or nomre3>20:
    print("adad 0 ta 20 vared kon")
elif nomre1<0 or nomre2<0 or nomre3<0 :
    print("adad 0 ta 20 vared kon")
else:
    Average=(nomre1+nomre2+nomre3)/3
    print(Average)

    if Average>17:
        print("great")
    elif Average<17 and Average>=12 :
        print("normal")
    elif Average<12:
        print("fail")