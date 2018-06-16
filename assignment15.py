#1
emails = ["zuck26@facebook.com","page33@google.com","jeff42@amazon.com"]
for i in range (0,len(emails)):
    string1=emails[i]
    str1=string1.replace("@"," ")
    str2=str1.replace("."," ")
    #print(str2)
    emails[i]=str2
    str3=emails[i]
    emails[i]=str3.split(" ")
for i in range (0,len(emails)):
    print(emails[i])
    
#2
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
print(re.findall(r'[bB][a-zA-Z]+',text))

#3
sentence = "A, very very; irregular_sentence"
regex = r'[^a-zA-Z][ ]*'
sent=re.sub(regex," ",sentence)
print(sent)