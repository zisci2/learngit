#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author：zsw time:2020-6-25

import spider
from multiprocessing import Pool


if __name__ =='__main__':
    po = Pool(10)
    for i in range(1,100001):
        po.apply_async(spider.save,(i,))

    print("-----star----")
    po.close()
    po.join()
    print("-----end-----")


