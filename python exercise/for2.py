lost_socks = "sofa"
location = ["bed", "closet", "chair", " sofa" ,"shoes"]
for socks in location:
    if socks == lost_socks:
        print("Lost Socks is found in", socks)
        break
    else:
        print("Lost socks is not found in", socks)