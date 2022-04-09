from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Algorithm
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, AlgorithmSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AlgorithmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows algorithms to be viewed or edited.
    """
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    algos = Algorithm.objects.filter(sort_percentage=0, item_count=500)
    return render(request, 'site/index.html', {'algos': algos})


def sort_profile(request, pk: int):
    algo = Algorithm.objects.get(pk=pk)
    return render(request, 'site/sort_profile.html', {'algo': algo})


def ajax_algos(request, item_count, sort_percentage):
    algos = Algorithm.objects.filter(
        item_count=item_count, sort_percentage=sort_percentage)

    tbody = ""
    print(algos, len(algos))
    for algo in algos:
        tbody += '<tr>'
        # tbody += f'<td>{algo.name}</td>'
        # tbody += f'<td><p style="color: blue;" algo_name="{algo.name}" class="algo_name_link">{algo.name}</p></td>'
        tbody += f'<td><a algo_name="{algo.name}" href="/profile/{algo.pk}">{algo.name}</a></td>'
        # tbody += f'<td><div class="ui animated fade fluid basic violet button algo_name_link" algo_name="{algo.name}" tabindex="0">'
        tbody += f'<div class="visible content">{algo.name}</div>'
        tbody += f'<div class="hidden content">Посмотреть код</div>'
        tbody += f'</div></td>'

        tbody += f'<td>{algo.type}</td>'
        tbody += f'<td>{algo.complexity}</td>'
        tbody += f'<td>{algo.time}</td>'
        tbody += f'<td>{algo.iter_count}</td>'
        tbody += f'<td>{algo.replacements_count}</td>'
        tbody += f'<td>{algo.code_lines_count}</td>'
        tbody += '</tr>'

    print(tbody)

    table = f"""
    <tbody>
        <tr>
            {tbody}
        </tr>
    </tbody>
    """

    response = {
        'table': table
    }

    return JsonResponse(response)


def ajax_algos_code(request, algo_name: str):
    algo = Algorithm.objects.filter(
        name=algo_name).first()

    """
    '<div class="content" id="modal-content"><p>' +
                'Выбранный сервер: ' + response.server_name + '<br>' +
                'Цена: ' + response.price + '₽/месяц<br>' +
                response.text + 
                '<div class="ui divider"></div>' +
                '<div class="ui warning message">' +
                '<i class="warning icon"></i>' + 
                'Дальнейшее проведение заказа осуществляется через Telegram, ' + 
                'где вы можете в удобной форме уточнить особенности и возможности сервера, ' + 
                'заказать дополнительные услуги, а также получать техподдержку в течение периода работы сервера.' + 
                '</div></p></div>'
    
    """

    card = f"""
<div class="ui fluid card">
    <div class="content">
        <h2 class="header">Алгоритм сортировки «{algo_name}»</h2>
        <a class="ui violet ribbon label">{algo.item_count} элементов<br>{algo.sort_percentage}% отсортировано</a>
        <div class="ui top right attached label">Code</div>
        
        <div class="scrollable content"><pre><code class="python">{algo.code}</code></pre></div>
        <script>hljs.highlightAll();</script>
        <p>
        </p>
    </div>
</div>

"""

    basement = (
        '<div class="content" id="modal-content">'
        ''
        f'{card}'

        '</div>'
    )

    modal_content = f"""
    <tbody>
        <tr>
            
        </tr>
    </tbody>
    """

    response = {
        'modal_content': basement
    }

    return JsonResponse(response)
