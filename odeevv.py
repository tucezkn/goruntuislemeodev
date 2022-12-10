dosya = open("data", "r")
dosya.write("Name : gökçe\nSurname : sayın\nGender : female\nUsername : Wtfgokce\Job : oyunncu")
dosya.close()
dosya = open("data", "r")
string=dosya.read()
s_string=string.split("\n")
Dictionary={ 


}
types=[0,1,2,3,4]
for i in types:
    s2_string = s_string[i].split(":")
    Dictionary[s2_string[0]]=s2_string[1]

print(Dictionary)
dosya.close()
