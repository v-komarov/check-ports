#coding: utf-8

import pandas as pd
import argparse
import config


SOURCE = config.SOURCE
DATA = config.DATA



### Чтение и определение активных пользовательских портов на оборудовании с привязкой к ip адресу коммутарора


class GetUserPorts():

    def __init__(self,args):
        self.infile = SOURCE+args.infile
        self.outfile = DATA+args.outfile
        self.df = pd.read_csv(self.infile, sep=";")

        print self.df.head()






def parse_args():
    parser = argparse.ArgumentParser(description='Подготовка списка пользовательских MAC адресов')
    parser.add_argument('infile', help='Название файла с исходными данными')
    parser.add_argument('outfile', help='Название файла результата')

    return parser.parse_args()



if __name__ == '__main__':

    args = parse_args()

    up = GetUserPorts(args)
    #ph.getmanageid()

