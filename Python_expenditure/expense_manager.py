balance_initial = 216327.54
from expendituredb import parse, new_entry, store, display_report
def add_entry():
    report = parse()
    n = raw_input("Enter Name : ")
    ca = raw_input("Enter Category : ")
    c = raw_input("Enter Cost : ")
    q = raw_input("Enter Quantity : ")
    d = raw_input("Enter Date : ")
    p = raw_input("Enter Place : ")    
    co = raw_input("Enter Comments : ")
    #print new_entry(n, ca, c, d, co)    
    report.append(new_entry(n, ca, c, q, d, p, co))
    #print report
    store(report)

def sort_expenses(report, attribute = "date"):
    report_total = {}
    attribute_total = []
    total = 0
    grand_total = 0
    for entry in report:
        for key, value in entry.viewitems():
            if key == attribute:
                try : report_total[value].append(entry)
                except KeyError:
                    report_total[value] = []
                    report_total[value].append(entry)
                    break
    for key, value in report_total.viewitems():
        for entry in value:
            for entry_attribute, amount in entry.viewitems():
                if entry_attribute == attribute: total += float(entry["cost"])
        attribute_total.append((key, total))
        grand_total += total
        print key, " : ", total, "current balance : ", balance_initial - grand_total        
        total = 0
    print "Grand Total : ", grand_total
    print "Initial Balance : ", balance_initial
    print "Final Balance : ", balance_initial - grand_total
    
if __name__ == '__main__':
    #add_entry()
    display_report(parse())
    sort_expenses(parse(), "date")
    
    
