#!/usr/bin/python
# -*- coding: utf-8 -*-

def now():
	print('2016-12-05')
f = now
print(f)
print(f())
print(now.__name__)
print(f.__name__)

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
@log
def now():
	print('2016-12-06')
print(now())
print(now.__name__)

def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
@log('execute')
def now():
	print('2016-12-07')
print(now())
print(now.__name__)

def log(func):
	def wrapper(*args, **kw):
		print('begin call.')
		# result = func(*args, **kw)
		func(*args, **kw)
		print('end call.')
		# return  result
	return wrapper
@log
def now():
	print('2016-12-08')
print(now())
print(now.__name__)

import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
