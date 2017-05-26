#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#

from math import radians, cos, sin, asin, sqrt
from math import pi as PI
import math
pi = PI * 3000.0 / 180.0


def haversine(lng1, lat1, lng2, lat2):
    """
	计算地球上两点之间的距离
	:param lng1:
	:param lat1:
	:param lng2:
	:param lat2:
	:return:
	"""
    lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])  # 将十进制度数转化为弧度

    # haversine公式
    dlng = lng2 - lng1


    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r * 1000



def point_move(lng,lat,dis,direction):
	"""
	点位移
	:param lng: 经度
	:param lat: 纬度
	:param dis: 位移距离  米
	:param direction: 位移方向 e:东 w:西 s:南 n:北
	:return: 位移后点的经纬度 (经度, 纬度)
	"""
	lng_ = 0
	lat_ = 0

	if direction == 'e' or direction == 'w':
		lng_ = dis/haversine(lng, lat, lng + 0.000001, lat) * 0.000001
		if direction == 'w':
			lng_ *= -1
	else:
		lat_ = dis / haversine(lng, lat, lng, lat + 0.000001) * 0.000001
		if direction == 's':
			lat_ *= -1

	return int((lng + lng_) * 1000000) / 1000000.0, int((lat + lat_) * 1000000) / 1000000.0


def gcj02_to_bd09(gg_lon, gg_lat):
    x = gg_lon
    y = gg_lat
    z = math.sqrt(x * x + y * y) + 0.00002 * math.sin(y * pi)
    theta = math.atan2(y, x) + 0.000003 * math.cos(x * pi)
    bd_lon = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return (bd_lon, bd_lat)


def bd09_to_gcj02(bd_lon, bd_lat):
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * pi)
    gg_lon = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return (gg_lon, gg_lat)


lng_lat = (102.665696,25.045998)
dis = 1000
point_e = point_move(lng_lat[0], lng_lat[1], dis, 'e')
point_w = point_move(lng_lat[0], lng_lat[1], dis, 'w')
point_s = point_move(lng_lat[0], lng_lat[1], dis, 's')
point_n = point_move(lng_lat[0], lng_lat[1], dis, 'n')
point_ws = (point_w[0], point_s[1])
point_en = (point_e[0], point_n[1])

print( point_en )
print( point_ws )
