calls=0
def count_calls (calls):
    return calls
def string_info (string):
    global calls
    calls=calls+1
    info=string
    count=len(info)
    count1=(info.upper())
    count2=info.lower()
    kort=count,count1,count2
    return kort


def is_contane (string,list):
    global calls
    calls=calls+1
    list_1=list; b=bool
    wr=string.upper()
    for i in range(len(list_1)):
        list_1[i]=list_1[i].upper()
        b1=0
    for i in  range(len(list_1)):
        if wr==list_1[i]:
            b1 = 1
    if bool(b1==1):
     print(bool(b1 == 1))
     print(bool(b1!=1))
    return b1



print(string_info("Capybara"))
print(string_info("Armageddon"))
print(is_contane("Urban",['ban','BaNaN','urBAN']))
print(is_contane('cycle',['recycling','cycling']))
print(calls)