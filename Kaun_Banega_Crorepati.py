q_l = ["tomato is a vegetable or fruit?",
      "what is the capital of India?",
      "NG me kon sa course karaya jata hai?",
      "when did COVID come to India?"]  #taking a list of questions

o_l = [["red color", "fruit", "vegetable", "flower"],
      ["patna", "bhopal", "delhi", "itanagar"],
      ["software engineering", "counseling", "tourism", "agriculture"],
      [2021, 2018, 2020, 2019]]

s_l = [2, 3, 1, 4]

o_50_50 = [["fruit", "vegetable"],
           ["patna", "delhi"],
           ["software engineering", "agriculture"],
           [2020, 2019]]

s_50_50_l = [1, 2, 1, 2]

print("WELCOME TO THE KBC CONTEST")
c = 0
i = 0

while i < len(q_l):
    print("Aapka Sawal Hai:")
    print(q_l[i])
    print("Aapke Options Hai:")
    j = 0
    while j <= 3:
        print(str(j + 1) + ".", o_l[i][j])
        j += 1

    a = input("Do you want to use the 50-50 lifeline? (yes or no):")
    if a.lower() == "yes":
        c += 1
        if c == 1:
            k = 0
            while k < 2:
                print(str(k + 1) + ".", o_50_50[i][k])
                k += 1
            answer = int(input("Enter your answer (1 or 2): "))
            if answer == s_50_50_l[i]:
                print("Congratulations! Aapka Jawab Sahi Hai")
                i += 1
            else:
                print("Aapka Jawab Galat Hai. Aapka game yahi par samapt hota hai.")
                break
        else:
            print("Aap 50-50 lifeline ka istemal kar chuke hain")
            answer = int(input("Enter your answer (1, 2, 3, or 4): "))
            if answer == s_l[i]:
                print("Congratulations! Aapka Jawab Sahi Hai")
                i += 1
            else:
                print("Aapka Jawab Galat Hai. Aapka game yahi par samapt hota hai.")
                break
    elif a.lower() == "no":
        answer = int(input("Enter your answer (1, 2, 3, or 4): "))
        if answer == s_l[i]:
            print("Congratulations! Aapka Jawab Sahi Hai")
            i += 1
        else:
            print("Aapka Jawab Galat Hai. Aapka game yahi par samapt hota hai.")
            break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

if i == len(q_l):
    print("Congratulations! You have successfully completed the KBC contest.")

