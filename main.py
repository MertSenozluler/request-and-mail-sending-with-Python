# -*- coding: utf-8 -*-
from getCar import GetCar
from sendMail import SendMail
from mailData import MailData
from url import Url


# It directly reads the filter.ini file without receiving filtering information from the user. If you want to get data from the user first, user_input.py should be run first.

class CarFilter:
    def __init__(self):
        self.pageContinue = True
        self.isEmailReceived = True
        

    def run(self):
        # The page variable is incremented by 20 in each loop because when reading data from sahibinden.com, it is necessary to increment it by 20 to read the 2nd page.

        page=1
        # The numerator variable is n in the mail content. defined for editing the vehicle information section
        numerator= 0
        while self.pageContinue:
            
            # This variable is defined for checking to see if we are on the last page
            oldCarListStr = ""
            carList = []
            lists = Url().getUrl(page)        
            totalNumberOfCarsListed=0

            carList, totalNumberOfCarsListed = GetCar().getCar(lists, totalNumberOfCarsListed, carList)
            if totalNumberOfCarsListed==0:
                print("Car not found")
                self.pageContinue = False
                
            if totalNumberOfCarsListed != 0:

                if self.isEmailReceived:
                    print('*******************************************************************************')
                    email = input("Enter the email address to send to: ")
                    print('*******************************************************************************')
                    self.isEmailReceived = False

                carListStr,numerator = MailData().mailData(carList,numerator)
                sendmail = SendMail()
                sendmail.send_email(carListStr, email)
                if carListStr != oldCarListStr:
                    oldCarListStr = carListStr
                else:
                    print('*******************************************************************************')
                    print("You have reached the last page")
                    print('*******************************************************************************')
                    self.pageContinue=False
                if totalNumberOfCarsListed > 19:
                    print('*******************************************************************************')
                    continuation = input("We sent "+ str(totalNumberOfCarsListed) +" of them. Shall we send the other page? Y/N: ")
                    
                    print('*******************************************************************************')
                    if continuation=="Y" or continuation=="y":
                        self.pageContinue=True 
                        page += 20
                    else:
                        print('*******************************************************************************')
                        print("Process Terminating")        
                        print('*******************************************************************************')
                        self.pageContinue=False
                else:
                    if numerator !=  0:
                        print('*******************************************************************************')
                        print("We sent "+str(numerator)+" of them. No other vehicles were found. The process is terminating.")
                        print('*******************************************************************************')
                        self.pageContinue = False

if __name__ == "__main__":
    carFilter = CarFilter()
    carFilter.run()

    