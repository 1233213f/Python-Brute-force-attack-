#!/usr/bin/env python
 # -*- coding: gbk -*-
 # -*- coding: utf_ -*-
 e = raw_input(��������Ҫ���ܵ��ַ���\n��)
 elen = len(e)
 field=[]
 for i in range(,elen):
       if(elen%i==):
         field.append(i)
 for f in field:
   b = elen / f
   result = {x:���� for x in range(b)}
   for i in range(elen):
     a = i % b;
     result.update({a:result[a] + e[i]})
   d = ����
   for i in range(b):
     d = d + result[i]
   print ����Ϊ\t��+str(f)+��\t��+����ʱ�����ܽ��Ϊ�� ��+d