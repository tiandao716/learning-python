# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/12/10 13:03
"""
import datetime
import random

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from app01.utils.form import OrderModelForm
from django.views.decorators.csrf import csrf_exempt


def order_list(request):
    form = OrderModelForm()
    context = {
        'form': form
    }
    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    """
    创建订单
    :param request:
    :return:
    """
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        print(form)
        """<tr>
    <th><label for="id_title">订单名称:</label></th>
    <td>
      
      <input type="text" name="title" value="qw" maxlength="32" class="form-control" placeholder="订单名称" required id="id_title">
      
      
    </td>
  </tr>

  <tr>
    <th><label for="id_price">商品价格:</label></th>
    <td>
      
      <input type="number" name="price" value="3333" class="form-control" placeholder="商品价格" required id="id_price">
      
      
    </td>
  </tr>

  <tr>
    <th><label for="id_status">订单状态:</label></th>
    <td>
      
      <select name="status" class="form-control" placeholder="订单状态" id="id_status">
  <option value="1" selected>未支付</option>

  <option value="2">已支付</option>

</select>
      
      
    </td>
  </tr>

  <tr>
    <th><label for="id_admin">管理员:</label></th>
    <td>
      
      <select name="admin" class="form-control" placeholder="管理员" required id="id_admin">
  <option value="">---------</option>

  <option value="1" selected>sunliguo</option>

  <option value="2">root</option>

</select>
      
      
        
      
    </td>
  </tr>
        
        """
        # print(type(form))
        # <class 'app01.utils.form.OrderModelForm'>
        # print(form.cleaned_data)
        # {'title': 'qw', 'price': 3333, 'status': 1, 'admin': <Admin: sunliguo>}
        form.instance.oid = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        # 保存到数据库
        form.save()
        return JsonResponse({"status": True})
        # return HttpResponse(json.dumps({"status":True}))
    else:
        return JsonResponse({'status': False, 'error': form.errors})
        '''
        error: {title: ["这个字段是必填项。"], price: ["这个字段是必填项。"], admin: ["这个字段是必填项。"]}
        status: false
        '''
