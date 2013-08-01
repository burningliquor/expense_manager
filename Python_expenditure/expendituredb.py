def parse(filename = "expendituredb.dat"):
    expensesdb = []
    try:
        for line in open(filename):
            line = line.strip()
            n, ca, c, q, d, p, co = line.split(";")
            rec = dict(name = n, category = ca, cost = c, quantity = q, date = d, place = p, comments = co)
            expensesdb.append(rec)
    except IOError:
        print "IOError: Could not find database '{0}'\nCreating new empty database".format(filename)
        open(filename, "w")
        print "Database '{0}' created".format(filename)
    return expensesdb

def display_report(report):
    #if len(report) is not 0 : print "name\tcategory\tcost\tdate\tcomments\n"
    for entry in report:
        print entry["name"], ":", entry["category"], ":",entry["cost"], ":", entry["quantity"], ":", entry["date"], ":", entry["place"], ":", entry["comments"],"\n",

def new_entry(n, ca, c, q, d, p, co):
    return dict(name = n, category = ca, cost = c, quantity = q, date = d, place = p, comments = co)
        
def store(report, filename = "expendituredb.dat"):
    if report == None:
        print "ERROR"
        report = []
    #else: print report, type(report)
    with open(filename, "wb") as out:
        for purchase in report:
            #print purchase
            line = "{name};{category};{cost};{quantity};{date};{place};{comments}"
            out.write(line.format(**purchase))
            out.write("\n")
      
if __name__ == '__main__':
    report = parse()
    display_report(report)
