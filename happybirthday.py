from datetime import date

print('what is your name? ')
name=input()

print('what month were you born? ')
birthmonth=input()

print('hello', name)
print('the number of letters in your name are: ', len(name))

month=date.today().strftime('%B')


if birthmonth.lower()==month.lower():
    print('Happy birthday month')