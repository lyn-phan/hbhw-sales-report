# """Generate sales report showing total melons each salesperson sold."""


# salespeople = []
# melons_sold = []

# f = open('sales-report.txt')
# # opens sales report that contains salesperson's name, total amt of 
# # the order and total number of melons sold
# for line in f:
#     # loop through each line in the sales report (each transaction)
#     line = line.rstrip()
#     # removes the white space in each line
#     entries = line.split('|')
#     # splits string by this characer "|" and labels it as entries

#     salesperson = entries[0]
#     # the first index is the name of the salesperson
#     melons = int(entries[2])
#     # the last index is how many melons were sold in that transaction, 
#     # and it is converted to an integer

#     if salesperson in salespeople:
#         # if the name of the salesperson is in the list of salespeople,
#         position = salespeople.index(salesperson)
#         # finds the index of the salesperson in the list of salespeople 
#         # and assigns it to the variable 'position'

#         melons_sold[position] += melons
#         # add in the number of melons sold to the corresponding index of 
#         # where we're tracking the salesperson's qty of sold melons
#     else:
#         salespeople.append(salesperson)
#         # add the salesperson to the salespeople list
#         melons_sold.append(melons)
#         # add the number of melons they sold to the list of melons_sold


# for i in range(len(salespeople)):
#     # looping through the index of the salespeople list
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')
#     # prints out a list of all salespeople and their corresponding melon
#     # count of sales

# refactored code

def produce_sales_report(filename):

    melon_sales_to_date = {}
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            salesperson, profit_made, melons_sold = line.split("|")
            
            if salesperson in melon_sales_to_date:
                melon_sales_to_date[salesperson] += int(melons_sold)
            else:
                melon_sales_to_date[salesperson] = int(melons_sold)

    return melon_sales_to_date

def print_sales_report(melons_sold_by_sales):
    for salesperson, melons_sold in melons_sold_by_sales.items():
        print(f'{salesperson} sold {melons_sold} melons')

print_sales_report(produce_sales_report('sales-report.txt'))


# for i in range(len(salespeople)):
#     # looping through the index of the salespeople list
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')
#     # prints out a list of all salespeople and their corresponding melon
#     # count of sales
