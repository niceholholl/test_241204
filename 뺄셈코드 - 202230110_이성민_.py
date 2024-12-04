# -*- coding: utf-8 -*-
"""뺄셈코드 - 202230110 이성민 .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18y2DAGZHPArOVQj_UE37iHspiVycbEXp

# 1. 이진법 빼기 코드 subtract(a,b) 을 작성하라. 이 함수는 십진수 a, b 를 받고, 이를 이진법으로 변환한 후, 두 수 a-b 를 수행하여  이진법의 수로 반환한다. 계산 과정에서는 1의 보수를 만드는 함수 xor(a, len(b)) 를 사용하도록 한다. 이 함수는 a 를 b 와 길이가 같은 1의 보수로 만들며, 3-5와 같은 계산도 가능해야함. 이를 모듈로 임포트하여 3-5를 계산하여보라. (팀별 각 함수 담당자 선정 후, 모듈화 함께 이해하여 발표 준비)
"""

def transform(N,n) : # 십진수로 나타내진 N을 n진수로 변환하는 함수 (n ~ 16진수까지 가능)
  a = '0123456789ABCDEF' # n진수로 나타내기 위한 수 0~F(16진수)
  result = '' # 결과 초기값
  while N > 0 : # while
    r = N%n # N을 나타내고 싶은 진수 n으로 나눈 나머지
    result = a[r] + result # a의 순서에 따른 값 result에 추가
    N = N//n # N의 몫으로 N 반복 ~ while
  return result

def xor(a,length) : # 이진수 a의 길이를 length에 맞게 맞춰줌(0추가) ~ 이진수로 변환된 a와 b를 받음 (a와 b는 문자열)
  a = '0' * (length - len(a)) + a # 먼저 a의 앞에 length 길이를 맞추기 위한 0 추가
  complement = '' # 1의보수 초기값
  for i in a : # a의 값을 차례대로 넣어서 0인 경우 1로, 1인 경우 0으로 complement에 추가
    if i == '0' :
      complement += '1'
    elif i == '1' :
      complement += '0'
  return complement

def additive_binary(a,b) : # 이진수 a와 이진수 b를 더해서 이진수의 값으로 나타내주는 함수

  a = a[::-1] # 일의 자리부터 덧셈을 하기 위해 이진수 a,b를 뒤집어서 나열
  b = b[::-1]
  result = [] # 결과 초기값
  carry = 0 # 1+1 = 0, 1+1+1 = 1 이 되는 이진법 계산에서의 올림수

  for i in range(max(len(a),len(b))) : # 이진수 a와 b 중 길이가 긴걸 range로 받음 ~ if 사용해서 차례대로 작은 경우만 추가되도록 설정
    sum_ab = carry # 업데이트된 carry를 추가

    if i < len(a) : # len보다 작은 경우 a의 i번째 값을 추가
      sum_ab += int(a[i]) # a와 b가 이진수로 나타내진 str ~ 계산을 위해 int로 변경

    if i < len(b) : # 위와 동일
      sum_ab += int(b[i])

    result.append(str(sum_ab % 2)) # 차례대로 올림수 + a[i] + b[i] 의 나머지 ~ result에 추가
    carry = sum_ab // 2 # 올림수는 몫 ~ 업데이트

  if carry : # 마지막에 올림수가 생긴 경우 1+1+(올림수) 이런 경우를 대비하여 1을 마지막에 추가되도록 설정
    result.append(str(carry))

  result = ''.join(result[::-1]) # 뒤집어서 나열된 결과값을 다시 뒤집어서 도출

  return result

def subtract(a,b) : # 십진수 a,b를 받아 이진수로 변경하고, a-b를 1의 보수를 활용한 이진법으로 나타내주는 하는 함수
  am = transform(a,2) # 이진법으로 나열된 a ~ str
  bm = transform(b,2) # 이진법으로 나열된 b ~ str
  length = max(len(am), len(bm)) # am 와 bm 중 길이가 큰 값의 len ~ length
  bm_complement = xor(bm, length) # bm의 1의 보수 -> xor함수 사용
  result = additive_binary(am,bm_complement) # 첫번째 result는 am 과 bm의 1의 보수를 더한 값으로 만듦 -> 이진법더하기 additive_binary사용

  if len(result) == length : # result에 캐리가 발생하지 않는 경우 ~ 1.양수 2.음수
    result = xor(result,length) # 1.양수 ~ result의 1의 보수를 취해줌 -> xor함수 사용
    if a < b : # 2. 음수 ~ result의 1의 보수에 음수기호 붙여줌 -> xor함수 사용
      result = '-' + str(int(result))

  if len(result) > length : # result에 캐리가 발생하는 경우 ~ result의 길이가 length보다 큰 경우, result의 캐리를 구분하여 2^0의 자리에 추가
    n = result[1:] # 캐리가 없는 부분 result[1:]
    result = additive_binary(n,'1') # result[1:] + 1(이진수) -> 이진법더하기 additive_binary사용

  return str(int(result)) # 앞에 나열된 0을 없애기 위해 str(int(000110))=110 이런식으로 사용