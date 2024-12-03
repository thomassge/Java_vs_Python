#Thema global und nonlocal
##################################################
##################Klausuraufgabe##################
##################################################

def global_test():
    global v0
    v1 = "v1 ist eine lokale Variable"
    print(v1)
    v0 = "v0 ist eine globale Variable wird in global_test verwendet."

    def local_test():
        nonlocal v1
        v2 = "v2 ist eine lokale Variable in local_test"
        print(v2)
        v1 = "v1 ist eine lokale Variable"
        print(v1)

    local_test()
    print(v1)

v0 = "v0 ist eine globale Variable"
print(v0)

global_test()
print(v0)
