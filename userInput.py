# -*- coding: utf-8 -*-
import configparser
import subprocess
import os
from flask import Flask
from main import CarFilter

class UserInput:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('filter.ini', encoding='utf-8')

    def run(self):
        if 'CAR' not in self.config:
            self.config['CAR'] = {}
        self.config['CAR']['model'] = input('Model: ')
        self.config['CAR']['min_year'] = input('Min year: ')
        self.config['CAR']['max_year'] = input('Maks year: ')
        self.config['CAR']['min_price'] = input('Min fiyat: ')
        self.config['CAR']['max_price'] = input('Maks fiyat: ')
        self.config['CAR']['min_km'] = input('Min km: ')
        self.config['CAR']['max_km'] = input('Maks km: ')
        self.config['CAR']['color'] = input('Color: ')
        with open('filter.ini', 'w', encoding='utf-8') as configfile:
            self.config.write(configfile)
        print('Data has been filtered successfully')

    app = Flask(__name__)

    @app.route('/filter')
    def filterData():
        userInput = UserInput()
        userInput.run()
        main = CarFilter()
        main.run()
        

UserInput.filterData()
