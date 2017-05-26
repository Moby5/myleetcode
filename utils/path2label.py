#!/usr/bin/env python
# coding=utf-8

import pandas as pd

def path2label(path='./dy1905', fname='output.xlsx'):

    fnames = [os.path.join(path, fname) for fname in os.listdir(path)]
    df = pd.DataFrame()
    df['imgId'] = fnames

    df['ans'] = ['']*len(fnames)
    df[u'抽查'] = ['']*len(fnames)
    df['idx'] = df['imgId'].apply(lambda x: int(x.split('/')[-1][2:].split('.')[0]))
    df.sort_values(inplace=True, by='idx') # 按id排序
    df.drop(['idx'], axis=1, inplace=True)
    print df.head()
    # df.to_excel(u'to_label_dy1905.xlsx', index=None)
    df.to_excel(fname, index=None)
