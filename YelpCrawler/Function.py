import pypyodbc
from datetime import datetime, timedelta

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


def DatabaseConnectionBuilder():
    IPAddress = '140.123.174.167'
    UserName = 'kakaci123'
    PassWord = 'zaza5201314'
    DataBase = 'Yelp_ChenWei'

    connection = pypyodbc.connect('Driver={SQL Server};'
                                  'Server=' + IPAddress + ';'
                                                          'Database=' + DataBase + ';'
                                                                                   'uid=' + UserName + ';pwd=' + PassWord + '')
    return connection.cursor()


def GetAuthAndClient():
    auth = Oauth1Authenticator(
        consumer_key='_GHyOtIbZl0GCrjsQDYSwg',
        consumer_secret='WDqxsZJdKcg4BmI-bBBcfdQhNt4',
        token='EvYL_JqVpEAq0tzasuwdn_5JZ_adm59I',
        token_secret='xEvIsXujBvWEE_mYYqHaIc9olrU',
    )
    return Client(auth)


def GetTimeStamp():
    return str(datetime.now()).split(' ')[0]


def GetYesterdayTimeStamp():
    return str(datetime.now() + timedelta(days=-1)).split(' ')[0]
