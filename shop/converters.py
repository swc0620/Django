class FourDigitYearConverter:
    regex = r'\d{4}' #정규표현식, 정수값이 4회 반복됨을 의미

    def to_python(self, value):
        return int(value) #self에 어떤 값이 넘어오면 value로 return해 준다.

    def to_url(self, value):
        return '%04d' % value #4자리 수로 변환하되, 4자리에 미치지 못하면 앞에 0을 추가하여 4자리로 맞춤