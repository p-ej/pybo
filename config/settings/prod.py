from .base import *
# 서버 환경을 담당
ALLOWED_HOSTS = ['13.209.232.166']

"""
prod.py 파일에는 서버 환경에 맞게끔 ALLOWED_HOSTS 항목에 서버의 고정 아이피를 등록하였다
"""
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]