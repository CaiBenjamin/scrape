from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import pc_parts
from collections import defaultdict

def view_part(request, part_name):
    quantity = defaultdict(int)
    data = pc_parts.objects.all()
  
    for d in data: 
        model = d  
        d = d.pub_date
        if(model.part_name == part_name):
            print(d)
            if(d.find('2021',0,len(d)) != - 1):
                pass
            else:
                if(d[2:5] == 'Dec'):
                    quantity[12]+=1
                if(d[2:5] == 'Nov'):
                    quantity[11]+=1
                if(d[2:5] == 'Oct'):
                    quantity[10]+=1
                if(d[2:6] == 'Sept'):
                    quantity[9]+=1
                if(d[2:5] == 'Aug'):
                    quantity[8]+=1
                if(d[2:6] == 'July'):
                    quantity[7]+=1
                if(d[2:6] == 'June'):
                    quantity[6]+=1
                if(d[2:5] == 'May'):
                    quantity[5]+=1
                if(d[2:7] == 'April'):
                    quantity[4]+=1
                if(d[2:7] == 'March'):
                    quantity[3]+=1
                if(d[2:5] == 'Feb'):
                    quantity[2]+=1
                if(d[2:5] == 'Jan'):
                    quantity[1]+=1
    
    store = []
    for i in range(1,13):
        store.append(quantity[i])
    
    #find unique strings
    unique_cpu_names = set()
    for i in data:
        unique_cpu_names.add(i.part_name)

    unique_cpu_names = list(unique_cpu_names)
    unique_cpu_names.sort()

    with_underscore = []

    for i in unique_cpu_names:
        with_underscore.append(i.replace("_", " "))

    tuple_list = []
    for i in range(len(unique_cpu_names)):
        tuple = (unique_cpu_names[i], with_underscore[i])
        tuple_list.append(tuple)

    ####
    return render(request, 'scrape/graph.html', {
        'data': store,
        'tuple_list': tuple_list,
        'title' : part_name
    })


    ####


def index(request):
    # that part to quantity
    # quantity = defaultdict(int)
    # data = pc_parts.objects.all()
    # for d in data:  
    #     d = d.pub_date
    #     if(d.find('2021',0,len(d)) != - 1):
    #         pass
    #     else:
    #         # print("ASDFASFDASDFASDFASDFASDF")
    #         if(d[2:5] == 'Dec'):
    #             quantity[12]+=1
    #         if(d[2:5] == 'Nov'):
    #             quantity[11]+=1
    #         if(d[2:5] == 'Oct'):
    #             quantity[10]+=1
    #         if(d[2:6] == 'Sept'):
    #             quantity[9]+=1
    #         if(d[2:5] == 'Aug'):
    #             quantity[8]+=1
    #         if(d[2:6] == 'July'):
    #             quantity[7]+=1
    #         if(d[2:6] == 'June'):
    #             quantity[6]+=1
    #         if(d[2:5] == 'May'):
    #             quantity[5]+=1
    #         if(d[2:7] == 'April'):
    #             quantity[4]+=1
    #         if(d[2:7] == 'March'):
    #             quantity[3]+=1
    #         if(d[2:5] == 'Feb'):
    #             quantity[2]+=1
    #         if(d[2:5] == 'Jan'):
    #             quantity[1]+=1

    # store = []
    # for i in range(1,13):
    #     store.append(quantity[i])
    
    # print(store)

    # #find unique strings
    # unique_cpu_names = set()
    # for i in data:
    #     unique_cpu_names.add(i.part_name)

    # unique_cpu_names = list(unique_cpu_names)
    # unique_cpu_names.sort()
    # print(unique_cpu_names)

    return render(request, 'scrape/graph.html', {
        'data': store,
        'pc_parts': unique_cpu_names 
        
    })