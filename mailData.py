# -*- coding: utf-8 -*-
# data to be sent by e-mail

class MailData:
    def mailData(self,carList,numerator):
        carListStr = ""
        
        for numerator, arac in enumerate(carList, start=numerator+1):
            carListStr += f"{numerator}. Car Information:\n"
            carListStr += f"\tModel Name: {arac['modelName']}\n"
            carListStr += f"\tModel Detail: {arac['modelDetails']}\n"
            carListStr += f"\tYear: {arac['year']}\n"
            carListStr += f"\tKilometer: {arac['mileage']}\n"
            carListStr += f"\tColor: {arac['color']}\n"
            carListStr += f"\tPrice: {arac['price']}\n\n"
        return carListStr,numerator    