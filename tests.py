#!/usr/bin/python3
from push_msg import *

def test_messages_are_empty():
   assert len(messages) == 0

def test_variables_not_empty():
   assert len(url) != 0
   assert len(user) != 0
   assert len(pw) != 0
   assert len(urlpush) != 0
   assert len(token) != 0
   assert len(me) != 0

