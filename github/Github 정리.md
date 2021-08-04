#  Github 정리

---





## Git 저장소

git init 

로컬 파일에서 git bash를 실행한 다음 명령어 입력 



### 원격 저장소

github에서 repository 생성하기

repository의 주소 복사 



 git remote add origin 주소~ 

명령어 입력 - 원격저장소와 연결 



git remote -v 

원격 저장소 확인 



git remote add <단축이름> <url>

한 로컬 저장소는 여러 개의 원격 저장소를 가질 수 있다. 



git remote remove origin

원격 저장소 삭제 



---



### 원격 저장소에  자료 올리기(push)

git status

상태 확인



git add . 

바뀐 것을 전부 첨가



git commit -m '메세지내용'

메세지 내용과 함께 커밋



git push origin master

원격 저장소에 연결 





### 원격 저장소에서 자료 다운받기 (pull)

git pull origin master

원격저장소에 파일들을 땡겨온다.







----

## 브런치 이용하기



### 원격 저장소 내용 받아오기

1. git stash
2. git pull origin master
3. git stash pop



1. git status로 이상있는 파일 있는지 확인

- both modified가 있을 경우 해당 파일 켜서 문제점 해결

  <<<<<<< HEAD 충돌유발- new_branch (pull로 받아온거)

  충돌유발- master (폴더내에 있던거)

  master

- git add .

- git commit

- git status로 재 확인

git rm -r --cached . git add .

git commit -m "Fix untracked files





### 원격저장소에 데이터 보내기

1. git checkout -b '브랜치이름'   --- 생성하면서 이동한다.
2. git add . (staging area로) 전송된다.
3. git commit -m '커밋메세지'   (커밋, 스냅샷, 버전을 새롭게 만듬)
4. git push origin '브랜치 이름' (원격저장소에 보내기)
5. git checkout master (마스터로 이동한다.)
6. git merge 브랜치이름 : 브랜치를 병합한다. (master로 병합된다.)
7. git branch : 브랜치 삭제되었나 목록을 확인한다.



### 깃허브에서 할 일

1. pull request 보내기 (문제 사항이 있나 없나 꼭 확인한다)
2. merge 하기
3. 브랜치 삭제하기



## 기타 명령어

git status : 깃의 현재 상태를 확인

git config -- global -l : 깃 전체 글로벌 옵션을 확인

git config --global user.name '이름' : 이름 설정

git config --global user.email '메일' : 메일 설정

git remote rm origin : 원격저장소 삭제













