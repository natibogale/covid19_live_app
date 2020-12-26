from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

import requests

import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': settings.API_KEY,
    'x-rapidapi-host': settings.API_HOST
    }

response = requests.request("GET", url, headers=headers).json()
# import requests
# import json

# url = "https://covid-19-tracking.p.rapidapi.com/v1"

# headers = {
#     'x-rapidapi-key': "0b8e173dd4msh80bdf54ce2e946ap13925djsn208f3501941e",
#     'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com"
#     }

# response = requests.request("GET", url, headers=headers).json()



def home(request):
    response = requests.request("GET", url, headers=headers).json()
    results = int(response['results'])
    lists = []
    for x in range(0,results):
        lists.append(response['response'][x]['country'])
    lists.sort()
    if request.method=="POST":
        lists = []
        for x in range(0,results):
            lists.append(response['response'][x]['country'])
        lists.sort()
        print('sssssssssssssssssssssssssssssssss  ')
        selectedCountry = request.POST['selectedCountry']
        # print(selectedCountry)
        for x in range(0,results):
            if selectedCountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = response['response'][x]['deaths']['total']
        context = {'lists':lists,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}
        print(new)
        data = {
        'new' : new,
        'active' : active,
        'critical' : critical,
        'recovered' : recovered,
        'total' : total,
        'deaths' : deaths,
        'selectedCountry' : selectedCountry,
        }
        return JsonResponse(data)
        
    context = {'lists' : lists, 'response':response}
    return render(request,'index.html',context)