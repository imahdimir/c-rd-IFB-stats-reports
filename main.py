"""

    """

import pandas as pd
from githubdata import GithubData


class GDUrl :
    src = 'https://github.com/imahdimir/rd-IFB-stats-reports'

gu = GDUrl()

class Constant :
    mn = 'نام نوع بازار'

cte = Constant()

def find_sub_table(df) :
    pass

def main() :
    pass

    ##
    # 1. Get data from Github
    gd_src = GithubData(gu.src)
    gd_src.overwriting_clone()

    ##
    fp = '/Users/mahdi/Dropbox/PycharmProjects/c-rd-IFB-stats-reports/rd-IFB-stats-reports/data/15951.xlsx'
    df = pd.read_excel(fp , header = None)

    ##
    # 2. Find sub-tables
    df['c'] = df[0].eq(cte.mn)
    inds = df[df['c']].index[2]
    st = inds - 2


    ##

    ##

##
if __name__ == "__main__" :
    main()

##
# noinspection PyUnreachableCode
if False :
    pass

    ##


    ##


    ##

##
