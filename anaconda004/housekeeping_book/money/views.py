import calendar    
import datetime
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
import matplotlib.pyplot as plt
import pytz
from .models import Money
from .forms import SpendingForm
from .utils import index_utils

plt.rcParams['font.family'] = 'IPAPGothic'

TODAY = str(timezone.now()).split('-')

class MainView(View):
    def get(self, request, year=TODAY[0], month=TODAY[1]):

        money = Money.objects.filter(use_date__year=year,    
                            use_date__month=month).order_by('use_date')
        total = index_utils.calc_month_pay(money)
        index_utils.format_date(money)
        form = SpendingForm()
        next_year, next_month = index_utils.get_next(year, month)
        prev_year, prev_month = index_utils.get_prev(year, month)

        context = {'year' : year,
                'month' : month,
                'prev_year' : prev_year,
                'prev_month' : prev_month,
                'next_year' : next_year,
                'next_month' : next_month,
                'money' : money,
                'total' : total,
                'form' : form
                }

        draw_graph(year, month)

        return render(request, 'money/index.html', context)

    def post(self, request, year=TODAY[0], month=TODAY[1]):
        data = request.POST
        use_date = data['use_date']
        cost = data['cost']
        detail = data['detail']
        category = data['category']
        use_date = timezone.datetime.strptime(use_date, "%Y/%m/%d")
        tokyo_timezone = pytz.timezone('Asia/Tokyo')
        use_date = tokyo_timezone.localize(use_date)
        use_date += datetime.timedelta(hours=9)

        Money.objects.create(
                use_date = use_date,
                detail = detail,
                cost = int(cost),
                category = category,
                )

        return redirect(to='/money/{}/{}'.format(year, month)) 

def draw_graph(year, month):    #追加

    money = Money.objects.filter(use_date__year=year,
            use_date__month=month).order_by('use_date')
    last_day = calendar.monthrange(int(year), int(month))[1] + 1

    day = [i for i in range(1, last_day)]
    cost = [0 for i in range(len(day))]
    for m in money:
        cost[int(str(m.use_date).split('-')[2])-1] += int(m.cost)
    plt.figure()
    plt.bar(day, cost, color='#00bfff', edgecolor='#0000ff')
    plt.grid(True)
    plt.xlim([0, 31])
    plt.xlabel('日付', fontsize=16)
    plt.ylabel('支出額(円)', fontsize=16)

    #staticフォルダの中にimagesというフォルダを用意しておきその中に入るようにしておく
    plt.savefig('money/static/images/bar_{}_{}.svg'.format(year, month),
            transparent=True)

    return None
