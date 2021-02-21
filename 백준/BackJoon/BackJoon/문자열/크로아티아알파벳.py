#**
# 문자열의 길이로 풀어볼 생각해보기

st = input()

for i in ['c=','c-','dz=','d-','lj','nj','s=','z=']:
    st = st.replace(i,'a')
        
print(len(st))