#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:47539
@file: 2.py
@time: 2020/3/27  23:23
"""
import datetime

def week(year, month, day):
    time1 = datetime.datetime(year, month, day)
    time0 = datetime.datetime(year, 1, 1)
    today = datetime.date.isoweekday(time1)
    delta_days = (time1-time0).days
    firstday = datetime.date.isoweekday(time0)
    delta_weeks = (delta_days+firstday-1)/7 + 1
    print("是该年第%d周的周%d"%(delta_weeks, today))
    #print(today)

week(2020,3,27)

def school_week(year, month, day):
    time1 = datetime.datetime(year, month, day)
    time0 = datetime.datetime(2020, 2, 17)
    today = datetime.date.isoweekday(time1)
    delta_days = (time1-time0).days
    firstday = datetime.date.isoweekday(time0)
    delta_weeks = (delta_days+firstday-1)/7 + 1
    print("是校历第%d周的周%d"%(delta_weeks, today))

school_week(2020,3,27)
