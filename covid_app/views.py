from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

import requests

import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "0b8e173dd4msh80bdf54ce2e946ap13925djsn208f3501941e",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
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

str = "{:,}"

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
                if response['response'][x]['cases']['new'] == None:
                    new = 0
                else:
                    new = response['response'][x]['cases']['new']
                    new = str.format(int(new))
                if response['response'][x]['cases']['active'] == None:
                    active = 0
                else:
                    active = response['response'][x]['cases']['active']
                    active = str.format(active)
                if response['response'][x]['cases']['critical'] == None:
                    critical = 0
                else:
                    critical = response['response'][x]['cases']['critical']
                    critical = str.format(critical)
                if response['response'][x]['cases']['recovered'] == None:
                    recovered = 0
                else:
                    recovered = response['response'][x]['cases']['recovered']
                    recovered = str.format(recovered)
                if response['response'][x]['cases']['total'] == None:
                    total = 0
                else:
                    total = response['response'][x]['cases']['total']
                    total = str.format(total)
                if response['response'][x]['deaths']['total'] == None:
                    deaths = 0
                else:
                    deaths = response['response'][x]['deaths']['total']
                    deaths = str.format(deaths)
                print(response['response'][x]['cases']['new'])

        context = {'lists':lists,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}
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
