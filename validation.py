from django.views.generic.edit import CreateView
from django.contrib import messages#メッセージフレームワーク

from myapp.models import MyModel

class MyCreateView(CreateView):
    model=MyModel
    def form_valid(self,form):
        #フォームが送信される（バリデーションが通った時）
        message.success(self.request,"保存しました")
        return super().form_valid(form)
    
    def form_invalid(self,form)
    #失敗したとき
    message.warning(self.request,"保存できませんでした")
    return super().form_invalid(form)
    #super()=継承元(CreateView)を呼び出すときに使う

html
{& if messages %}
<ul class="message">
    <% for message in messages %}
    <li{% if message.tags %} class="{{message.tags}}"{% end if %}>{{message}}</li>
    {% endfor %}
</ul>
{% endif %}

#メッセージレベル（＝メッセージのカテゴリやタイプを示すもの）
debug(開発用に使う)
info(通常情報通知)
success(ユーザのアクションが成功したとき)
warning(ユーザーのアクションで問題は起こらなかったが注意喚起する時)
error(ユーザーのアクションが成功しなかったとき)

