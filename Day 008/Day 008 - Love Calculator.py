def calculate_love_score(name1,name2):
    tru=['T','R','U','E']
    luv=['L','O','V','E']
    names = list(first_name.upper()+second_name.upper())
    tru_score=0
    luv_score=0
    love_score=tru_score
    for letter in names:
        if letter in tru:
            tru_score +=1
            
    for char in names:
        if char in luv:
            luv_score +=1
    print(f"Your love score is {str(tru_score)+str(luv_score)}.")
    
first_name = input("Type in the first name: \n")
second_name = input("Type in the second name: \n")    

calculate_love_score(first_name, second_name)