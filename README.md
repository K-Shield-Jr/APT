# APT 공격 시나리오
## 1. 공격 기본 정보

+ ### 공격 대상 : R&B손해보험
+ ### 공격 이유 <br> : 회사에 등록된 개인 또는 여러 회사들의 중요 정보를 랜섬웨어로 잠그고 돈을 요구하기 위해서 공격
+ ### 공격 계획 <br> : R&B손해보험에서 주최하는 [디지털 취약 계층 서비스 아이디어 공모전](https://user-images.githubusercontent.com/66483772/149353129-008ce51a-1e93-4ec8-ad35-320c8e120a1d.png)에 참가 신청서 및 제출보고서를 이용하여 메일로 침투하는 스피어피싱을 계획


## 2. 시나리오 등장 인물
<p align="center">
  <img src="https://user-images.githubusercontent.com/66483772/149353334-699fad03-ebfa-4235-8bfe-ac1662839cca.png">
</p>

## 3. 토플로지 구성 및 세부 사항
![image](https://user-images.githubusercontent.com/66483772/149354447-db31fd72-c476-4056-9b14-1ebbfa46d0bf.png)

## 4. 시나리오 타임라인
![image](https://user-images.githubusercontent.com/66483772/149354486-9dc5fba5-ac24-4c4e-aa3e-3c1731c45488.png)

## 5. 공격에 사용할 취약점 및 랜섬웨어
+ ### 사용할 취약점 : CVE-2021-40444
  + ### Microsoft MSHTML Remote Code Execution Vulnerability <br> : Microsoft Office 365 및 Office 2019에 영향을 미치는 원격 코드 실행 취약점

+ ### 사용할 랜섬웨어 : Ransom.py 참고

## 6. 공격 시현
+ ### [공격 시현 영상(Youtube)](https://youtu.be/akB2ufK3PgI)
+ ### [01단계] R&B손해보험 공식 블로그에서 참가신청서 다운로드
![image](https://user-images.githubusercontent.com/66483772/149355035-22375552-87c0-4c45-832f-ab601f8348e0.png)

+ ### [02단계] Git에서 공격 코드를 다운 받아 Reverse Shell 생성
![image](https://user-images.githubusercontent.com/66483772/149355104-71303e31-e440-406b-b307-46a0557058af.png)

+ ### [03단계] 문서에 Reverse Shell을 추가하여 악성 문서 파일 제작
![image](https://user-images.githubusercontent.com/66483772/149355138-c0f84837-c4db-48a6-b495-398b3a171087.png)

+ ### [04단계] 공격자(최길동)가 참가신청서와 제출보고서를 김홍보의 외부 메일로 전송
![image](https://user-images.githubusercontent.com/66483772/149355207-6e734f02-2e30-4f67-98ed-866e69557ad3.png)

+ ### [05단계] 김홍보 내부 PC에서 외부 메일로 로그인한 후 파일 저장
![image](https://user-images.githubusercontent.com/66483772/149355257-9e8fe6ad-48d7-489f-ae57-3ca7ce30a9b5.png)

+ ### [06단계] 아래의 사진에서 편집 사용을 누르면 악성코드가 실행
![image](https://user-images.githubusercontent.com/66483772/149355304-ce85d657-7244-47f9-a06f-0818cc3555fb.png)

+ ### [07단계] 김홍보가 편집 사용을 누르면 공격자 PC에서 연결되었음을 확인
![image](https://user-images.githubusercontent.com/66483772/149355348-751b6e61-a25f-4de2-a004-c6c9ae80cf6c.png)

+ ### [08단계] 안전한 프로세스로 이주한 후, 피해자의 PC가 재부팅된 이후에도 <br> 미터프리터가 수행될 수 있도록 에이전트 삽입
![image](https://user-images.githubusercontent.com/66483772/149355392-1d11e6ab-0d82-41ce-a1e7-7185b189919e.png)

+ ### [09단계] run vnc 명령어를 통해 피해자 PC 화면을 실시간으로 공격자 PC에서 보기 위한 작업을 수행
![image](https://user-images.githubusercontent.com/66483772/149355441-c94ded20-454b-4fee-8d5a-1bf8750974ae.png)

+ ### [10단계] 공격자는 keyscan을 통해 김홍보의 내부 메일 계정 획득
![image](https://user-images.githubusercontent.com/66483772/149355492-6a0895c7-3d0e-4193-b73a-9c5c56ed80ad.png)

+ ### [11단계] 받은 메일함을 확인하여 보상팀의 최기밀에게 메일이 왔음을 확인하고 <br> 지켜보던 공격자가 이를 이용
![image](https://user-images.githubusercontent.com/66483772/149355534-33001e68-c3f2-4bf1-9a6a-18411acfe723.png)

+ ### [12단계] 내부 메일 계정에 접속하기 위해 내부 DNS 서버 IP 검색
  + ### mail.rnb.com의 DNS 주소를 검색해보니 2개의 IP가 나옴
  + ### mail이 붙어 있는 DNS 주소는 메일 서버로 판단하여 위의 IP 주소를 <br> DNS 주소로 판단하여 사용하기로 결정
![image](https://user-images.githubusercontent.com/66483772/149355579-9448b0cb-5317-4c5f-bee5-b2051f94d578.png)

+ ### [13단계] DNS 주소 설정 후 알아낸 정보들로 공격자 PC에서 김홍보 내부 메일 계정으로 로그인
![image](https://user-images.githubusercontent.com/66483772/149355633-d1bbed47-e34e-4d5d-bd82-3e1174e45d9c.png)

+ ### [14단계] 악성코드가 포함된 문서를 제목을 알맞게 변경한 후 첨부하여 <br> 보상팀의 최기밀이 보낸 메일에 답장
![image](https://user-images.githubusercontent.com/66483772/149355680-c16e3f80-fbb9-4a41-bdd1-e0c2ec77a1cf.png)

+ ### [15단계] 최기밀 PC에서 공격자가 보낸 메일이 도착한 것을 확인하고, 저장 후 파일 열고, <br> 편집 사용을 누르면 공격자 PC와 연결됨
![image](https://user-images.githubusercontent.com/66483772/149355717-8aeddbf5-47a1-4748-97d4-ed5a6483e361.png)

+ ### [16단계] 랜섬웨어 파일을 최기밀 PC에 업로드 후 실행
![image](https://user-images.githubusercontent.com/66483772/149355763-326c727a-7920-4a64-93d8-04cf09a18af4.png)

+ ### [17단계] 파일들이 잠긴 것을 확인
![image](https://user-images.githubusercontent.com/66483772/149355838-5fed5271-fafa-4364-9767-fe18ed0477a7.png)

![image](https://user-images.githubusercontent.com/66483772/149355854-3d8f3746-2db5-494f-90a6-bc199f6b6433.png)
