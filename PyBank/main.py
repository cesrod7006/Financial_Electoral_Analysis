#Calculate months
        Months_Count += 1

        #Collect Dates 
        Dates.append(row[0])

        #Collect Profit Info and calculate total
        Profit.append(row[1])
        Total_Profits += int(row[1])
        
        #Calculate the average change in profits/loses
        final_profit=int(row[1])
        Monthly_Change_Profits = final_profit - Initial_Profits

        #Put average chane in a list 
        Monthly_Change.append(Monthly_Change_Profits)

        Change_Profits += Monthly_Change
        Initial_Profits = final_profit

        #Calculate average change in profits 
        average_change_profits=(Change_Profits/Months_Count)

        #Find Max and Min
        greatest_increase_profits = max(Monthly_Change)
        greatest_decrease_profits = min(Monthly_Change)

        increase_date = Dates[Monthly_Change.index(greatest_increase_profits)]
        decrease_date = Dates[Monthly_Change.index(greatest_decrease_profits)]

        print("----------------------------------------------------------")
        print("Financial Analysis")
        print("----------------------------------------------------------")
        print("Total Months: " + str(Months_Count))
        print("Total Profits: " + "$" + str(Total_Profits))
        print("Average Change: " + "$" + str(int(average_change_profits)))
        print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
        print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
        print("----------------------------------------------------------")
