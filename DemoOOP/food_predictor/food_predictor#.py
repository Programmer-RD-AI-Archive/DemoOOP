import pickle
import math
import random
from math import remainder

'''
Comments:Vibhatha
Variables in python
Food Center => class Food_Center, food_center = 
'''
# TODO: Variable names in simple case
# Do the TODO list
user_name: str["Ranuga"]
passwor = "Devin"
user__name = input(" > Enter the User Name... \n > ")
password = input(" > Enter the Password... \n > ")
while not (user_name != user__name or not (password != passwor)):
    user_name = input(" > Enter the User Name... \n > ")
    password = input(" > Enter the Password... \n > ")

print(" < | > Welcome < | > ")
first_name = input(" > Enter your first Name please... \n > ")
second_name = input(f" > {first_name} please enter your Second Name please... \n > ")
age = int(input(f" > How old are you {first_name} ? \n > "))

if age > 18:
    pass

elif age < 18:
    quit()

else:
    pass
Full_Name = first_name + second_name


def add():
    what_is_the_measuring_unit: str = input(" > What is the measuring Unit ? (Kg or g or Pounds) \n > ")
    name: str = input(" > Enter the Name of the food.... \n > ")
    how_much = int(input(" > Enter how much do you use it per day ? \n > "))
    ho_much = int(input(" > How Much did you buy in totall ? \n > "))
    how_many_das = int(
        input(f" > {first_name} How many days are you thinking of using the {ho_much} {what_is_the_measuring_unit} ? \n > "))
    m = how_much / ho_much
    x = how_many_das / ho_much
    v = remainder(how_much, ho_much)
    z = remainder(how_many_das, ho_much)
    per_week_the_Amount = how_much * 7
    per_month_the_Amount = per_week_the_Amount * 4
    per_year_the_Amount = per_month_the_Amount * 12
    ap = open("per_day.txt", "a")
    ap.write(f" \n > Per Day : {how_much} ")
    ap.close()
    rafaa = open("per_week.txt", "a")
    rafaa.write(f" \n > Per week : {per_week_the_Amount} ")
    rafaa.close()
    rafaatedud = open("per_month.txt", "a")
    rafaatedud.write(f" \n > Per Month : {per_month_the_Amount} ")
    rafaatedud.close()
    fygedgsjth = open("per_year.txt", "a")
    fygedgsjth.write(f" \n > Per year : {per_year_the_Amount} ")
    fygedgsjth.close()
    print(f" \n > You use {name} per day : {m}")
    print(f" \n > Remainder if you eat {how_much} per Day the remainder is : {v}")
    print(f" \n > If you want to use {how_many_das} you should eat : {what_is_the_measuring_unit}")
    print(f" \n > if you want to use {ho_much} for {how_many_das} the remainder is : {z}")
    forhow = input(f" > For how many day did you buy the above {name} ? (Day or Week or month) \n > ")

    if forhow == "Week" or "week":
        how_many_days = m * 4 * 12
        how_mont = m * 4
        how_d = m / 7
        kk = open("Per_dfg.txt", "a")
        kk.write(f" \n > Per Day : {how_d} ")
        kk.write(f" \n > Per Month : {how_mont}")
        kk.write(f" \n > Per Year : {how_many_days} ")
        kk.close()
        addd = open("per_day.txt", "a")
        addd.write(f" \n > Per Day : {how_d} ")
        addd.close()
        print(f" > This is How much it will take you per a year : {how_many_days} {what_is_the_measuring_unit} ")
        print(f" > This is how much {name} that you need per Month : {how_mont} {what_is_the_measuring_unit} ")
        print(f" > This is how much you need per day : {how_d}")
        print(
            "> An averahe person should eat : 18.82408 kilo gram | 18824.08 gram | 41.499992603 Pounds {What_is_it} "
            "per Day")
        print(f" > Per Year : {how_many_days}")
        print(f" > Per Month : {how_mont}")
        print(f" > Per Day : {how_d}")
        ap = open("per_day.txt", "a")
        ap.write(f" \n > Per Day : {how_d} ")
        ap.close()
        rafaatedud = open("per_month.txt", "a")
        rafaatedud.write(f" \n > Per Month : {how_mont} ")
        rafaatedud.close()
        fygedgsjth = open("per_year.txt", "a")
        fygedgsjth.write(f" \n > Per year : {how_many_days} ")
        fygedgsjth.close()

    elif forhow == "Day" or "day":
        ff = m * 7
        fg = ff * 4
        fh = fg * 12
        fs = open("Per__wefg.txt", "a")
        fs.write(f" \n > Per Week : {ff} ")
        fs.write(f" \n > Per Month : {fg}")
        fs.write(f" \n > Per Year : {fh} ")
        fs.close()
        print(f" > This is How much it will take you per a year : {fh} {what_is_the_measuring_unit} ")
        print(f" > This is how much {name} that you need per Month : {how_mont} {what_is_the_measuring_unit} ")
        print(f" > This is how much you need per Week : {ff}")
        print(
            "> An averahe person should eat : 18.82408 kilo gram | 18824.08 gram | 41.499992603 Pounds {What_is_it} "
            "per Day")
        print(f" > Per Year : {fh}")
        print(f" > Per Month : {fg}")
        print(f" > Per Week : {ff}")
        rafaa = open("per_week.txt", "a")
        rafaa.write(f" \n > Per week : {ff} ")
        rafaa.close()
        rafaatedud = open("per_month.txt", "a")
        rafaatedud.write(f" \n > Per Month : {fg} ")
        rafaatedud.close()
        fygedgsjth = open("per_year.txt", "a")
        fygedgsjth.write(f" \n > Per year : {fh} ")
        fygedgsjth.close()

    elif forhow == "Month" or "month":
        dfg = m / 4
        hi = dfg / 7
        how_many_day = m * 12
        z = open("Per__weethtk.txt", "a")
        z.write(f" \n > Per Day : {dfg} ")
        z.write(f" \n > Per Week : {hi}")
        z.write(f" \n > Per Year : {how_many_day} ")
        z.close()
        print(f" > This how much you will need per year : {how_many_day} {what_is_the_measuring_unit}")
        print(f" > This is how much you need per week : {dfg} {what_is_the_measuring_unit}")
        print(f" > This is how much you need per Day : {hi} {what_is_the_measuring_unit}")
        print(" > An average person should eat : | 75450 g | 75.45 kg | 166.33878 pounds | per month")
        print(f" > Per Year : {how_many_day}")
        print(f" > Per Week : {hi}")
        print(f" > Per Day : {dfg}")
        app = open("per_day.txt", "a")
        app.write(f" \n > Per Day : {dfg} ")
        app.close()
        tedlfdud = open("per_week.txt", "a")
        tedlfdud.write(f" \n > Per week : {hi} ")
        tedlfdud.close()
        fygeidfeif = open("per_year.txt", "a")
        fygeidfeif.write(f" \n > Per year : {how_many_day} ")
        fygeidfeif.close()
    elif forhow == "Year" or "year" :
        iii = #where i ended

    else:
        print(" > An error occurred")
        print(" > Please try again later")

    if how_much < 18.232 or 40.19467964 or 18232:
        print(" > I think you should Eat a little bit more")

    elif how_much > 75.458870685916664911 or 75458.870685916670482 or 166.35833333333332007:
        pass

    else:
        print(" > An error occured")
        print(" > Try again later")
    main_menu()


def pr():
    one_or_more = input(" > Do you only Want to enter one product or many ? \n > ")
    if one_or_more == "Many" or "many":
        times = int(input(" > How many iteams do you ant to add ? \n > "))
        for i in range(0, times):
            name_of_the_product = input(" > What is the Name of the product ? \n > ")
            how_much_are_ther : int = input(f" > How many packs are there of {name_of_the_product}")
            ii = input(" > What is the mass weight unit ? (Kg) or (g) or (Pounds)\n > ")
            o = input(" > For what can you enter the price ? (Per day or per week or Per month).. \n > ")
            money_type = input("What is the money Type ? ($ or Rs) \n > ")

            if o == "per day" or "Per Day" or "per Day" or "Per day":
                pric = int(input(f" > Enter the price per one {ii} of {name_Of_The_product} per day..\n > "))
                per_week = pric * 7
                per_month = per_week * 4
                per_yyear = per_month * 12
                r = open("Per__week.txt", "a")
                r.write(f" \n > Per Week : {money_type}{per_week} ")
                r.write(f" \n > Per Month : {money_type}{per_month}")
                r.write(f" \n > Per Year : {money_type}{per_yyear} ")
                r.close()
                ad = open("per_day.txt", "a")
                ad.write(f" \n > Per Day : {pric} ")
                ad.close()
                raf = open("per_week.txt", "a")
                raf.write(f" \n > Per week : {per_week} ")
                raf.close()
                rafaatedeeeee = open("per_month.txt", "a")
                rafaatedeeeee.write(f" \n > Per Month : {per_month} ")
                rafaatedeeeee.close()
                fygedgs = open("per_year.txt", "a")
                fygedgs.write(f" \n > Per year : {per_yyear} ")
                fygedgs.close()
                print(f" > Per Week : {money_type}{per_week}")
                print(f" > Per Month : {money_type}{per_month}")
                print(f" > Per year : {money_type}{per_yyear}")

            elif o == "Month" or "month":
                price = int(input(f" > Enter the price per one {ii} of {name_of_the_product} per Month..\n > "))
                per_week = price / 4
                per_____da = per_week / 7
                per_year = price * 12
                Ra = open("Per__wee.txt", "a")
                Ra.write(f" \n > Per Day : {per_____da} ")
                Ra.write(f" \n > Per Week : {per_week}")
                Ra.write(f" \n > Per Year : {per_year} ")
                Ra.close()
                adf = open("per_day.txt", "a")
                adf.write(f" \n > Per Day : {per_____da} ")
                audflose()
                rafa = open("per_week.txt", "a")
                rafa.write(f" \n > Per week : {per_week} ")
                rafa.close()
                rafaated = open("per_month.txt", "a")
                rafaated.write(f" \n > Per Month : {price} ")
                rafaated.close()
                fygedgsj = open("per_year.txt", "a")
                fygedgsj.write(f" \n > Per year : {per_year} ")
                fygedgsj.close()
                print(f" > Per Day  : {money_type}{per_____Da}")
                print(f" > Per Week : {money_type}{per_week}")
                print(f" > Per year : {money_type}{per_year}")

            elif o == "Per week" or "Week" or "week" "per week":
                per__wee = int(input(f" > Enter the price of {name_of_the_product} per week... \n > "))
                per__da = per__wee / 7
                per__monh = per__wee * 4
                per__yea = per__monh * 12
                ran = open("Per__week.txt", "a")
                ran.write(f" \n > Per Day : {money_type}{per__da} ")
                ran.write(f" \n > Per Month : {money_type}{per__monh}")
                ran.write(f" \n > Per Year : {money_type}{per__yea} ")
                ran.close()
                a = open("per_day.txt", "a")
                a.write(f" \n > Per Day : {per__da} ")
                a.close()
                rafaa = open("per_week.txt", "a")
                rafaa.write(f" \n > Per week : {per__wee} ")
                rafaa.close()
                rafaatedu = open("per_month.txt", "a")
                rafaatedu.write(f" \n > Per Month : {per__monh} ")
                rafaatedu.close()
                fygedgsjt = open("per_year.txt", "a")
                fygedgsjt.write(f" \n > Per year : {per__yea} ")
                fygedgsjt.close()
                print(f" > Per Day : {money_mype}{per__Da}")
                print(f" > Per Month : {money_type}{per__monh}")
                print(f" > Per year : {money_type}{per__yea}")

            else:
                print(" > An error occured")
                print(" > Please try again later")

    elif one_or_more == "One" or "1" or "one":
        X = input(" > What is the mass weight unit ? (Kg) or (g) or (Pounds)\n > ")
        P = input(" > For what can you enter the price ? (Per day or Per Week or Per month).. \n > ")
        if P == "per day" or "Per Day" or "per Day" or "Per day" or "Day" or "day":
            price = int(input(f" > Enter the price per one {X} of {name_Of_The_product} per day..\n > "))
            per____week = price * 7
            per____month = per____week * 4
            per____year = per____month * 12
            ranu = open("Per__Day.txt", "a")
            ranu.write(f" \n > Per Week : {money_mtype}{per____week} ")
            ranu.write(f" \n > Per Month : {Money_Type}{per____month}")
            ranu.write(f" \n > Per Year : {Money_Type}{per____year} ")
            ranu.close()
            au = open("per_day.txt", "a")
            au.write(f" \n > Per Day : {price} ")
            au.close()
            rafaa = open("per_week.txt", "a")
            rafaa.write(f" \n > Per week : {per____week} ")
            rafaa.close()
            rafaatedud = open("per_month.txt", "a")
            rafaatedud.write(f" \n > Per Month : {per____month} ")
            rafaatedud.close()
            fygedgsjth = open("per_year.txt", "a")
            fygedgsjth.write(f" \n > Per year : {per____year} ")
            fygedgsjth.close()
            print(f" > Per Week : {Money_Type}{per____week}")
            print(f" > Per month : {Money_Type}{per____month}")
            print(f" > Per Year : {Money_Type}{per____year}")

        elif P == "Month" or "month" or "Per month" or "per month":
            price = int(input(f" > Enter the price per one {X} of {name_Of_The_product} per Month..\n > "))
            per___week = price / 4
            per___day = per___week / 7
            per___year = price * 12
            ranug = open("Per__Month.txt", "a")
            ranug.write(f" \n > Per Day : {per___day} ")
            ranug.write(f" \n > Per Week : {per___week}")
            ranug.write(f" \n > Per Year : {per___year} ")
            ranug.close()
            aua = open("per_day.txt", "a")
            aua.write(f" \n > Per Day : {per___day} ")
            aua.close()
            rafaat = open("per_week.txt", "a")
            rafaat.write(f" \n > Per week : {per___week} ")
            rafaat.close()
            rafaatedudu = open("per_month.txt", "a")
            rafaatedudu.write(f" \n > Per Month : {price} ")
            rafaatedudu.close()
            fygedgsjthd = open("per_year.txt", "a")
            fygedgsjthd.write(f" \n > Per year : {per___year} ")
            fygedgsjthd.close()
            print(f" > Per Day : {per___day}")
            print(f" > Per Week : {per___week}")
            print(f" > Per Year : {per___year}")

        elif P == "Per week" or "Week" or "week" "per week":
            per__week = int(input(f" > Enter the price of {name_Of_The_product} per week... \n > "))
            per__day = per__week / 7
            per__month = per__week * 4
            per__year = per__month * 12
            anuga = open("Per__Wek.txt", "a")
            anuga.write(f" \n > Per Day : {per__day} ")
            anuga.write(f" \n > Per Month : {per__month}")
            anuga.write(f" \n > Per Year : {per__year} ")
            anuga.close()
            auga = open("per_day.txt", "a")
            auga.write(f" \n > Per Day : {per__day} ")
            auga.close()
            rafaaty = open("per_week.txt", "a")
            rafaaty.write(f" \n > Per Week : {per__week} ")
            rafaaty.close()
            rafaatedudue = open("per_month.txt", "a")
            rafaatedudue.write(f" \n > Per Month : {per__month} ")
            rafaatedudue.close()
            fygedgsjthdt = open("per_year.txt", "a")
            fygedgsjthdt.write(f" \n > Per year : {per__year} ")
            fygedgsjthdt.close()
            print(f" > Per Day : {per__day}")
            print(f" > Per Week : {per__month}")
            print(f" > Per Year : {per__year}")

        else:
            print(" > An error occurred")
            print(" > Please try again later")

        want_to_quit: Str = input(" > Do you want to quit ? ")
        if want_to_quit == True or "Yes" or "yes" or "Yep" or "yep":
            quit()

        elif want_to_quit == False or "No" or "no" or "Nope" or "nope":
            main_menu()

def view():
    print(" > Funtions : ")
    print(f"""
    PR = Predicted prices
    AD= Predicted amount of kg or g or Pounds
    """)
    choice: str = input(" > Enter what is your option... \n > ")
    if choice == "PR" or "pr" or "Pr" or "pR":
        print("""
	    A = Per Day
	    B = Per Week
	    C = Per Month
	    D = Per Year
	    """)
        what_is_you_choice = input(" > Enter option... \n > ")
        if what_is_you_choice == "A" or "a":
            pp = open("per_day.txt", "r")
            pp.read()
            pp.close()
        elif what_is_you_choice == "B" or "b":
            zz = open("per_week", "r")
            zz.read()
            zz.close()
        elif what_is_you_choice == "c" or "C":
            oo = open("per_month", "r")
            oo.read()
            oo.close()
        elif what_is_you_choice == "D" or "d":
            ee = open("per_year", "r")
            ee.read()
            ee.close()
        else:
            print(" > Invalid Choice")
            View()

    elif choice == "AD" or "ad" or "Ad" or "aD":
        # Where I ended
        pass
        # Should add all the months and year to a one document


def main_menu():
    print(" > Function : ")
    print(" > | - MAIN MENU - | < ")
    print("""
	 > Add = : = To calculator for Month or Day or Year
	 > Pri = : = To calculate prices
	 > Vie = : = To View the stored data
	 > qui = : = To quit the programm
	""")
    enter_choice = input(" > Enter your choice... \n > ")
    if enter_choice == "Add" or enter_choice == "add":
        add()
    elif enter_choice == "Pri" or enter_choice == "pri":
        pr()
    elif enter_choice == "Vie" or "vie":
        view()
    elif enter_choice == "quit" or "Quit" or "Qui" or "qui":
        print(" > Bye | Bye < ")
        quit()
    elif enter_choice != "quit" or "Vie" or "Pri" or "Add":
        print(f" > There is No function as {enter_choice}")
        Want_to_quit = input(" > Do yu want to quit ? ")
        if Want_to_quit == "Yes" or "yes" or True or "Yep" "yep":
            quit()
        elif Want_to_quit == "No" or "no" or "Nope" or "nope":
            main_menu()
        else:
            print(" > An error occurred")
            main_menu()
    else:
        print(F" > {enter_choice} is Not available")
        random.choices(main_menu(), quit())


main_menu()
