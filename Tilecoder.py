numTilings = 8
tileWidth = 0.6
offset = 1/numTilings * tileWidth


def tilecode(in1,in2,tileIndices):

    for i in range(0, numTilings):
        index1 = int((in1 + (offset * i)) / 0.6)
        index2 = int((in2 + (offset * i)) / 0.6)
        index = index2 * 11 + index1
        tileIndices[i] = index + 121 * i
    # write your tilecoder here (5 lines or so)
    
def printTileCoderIndices(in1,in2):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,tileIndices)
    print('Tile indices for input (',in1,',',in2,') are : ', tileIndices)

#printTileCoderIndices(0.1,0.1)
#printTileCoderIndices(4.0,2.0)
#printTileCoderIndices(5.99,5.99)
#printTileCoderIndices(4.0,2.1)
