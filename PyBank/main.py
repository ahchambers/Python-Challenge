import os
import csv

#Create an empty list for revenue changes outside for loop
revenue_changes=[]

#Open file
csv_path=os.path.join("Resources", "budget_data.csv")
with open (csv_path) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=',')
    next(csv_reader, None)

    #Create file with no header
    line=next(csv_reader, None)

    #Set variables 
    total_month=0
    revenue=float(line[1])
    greatest_increase=revenue
    greatest_decrease=revenue
    months=[]
    total_revenue=0
    revenue_change=0
    previous_revenue=0
    sum_revenue_change=0
    av_revenue_change=0

    #Loop through each row and calculate summary info
    for row in csv_reader:
        total_month=total_month+1
        months.append(row[0])
        total_revenue=total_revenue+revenue
        revenue=float(row[1])
        
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
summary=(
f"Financial Analysis\n"
f"--------------------------\n"
f"Total months: {(total_month)}\n"
f"Total: {(total_revenue)}\n"
f"Average Change: ${(av_revenue_change)}\n"
f"Greatest Increase in Profits: {(max_month)} (${(greatest_increase)})\n"
f"Greatest Decrease in Profits: {(min_month)} (${(greatest_decrease)})\n"
)

#Save to file
file_to_output=os.path.join("Analysis", "Budget_Analysis.txt")
print(summary)
with open(file_to_output, "w") as txt_file:
    txt_file.write(summary)

