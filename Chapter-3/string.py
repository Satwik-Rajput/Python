Name = "Satwik"

print(Name[0:3])  #[0:3] mean 0,1,2 onle and the last one is excluded;3 is not included.

print(Name[-6:-3]) #negative sliceing

print(len(Name)) # Here (len-length) itnis used to determine the length of string.

print(Name[:5]) #[:5] mean [0:5]

print(Name[:5:2]) #[:5:2] mean [0:5:2]

print(Name.endswith("wik"))

print(Name.startswith("Sat"))

print(Name.center(12, '*'))

print(Name.count("a"))

print(Name.find("w"))

print(Name.upper())