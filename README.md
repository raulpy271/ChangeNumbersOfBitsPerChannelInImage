# Class that changes the amount of bits in each RGB channel of your photo

## Running

```
  $ python3 -i changeNumbersOfBitsPerChannel.py
>>> img = cv2.imread('person.jpg')
>>> img2bits = ClassForChangeNumbersOfBitsPerChannel(img, 2)
>>> img2bits.help()

In the RGB color system, one pixel can be represented by a set of three numbers that indicate the intensity of each of the three channels, each of them have the size of 8 bits. Thus, the number of possible colors is (2 ** 8) ** 3 = 16777216 .
Call the writeResults() function to see the result of your photo with 2 bits per channel, there are 64 possible colors.

>>> img2bits.writeResults('person-result.jpg')
```

## Exemples

### Original Image

![Person](https://raw.githubusercontent.com/raulpy271/ChangeNumbersOfBitsPerChannelInImage/master/person.jpg)

### 2 Bits Per Channel (64 possible colors)

![Person](https://raw.githubusercontent.com/raulpy271/ChangeNumbersOfBitsPerChannelInImage/master/person-result-2-bits.jpg)

### 1 Bit Per Channel (8 possible colors)

![Person](https://raw.githubusercontent.com/raulpy271/ChangeNumbersOfBitsPerChannelInImage/master/person-result-1-bits.jpg)

### [Image Source - this person does not exist](https://thispersondoesnotexist.com/)
