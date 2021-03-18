from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common' # 네임스페이스

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # 템플릿의 href에 실제 주소가 아니라 url 별칭 사용하려면...(name은 URL 별칭)
    # LoginView는 registration이라는 템플릿 디렉터리에서 login.html 파일을 찾는다.
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup', views.signup, name='signup'), # 회원가입 url 매핑
]