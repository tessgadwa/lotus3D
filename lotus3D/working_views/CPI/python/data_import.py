# importing pandas package
import pandas as pandasForSortingCSV

# assign dataset
csvData = pandasForSortingCSV.read_csv('../data/data.csv')

# creating a list of column names by calling the .columns
list_of_column_names = list(csvData.columns)
column_count = len(list_of_column_names)

#for item in list_of_column_names:
    #print(item)

# displaying unsorted data frame
print("\nBefore sorting:")
print(csvData)

# sort data frame

def sortframe(sortcol):
    csvData.sort_values(sortcol,
                    axis=0,
                    ascending=[False],
                    inplace=True)

    print("\nAfter sorting:")
    print(csvData)

#sortcol = (list_of_column_names[0])
#print (sortcol)
#sortframe(sortcol)

sortedData = csvData.to_csv(index=False)

# write sorted data to new quotes file, sorted by column name defined above
sortedQuotes = open("sorteddata.csv", "w")
sortedQuotes.write(sortedData)
sortedQuotes.close()

csvData = pandasForSortingCSV.read_csv("sorteddata.csv")

rowcount = csvData.shape[0]
print("\nNumber of Rows:")
print(rowcount)

# open copy of lotus renderer source code to insert array values
lrg = open("lotus_renderer_gen.js", "w")
f1 = open("reference_js_modules/chunk1.js", "r")
lrg.write(f1.read())
f1.close()
lrg.close()

lrg = open("lotus_renderer_gen.js", "a")
#f2 = open("chunk2.js", "r")

# generate datestamp, must be customized to reflect specific content and data schema of csv
# we need some if/then logic here, but it's fussy
def datetime():
    date = str(csvData["Date"][1])
    time = str(csvData["Time"][1])

    lrg.write("var time = '")
    lrg.write(time)
    lrg.write("'\n")

    lrg.write("var date = '")
    lrg.write(date)
    lrg.write("'\n")

#datetime()

lrg.write("var time = ' '")
lrg.write("\n")

lrg.write("var date = ' '")
lrg.write("\n")
lrg.write("\n")

def readcolumn(col_name):
    for x in range(rowcount):
        lrg.write('"')
        value = str(csvData[col_name][x])
        lrg.write(value)
        lrg.write('",')

    lrg.write("]\n")

def assignColumns(col_list):
    for item in col_list:
        position = col_list.index(item)
        letter = bytes("A", 'utf-8')
        letter = letter[0] + position
        col_id = 'col_' + chr(letter)
        lrg.write('var ' + col_id + ' = [')
        readcolumn(item)
        lrg.write("\n")
        label_id = "label_" + chr(letter)
        lrg.write('var ' + label_id + ' = "' + item + '"')
        lrg.write("\n")
        lrg.write("\n")

assignColumns(list_of_column_names)

rows = str(rowcount)
lrg.write('var rowcount = ' + rows)
lrg.write("\n")

lrg.write("\n")
lrg.write('var filter1 = col_D')  #this will eventually be replaced by variable selected by user
lrg.write("\n")

lrg.write("\n")
lrg.write('var filter2 = col_E')  #this will eventually be replaced by variable selected by user
lrg.write("\n")
lrg.write("\n")

# write remaining static js code to lotus_renderer_gen
#lrg.write(f2.read())
#f2.close()

f3 = open("reference_js_modules/chunk3.js", "r")
lrg.write(f3.read())
f3.close()
lrg.close()
