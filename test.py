from edit_distinct import EditDistinct


ed = EditDistinct()

str1 = "coffee"
str2 = "cafe"

ed.init_table(str1, str2)

print(ed.evaluate(str1, str2, len(str1), len(str2)))
print(ed.get_table())

