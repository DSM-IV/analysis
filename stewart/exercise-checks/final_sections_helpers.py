"""Translate explanatory labels embedded in math for the final three sections."""
import re
LABELS={
' constant':' 상수',' east':' 동쪽',' north':' 북쪽',' northeast':' 북동쪽',' south':' 남쪽',' west':' 서쪽',
' hypotenuse ':' 빗변 ',' person height ':' 사람 높이 ',' shadow ':' 그림자 ',' vertical ':' 수직 ',
'(right-triangle legs)':'(직각삼각형의 두 직각변)','(rising)':'(상승할 때)','approach speed':'접근 속력','diamond side':'야구장 한 변','distance from light':'조명에서의 거리','horizontal separation':'수평 간격','light-wall distance':'조명과 벽 사이 거리','minute-hand length':'분침 길이','person height':'사람 높이','pool width':'수영장 폭','pulley height':'도르래 높이','pulley height above bow':'뱃머리 위 도르래 높이','right triangle: horizontal ':'직각삼각형: 수평 ','rope length':'밧줄 길이','seconds since woman starts':'여자 출발 후 시간(초)','similar triangles: lamp height ':'닮은 삼각형: 가로등 높이 ','sphere with radius ':'구의 반지름 ','surface length':'수면 길이',
' concave down':' 위로 볼록',' decreasing':' 감소','(b) both overestimates':'(b) 둘 다 과대추정','(b) both underestimates':'(b) 둘 다 과소추정','all branches: ':'전체 가지: ','exact: ':'정확한 값: ',
'(rough graph estimate)':'(그래프에 의한 대략적인 추정)','by complementary-angle substitution':'여각 치환에 의해','first integral':'첫째 적분','first integrand odd':'첫째 적분함수는 기함수','second integral':'둘째 적분',
}
def localize(book):
 def convert(t):return re.sub(r'\\text\{([^}]*)\}',lambda m:r'\text{'+LABELS.get(m[1],m[1])+'}',t)
 for e in book.E.values():
  for key in ['statement','hint','steps','answer','check']:
   v=e[key]['ko'];e[key]['ko']=[convert(t)for t in v]if isinstance(v,list)else convert(v)
