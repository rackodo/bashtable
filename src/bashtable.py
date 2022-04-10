corners = ["\u2554", "\u2557", "\u255a", "\u255d"]
edgeH = "\u2550"
thinEdgeH = "\u2500"
edgeV = "\u2551"
thinEdgeV = "\u2502"
splits = ["\u2566", "\u2563", "\u2560", "\u2569"]

class bashtable:
    """
    A standard bashtable.
    """
    def __init__(self):
        self.data = []

    def setData(self, row = 0, data = ""):
        """
        Sets the data for the table.
        """
        row += 1

        oldData = []
        oldData.extend(self.data)

        self.data.extend(["" for x in range((row - len(oldData) - 2))])
        self.data.append(data)


    def draw(self):
        """
        Draws the bashtable.
        """
        CornerTL = corners[0]
        CornerTR = corners[1]
        CornerBL = corners[2]
        CornerBR = corners[3]
        EdgeH = edgeH
        ThinEdgeH = thinEdgeH
        EdgeV = edgeV
        ThinEdgeV = thinEdgeV
        SplitU = splits[0]
        SplitR = splits[1]
        SplitL = splits[2]
        SplitD = splits[3]

        # Do some math to get important variables.
        maxDataLength = max(len(self.data[x]) for x in range(len(self.data)))

        # Print the top part of the table.
        print(CornerTL + (EdgeH * (maxDataLength + 2)) + CornerTR)

        # Print rows.
        for i in range(len(self.data)):
            print(EdgeV + " " + self.data[i] + " " + (" " * (maxDataLength - len(self.data[i]))) + EdgeV)
            pass
            if i != len(self.data) - 1:
                print(SplitL + (ThinEdgeH * (maxDataLength + 2)) + SplitR)

        # Print the bottom part of the table.
        print(CornerBL + (EdgeH * (maxDataLength + 2)) + CornerBR)

table = bashtable()
table.setData(0, "1")
table.setData(1, "2")
table.setData(5, "3")
table.setData(9, "4")
table.draw()