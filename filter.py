#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Author D4RK5H4D0W5
G='\033[0;32m';C='\033[0;36m';W='\033[0;37m';R='\033[0;31m';Y='\033[0;33m'
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')
#os.system('cls' if os.name == 'nt' else 'clear')
all=[]
c=0
ah=raw_input('Input file: ')
file=open(ah).read().splitlines()
for site in file:
        try:
#               site=a.split('/')[0]+'//'+a.split('/')[2]
                c+=1
#               print '\r'+site
                if site in all:continue
                else:all.append(site);open('filter_'+ah,'a+').write(site+'\n')
                sys.stdout.write('\r%s[%sFILTER%s] %s/%s OK:%s'%(W,R,W,c,len(file),len(all)))
                sys.stdout.flush()
        except:continue
print '\nDone saved in filter_'+ah
