import unittest

def intToEnglish(number):
    NS = [
        {'value': 1000000000, 'str': "Billion"},
        {'value': 1000000, 'str': "Million"},
        {'value': 1000, 'str': "Thousand"},
        {'value': 100, 'str': "Hundred"},
        {'value': 90, 'str': "Ninety"},
        {'value': 80, 'str': "Eighty"},
        {'value': 70, 'str': "Seventy"},
        {'value': 60, 'str': "Sixty"},
        {'value': 50, 'str': "Fifty"},
        {'value': 40, 'str': "Forty"},
        {'value': 30, 'str': "Thirty"},
        {'value': 20, 'str': "Twenty"},
        {'value': 19, 'str': "Nineteen"},
        {'value': 18, 'str': "Eighteen"},
        {'value': 17, 'str': "Seventeen"},
        {'value': 16, 'str': "Sixteen"},
        {'value': 15, 'str': "Fifteen"},
        {'value': 14, 'str': "Fourteen"},
        {'value': 13, 'str': "Thirteen"},
        {'value': 12, 'str': "Twelve"},
        {'value': 11, 'str': "Eleven"},
        {'value': 10, 'str': "Ten"},
        {'value': 9, 'str': "Nine"},
        {'value': 8, 'str': "Eight"},
        {'value': 7, 'str': "Seven"},
        {'value': 6, 'str': "Six"},
        {'value': 5, 'str': "Five"},
        {'value': 4, 'str': "Four"},
        {'value': 3, 'str': "Three"},
        {'value': 2, 'str': "Two"},
        {'value': 1, 'str': "One"}
    ]

    result = ''
    for n in NS:
        if number >= n['value']:
            if number <= 99:
                result += n['str']
                number -= n['value']
                if number > 0:
                    result += ' '
            else:
                t = number // n['value']
                d = number % n['value']
                if d > 0:
                    return intToEnglish(t) + ' ' + n['str'] + ' ' + intToEnglish(d)
                else:
                    return intToEnglish(t) + ' ' + n['str']

    return result

print(intToEnglish(123))
print(intToEnglish(123456))
print(intToEnglish(123456789))

class TestIntToEnglish(unittest.TestCase):
    def test_intToEnglish(self):
        # Test cases for numbers less than 20
        self.assertEqual(intToEnglish(1), 'One')
        self.assertEqual(intToEnglish(2), 'Two')
        self.assertEqual(intToEnglish(11), 'Eleven')
        self.assertEqual(intToEnglish(19), 'Nineteen')
        
        # Test cases for numbers greater than 20 and less than 100
        self.assertEqual(intToEnglish(20), 'Twenty')
        self.assertEqual(intToEnglish(22), 'Twenty Two')
        self.assertEqual(intToEnglish(50), 'Fifty')
        self.assertEqual(intToEnglish(99), 'Ninety Nine')
        
        # Test cases for numbers greater than 100 and less than 1000
        self.assertEqual(intToEnglish(100), 'One Hundred')
        self.assertEqual(intToEnglish(150), 'One Hundred Fifty')
        self.assertEqual(intToEnglish(999), 'Nine Hundred Ninety Nine')
        
        # Test cases for numbers greater than 1000 and less than 1000000000
        self.assertEqual(intToEnglish(1000), 'One Thousand')
        self.assertEqual(intToEnglish(1000000), 'One Million')
        self.assertEqual(intToEnglish(1000000000), 'One Billion')

if __name__ == '__main__':
    #unittest.main()
    unittest.main(argv=[''], exit=False)