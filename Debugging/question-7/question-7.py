
day = raw_input("Aaj ka din kya hai? (monday/tuesday) > ")
time = raw_input("Kaunse samay ka khana banana hai? (lunch/dinner) > ")
if day == "monday" or day == "tuesday":
    print "Daal-Roti banegi aaj"
if day == "tuesday" and time == "dinner":
    print "Pav-Bhaji banegi aaj toh :)"