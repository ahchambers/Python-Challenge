import os
import csv

#Set variables 
total_month=0

months=[]
total_revenue=0
revenue_change=0
revenue_changes=[]
previous_revenue=0
sum_revenue_change=0
av_revenue_change=0


#Open file
csv_path=os.path.join("budget_data.csv")
with open (csv_path) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=',')
    next(csv_reader, None)

    #Create file with no header
    line=next(csv_reader, None)

    revenue=float(line[1])
    greatest_increase=revenue
    greatest_decrease=revenue

    #Loop through each row and calculate summary info
    for row in csv_reader:
        total_month=total_month+1
        months.append(line[0])
        total_revenue=total_revenue+revenue

        if total_month>1:
            revenue_change=revenue-previous_revenue
            revenue_changes.append(revenue_change)
            previous_revenue=revenue

        sum_revenue_change=sum(revenue_changes)
        av_revenue_change=sum_revenue_change/(total_month)
        greatest_increase=max(revenue_changes)
        greatest_decrease=min(revenue_changes)
        max_month_index= revenue_changes.index(greatest_increase)
        min_month_index= revenue_changes.index(greatest_decrease)
        max_month=months[max_month_index]
        min_month=months[min_month_index]
    

#Print summary info
print("Financial Analysis")
print("--------------------------")
print(f"Total months: {(total_month)}")
print(f'Total: {(total_revenue)}')
print(f'Average Change: ${(av_revenue_change)}')
print(f'Greatest Increase in Profits: {(max_month)} (${(greatest_increase)})')
print(f'Greatest Decrease in Profits: {(min_month)} (${(greatest_decrease)})')