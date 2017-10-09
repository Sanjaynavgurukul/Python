speed = int( raw_input("Gaadi ki speed daalo > ") )

# Ab aapne speed check kar ke kuch print karna hai:
# Agar 60 se kam hai toh print karna: "Speed kam hai"
# Agar 30 se kam hai toh print karna: "Speed bahot kam hai"
# Agar 100 se zyada hai toh print karo: "Bahot zyada hai"
if speed < 30:
    print "Speed bahot kam hai"
elif speed < 60:
    print "kam hai"
elif speed > 100:
    print "Speed bahot fast hai"