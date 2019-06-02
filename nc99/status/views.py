from django.shortcuts import render

from .models import Server

from .minecraft_status import clean_motd, status

def index(request):
    servers = [{'server': server, 'status': status(server.ip)}
                for server in Server.objects.all()]
    for server in servers:
        if server['status']:
            server['motd'] = clean_motd(server['status'].description['text'])
    context = {'servers': servers}
    return render(request, 'status/index.html', context)
