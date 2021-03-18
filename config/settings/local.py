from .base import *
# 개발 환경을 담당
ALLOWED_HOSTS = []

"""
개발 환경에 맞게끔 ALLOWED_HOSTS 항목을 비워 놓았다. 
from .base import * 는 base.py 파일의 모든 내용을 사용한다는 의미이다.
 즉, local.py 파일의 내용은 base.py 파일과 동일하지만 ALLOWED_HOSTS만 다르게 설정하겠다는 의미이다.
"""