#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MongoDB as db
import random
import threading
import logging

func_logger = logging.getLogger(__name__)
func_logger.setLevel(logging.INFO)
func_formatter = logging.Formatter('[%(asctime)s]:%(levelname)s:%(name)s:%(message)s')
funcfile_handler = logging.FileHandler('Mastermind.log')
funcfile_handler.setFormatter(func_formatter)
func_logger.addHandler(funcfile_handler)

class mastermind:
    def __init__(self):
        self.conn = db.DB()
        self.conn.start_conn('Name', 'Target')

    def Create_Number(self):
        digits = random.sample(range(0, 9), 4)
        number = ''.join(map(str, digits))
        return number

    def Start(self, usr, email):
        target_number = str(mastermind.Create_Number(self))
        attempt = int(0)
        sample1 = {'Name': usr, 'Email': email, 'Target': target_number,
                    'Count': attempt, 'Result': '', 'past_attempt': []}
        db.DB().insertion_mongo(self.conn.album, sample1)
        func_logger.info(f'NEWGAME,{usr},{email},{target_number}')
        return 'Bom Jogo'

    def tentativa(self, attempt_number, usr, email):
        data = mastermind.find(self, usr, email)
        target_number = data['Target']
        attempt = data['Count']
        id = data['_id']
        list = data['past_attempt']
        result = data['Result']
        if result != 'GAME OVER' and result != "VOCE VENCEU":
            list.append(attempt_number)
            result = ''
            for cont,val in enumerate(target_number):
                if val in attempt_number and val != attempt_number[cont]:
                    result += str(0)
                elif val in attempt_number and val == attempt_number[cont]:
                    result += str(1)
                else:
                    pass
            attempt += 1
            if result == '1111':
                result = "VOCE VENCEU!"
                func_logger.info(f'WIN,{usr},{email},{target_number},{list}')
            elif result != '1111' and attempt == 10:
                result = 'GAME OVER'
                func_logger.info(f'GAMEOVER,{id},{usr},{email},{target_number},{list}')
            else:
                func_logger.info(f'PLAYING,{id},{usr},{email},{target_number},{list}')

            updateprocess = threading.Thread(target=self.conn.update, args=[self.conn.album, usr, email,
                                                                            target_number, attempt, result, list])
            updateprocess.start()
        else:
            result = 'FIM DE JOGO'
            attempt = '10'

        return [result, attempt]

    def record(self):
        data = self.conn.findall(self.conn.album)
        return data

    def find(self, usr, email):
        data = self.conn.find_mongo(self.conn.album, usr, email)
        return data


if __name__ == '__main__':
    jogo = mastermind()
    print(jogo.Create_Number())
    print(jogo.Start())
    print(jogo.tentativa(4125))