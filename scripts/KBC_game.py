Q1 = ["What is the capital of INDIA?", ["A.Pune", "B.Delhi", "C.Kerala", "D.Andhra"],"B"]
Q2 = ["Who is the PM of India?",[ "A.Modi", "B.Pawar", "C.Yogi", "D.Gandhi"], "A"]
Q3 = ["What is the Capital of Maharashtra?",[ "A.Pune", "B.Delhi", "C.Mumbai", "D.Andhra"],"C"]
Q4 = ["Who is the CM of Maharashtra?", ["A.Modi", "B.Shinde", "C.Yogi", "D.Gandhi"],"B"]
Q5 = ["What is the Financial Capital of India?", ["A.Pune", "B.Andhra", "C.Kerala", "D.Mumbai"], "D"]
level = [0, 1000, 5000, 10000, 15000]
cnt = 0
Questions = [Q1, Q2, Q3, Q4, Q5]
user_name = input("Please enter your name:")

for i in Questions:
    print(i[0])
    print(i[1])
    ans = input("Enter your Choice(A/B/C/D):")
    if ans == i[2]:
        print(f"Yay, {user_name} Your answer is correct!!!")
        cnt += 1
        print(f"You have passed the level and won {level[cnt]}$ ")

        print("--------------------------------------")
        choice = input("Do you want to continue(y/n):")
        if choice == 'y':
            continue
        else:
            print(f'Excellent {user_name}, You won the {level[cnt]}$')
            break
    else:
        print(f"Hey {user_name} you lost the game, Better luck next time")
        break
