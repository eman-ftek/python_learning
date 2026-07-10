def total_distance(one,two):
    total=one+two
    return(total)
while True:
    on=int(input("Distant of first journy :"))
    tw=int(input("Dstant of secound joruny :"))
    if on ==0 :
        print("Go out")
        break
    else: 
        print(total_distance(on,tw))