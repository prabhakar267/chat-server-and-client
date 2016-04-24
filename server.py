# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-04-24 16:40:30
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-04-24 18:22:15

# Get the list sockets which are ready to be read through select
read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

