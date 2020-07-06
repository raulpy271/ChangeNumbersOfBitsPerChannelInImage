import cv2

class ClassForChangeNumbersOfBitsPerChannel:

    """class that changes the amount of bits in each RGB channel of your photo"""

    def __init__ (self, image, newBitsPerChannel):
        self.image = image
        self.height = image.shape[0]
        self.width = image.shape[1]
        self.defaultDirectory2Save = '/home/raul/Pictures/test-result3.jpg'
        self.initialBitsPerChannel = 8
        self.initialValuesPerChannel = 2 ** self.initialBitsPerChannel 
        self.newBitsPerChannel = newBitsPerChannel 
        self.newValuesPerChannel = 2 ** self.newBitsPerChannel 
        self.dic = self.makeDicForConvertIntensity()

    
    def help(self):
        print("\nIn the RGB color system, one pixel can be represented by a set of three numbers that indicate the intensity of each of the three channels, each of them have the size of 8 bits. Thus, the number of possible colors is (2 ** 8) ** 3 = " + str((2**8)**3) + " .\nCall the writeResults() function to see the result of your photo with " + str(self.newBitsPerChannel) + " bits per channel, there are " + str((2 ** self.newBitsPerChannel) ** 3) + " possible colors.\n")


    def makeDicForConvertIntensity(self):
        dic = {}
        interval = int(self.initialValuesPerChannel / self.newValuesPerChannel)  
        for i in range(0,self.initialValuesPerChannel ,interval ):
            for j in range(i, i+interval ):
                dic[j] = i
        return dic


    def convertIntensity256ValuestToNewValues(self, value):
        return self.dic[value]


    def convertPixel256ValuesToNewValues(self, pixel):
        new_pixel = []
        for i in range(len(pixel)):
            new_pixel.append(self.convertIntensity256ValuestToNewValues(pixel[i]))
        return new_pixel


    def convertAllPixels256ValuesToNewValues(self):
        for i in range(self.height):
            for j in range(self.width):
                self.image[i, j] = self.convertPixel256ValuesToNewValues(self.image[i, j])


    def writeResults(self, directory):
        self.convertAllPixels256ValuesToNewValues()
        cv2.imwrite(directory, self.image)


    def writeResultsInDefaultDirectory(self):
        self.writeResults(self.defaultDirectory2Save)


