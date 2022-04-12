phonenumber = input('Введите номер\n')
codes = ['25', '29', '33', '44', '17']
if phonenumber.startswith('+375') and \
    len(phonenumber) == 13 and \
    phonenumber[1:].isdigit() and \
    phonenumber[4:6] in codes:
    print('Phone number is valid!')
else:
    print('Phone number is not correct!')