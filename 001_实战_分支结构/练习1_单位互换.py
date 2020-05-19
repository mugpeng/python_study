# 练习1：英制单位英寸与公制单位厘米互换。

unit = input('Your unit is inch or centimeter?(in or cm)\n')
value = float(input('Your value is?\n'))
if unit == 'in':
    cm_value = value * 2.54
    print('Your unit converts to cm, the value is %f' % cm_value)
elif unit == 'cm':
    in_value = value / 2.54
    print('Your unit converts to in, the value is %f' % in_value)
else:
    print("Error! Please input 'in' or 'cm'.")
    