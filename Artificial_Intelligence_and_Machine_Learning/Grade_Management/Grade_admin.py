# 성적 관리 프로그램

# 입력 과정을 함수로 만들어서 호출
def input_student():
    list_st = [] # 학생 한명의 정보를 저장할 리스트
    
    print("종료하려면 학번에 '0'을 입력하세요.")
    print("학번을 입력하세요.")
    list_st.append(int(input("학번: ")))
    if list_st[0] == 0: # 학번이 0이면 종료
        return 0
    # 순서대로 이름, 국어, 영어, 수학 점수를 입력받음
    list_st.append(input("이름을 입력하세요."))
    list_st.append(int(input("국어 점수를 입력하세요.")))
    list_st.append(int(input("영어 점수를 입력하세요.")))
    list_st.append(int(input("수학 점수를 입력하세요.")))
    
    # 입력받은 값으로 총점, 평균을 계산하고 학점을 부여
    list_st.append(list_st[2] + list_st[3] + list_st[4])
    list_st.append(list_st[5] / 3)
    if list_st[6] >= 90:
        list_st.append('A')
    elif list_st[6] >= 80:
        list_st.append('B')
    elif list_st[6] >= 70:
        list_st.append('C')
    elif list_st[6] >= 60:
        list_st.append('D')
    else:
        list_st.append('F')
    return list_st

if __name__ == '__main__':
    
    lst = []  # 학생 전체의 정보를 저장할 리스트
    while True:        
        list_st = input_student() # 학생 한명의 정보를 입력받음
        if list_st == 0: # 학번이 0이면 종료
            break
        lst.append(list_st) # 한명의 정보를 전체 리스트에 추가

    # 학생들의 정보를 파일에 저장하기 위해 파일 객체를 생성
    infile = open('C:/Users/User/Desktop/인공지능과 기계학습/code/class_0404/Grade.txt', 'w') 
    
    # 출력
    print('='*60)
    print("학번\t이름\t국어\t영어\t수학\t총점\t평균\t학점")
    print('='*60)
    for st in lst:
        # 파일에 학생 각각의 정보를 저장
        infile.write("%d\t%s\t%d\t%d\t%d\t%d\t%.1f\t%s\n" % (st[0], st[1], st[2], st[3], st[4], st[5], st[6], st[7]))     
        # 화면에 학생 각각의 정보를 출력   
        print("%d\t%s\t%d\t%d\t%d\t%d\t%.1f\t%s" % (st[0], st[1], st[2], st[3], st[4], st[5], st[6], st[7]))
        
    print('='*60)  
    infile.close()  # 파일을 닫음        
    