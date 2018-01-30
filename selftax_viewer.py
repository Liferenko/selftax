class Income_money:
    income_money_before_tax = 0
    tax_to_my_future = 0 # TODO Add if income_money > 5000 uah then tax_to_my_future X2
    money_goes_to_mastercard = 0
    money_which_can_spend_after_next_income = 0
    money_for_this_moment = 0

    # TODO What can do this Income money?


    # TODO How to add already existing sum_block when money_for_this_moment less then sum_block

    # TODO Check if money_for_this_moment <= any of sum_blocks
    def separate_income_money_to_groups(income_money_before_tax):
        print("You money before taxing: %s" % (income_money_before_tax))
        tax_to_my_future = income_money_before_tax * 0.2
        print("Tax for your future: ", tax_to_my_future)

        money_goes_to_mastercard = income_money_before_tax * 0.4
        print("Money to your mastercard: ", money_goes_to_mastercard)

        money_which_can_spend_after_next_income = income_money_before_tax * 0.3
        print("After your next income you can spend: ", money_which_can_spend_after_next_income)

        money_for_this_moment = (( ( income_money_before_tax - tax_to_my_future) \
                                - money_goes_to_mastercard) \
                                - money_which_can_spend_after_next_income)
        print("Great job! Now you can buy something you want for this sum: ", money_for_this_moment)


income_money_before_tax = int(input("How much money you want to tax?\n"))
Income_money.separate_income_money_to_groups(income_money_before_tax)