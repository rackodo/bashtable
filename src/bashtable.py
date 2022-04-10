corners = ["\u2554", "\u2557", "\u255a", "\u255d"]
edgeH = "\u2550"
edgeV = "\u2551"
splits = ["\u2566", "\u2563", "\u2560", "\u2569"]

class bashtable:
    """
    A standard bashtable.
    """
    def __init__(self):
        self.data = ""

    def setData(self, data):
        """
        Sets the data for the table.
        """
        self.data = data

    def draw(self):
        """
        Draws the bashtable.
        """
        CornerTL = corners[0]
        CornerTR = corners[1]
        CornerBL = corners[2]
        CornerBR = corners[3]
        EdgeH = edgeH
        EdgeV = edgeV
        SplitU = splits[0]
        SplitR = splits[1]
        SplitL = splits[2]
        SplitD = splits[3]

        # Do some math to get important variables.
        dataLength = len(self.data)

        # Print the top part of the table.
        print(CornerTL + (EdgeH * (dataLength + 2)) + CornerTR)

        # Print the central part of the table.
        print(EdgeV + " " + self.data + " " + EdgeV)

        # Print the bottom part of the table.
        print(CornerBL + (EdgeH * (dataLength + 2)) + CornerBR)