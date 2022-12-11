print("i am lonely.")
print("are you lonely?")
answer = input()
if answer == "yes":
    print("okay can we be friends?")
    answer2 = input()
    if answer2 == "yes":
        print("thanks can we play ball?")
        answer3 = input()
        if answer3 == "yes":
            print("yay! lets play ball!")
        else:
            print("then what do you what to play?")
            answer4 = input()
            print("OK let's play " + answer4)
        print("OK, we are done! \nWhat do you want to do next?")
        answer5 = input()
        print("OK let's play " + answer5)
    else:
        print("awww man i really want to be friends.")
        print("okay byeeeeee!!!!!!!")
else:
    print("awww i wish we can be friends.")
    print("i really want to be friends.")
    print("maybe we can play secretly!")
