from datetime import date


def main():

    # define today's date
    y_today = int(date.today().year)
    m_today = int(date.today().month)
    d_today = int(date.today().day) 
    
    # get user input on their date of birth
    y_born = int(input('Enter year born as yyyy: \n'))
    m_born = int(input('Enter month born as mm: \n'))
    d_born = int(input('Enter day born as dd: \n'))
    
    age = calculate_age(y_today, m_today, d_today, y_born, m_born, d_born)
    if age > 50:
        print("You're old")
    elif age < 21:
        print("You're too young")
    else:
        print('Have a drink')
    
    #your main code goes here - this is where you call functions

def calculate_age(y_today, m_today, d_today, y_born, m_born, d_born):

    if m_born > m_today:
        age = y_today - y_born - 1
    elif m_born == m_today:
        if d_born > d_today:
            age = y_today - y_born - 1
        elif d_born == d_today:
            age = y_today - y_born
            print('Happy birthday!')
        else:
            age = y_today - y_born
    else:
        age = y_today - y_born
          
    return age
    

    
if __name__ == "__main__":
    main()
    