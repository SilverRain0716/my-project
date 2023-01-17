#1.위치 매개변수

def my_func(a, b):
    print(a, b)

my_func(2, 3)

#가변 변수
def comment_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')
        
comment_info(name = '파린이', content = '정말 감사합니다.')

def post_info(title, content, *tags):
    print(f'제목 : {title}')
    print(f'내용 : {content}')
    print(f'태그 : {tags}')


post_info('파이썬 함수 정리!', '다양한 매개 변수 정리합니다.','#파이썬', '#함수')
    