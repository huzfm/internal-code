string = input("Enter the String \n");
v=0
c=0
s=0
for i in string:
    if i in ('a','e','i','o','u'):
        v = v + 1;
    elif i.isspace():
        s = s + 1;
    else:
        c = c + 1;
print(v);
print(c);
print(s);