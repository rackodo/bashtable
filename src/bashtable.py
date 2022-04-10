corners = ["\u2554", "\u2557", "\u255a", "\u255d"]
edgeH = "\u2550"
thinEdgeH = "\u2500"
edgeV = "\u2551"
thinEdgeV = "\u2502"
splits = ["\u2566", "\u2563", "\u2560", "\u2569", "\u253c"]
thinSplits = ["\u252c", "\u2524", "\u251c", "\u2534", "\u253c"]

class bashtable:
    """
    A standard bashtable.
    """
    def __init__(self):
        self.data = []

    def setData(self, row, *data):
        """
        Sets the data for the table.
        """
        data = list(data)
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
        SplitX = splits[4]
        ThinSplitU = thinSplits[0]
        ThinSplitR = thinSplits[1]
        ThinSplitL = thinSplits[2]
        ThinSplitD = thinSplits[3]
        ThinSplitX = thinSplits[4]

        # Do some math to get important variables.
        numRows = len(self.data)
        numCols = max([len(i) for i in self.data])
        totalLength = 0
        for i in range(numRows):
            if sum([len(str(j)) for j in self.data[i]]) > totalLength:
                totalLength = sum([len(str(j)) for j in self.data[i]])
        totalLength += numCols * 2

        colLengths = []
        for i in range(numCols):
            colLengths.append(0)
            candidates = []
            for j in range(numRows):
                try:
                    candidates.append(len(self.data[j][i]))
                except IndexError:
                    candidates.append(0)
                colLengths[i] = max(candidates)

        # Print the top part of the table.
        top = CornerTL
        for i in range(len(colLengths)):
            top += EdgeH * (colLengths[i] + 2)
            if i < len(colLengths) - 1:
                top += SplitU
            else:
                top += CornerTR
        print(top)

        # Print rows.
        for i in range(numRows):
            rows = []
            rowText = EdgeV
            for j in range(numCols):
                try:
                    rowText += " " + self.data[i][j] + (" " * (colLengths[j] - len(self.data[i][j]))) + " "
                except IndexError:
                    rowText += " " + (" " * colLengths[j]) + " "
                if j < numCols - 1:
                    rowText += ThinEdgeV
                else:
                    rowText += EdgeV
            print(rowText)
            if i < numRows - 1:
                split = SplitL
                for i in range(len(colLengths)):
                    split += ThinEdgeH * (colLengths[i] + 2)
                    if i < len(colLengths) - 1:
                        split += ThinSplitX
                    else:
                        split += SplitR
                print(split)

        # Print the bottom part of the table.
        bottom = CornerBL
        for i in range(len(colLengths)):
            bottom += EdgeH * (colLengths[i] + 2)
            if i < len(colLengths) - 1:
                bottom += SplitD
            else:
                bottom += CornerBR
        print(bottom)