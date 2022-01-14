print("Stop! Who would cross the Bridge of Death\nMust answer me these questions three, 'ere the other side he see.\n")
name = input("What is your name?\t")
if name.lower() == "arthur":
    print("My liege! You may pass!")
else:
    seek = input("What is your quest?\t")
    if "grail" not in seek:
        print("Only those who seek the Grail may pass.")
    else:
        color = input("What is your favourite color?\t")
        if color[0] == name[0]:
                print("You may pass!")
        else:
                print("Incorrect! You must now face the Gorge of Eternal Peril.")

