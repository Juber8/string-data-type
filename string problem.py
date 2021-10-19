#add ing at end of string if ing alredy present add ly insted of ing if len string less than 3
#then unchaanged the string

'''
string = input('enter the string:')
if string.endswith('ing'):
    string+= 'ly'
elif len(string)>=3:
    string+= 'ing'
print(string)

def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'
  return str1
j=add_string('abc')
print(j)

#revese the string by using revesed function
s='juber'
r=reversed(s)
output=''.join(r)
print(output)

#reverse the string by using while loop:
s=input('enter the string:')
output=''
i=len(s)-1
while i>=0:
    output=output+s[i]
    i=i-1
print(output)

#write a program to revrse order of word of sting
s=input('enter string to be revrsed:')
l=s.split()
l1=l[::-1]
print(' '.join(l1))

#write a program to reverse internal content each word of string
s='juber nasaruddin mulla'
l=s.split()
l1=[]
for i in l:
    l1.append(i[::-1])
print(' '.join(l1))

s='one two three four five six'
l=s.split()
l1=[]
i=0
while i<len(l):
    if i%2 == 0:
        l1.append(l[i])
    else:
        l1.append((l[i][::-1]))
    i=i+1
print(' '.join(l1))

#write a program and fetch element at present at even and odd index
#by using while loop
s='jubermulla'
i=1
while i<len(s):
    print(s[i],end='')
    i=i+2
#by using slicing
s='jubermulla'
print('character present at even index:',s[::2])
print('character present at odd index:',s[1::2])


s='a4b3c2'
alphabetes=[]
digits=[]
for i in s:
    if i.isalpha():
        alphabetes.append(s)
    else:
        digits.append(s)
print(digits)
'''
