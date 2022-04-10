from bashtable import bashtable

table = bashtable()
table.setColumnTitle(0, "First Name")
table.setColumnTitle(1, "Last Name")
table.setColumnTitle(2, "Age")

table.setData(0, "Bash", "Elliott", "17")
table.setData(1, "Jane", "Doe", "21")
table.setData(2, "John", "Doe", "21")
table.draw()