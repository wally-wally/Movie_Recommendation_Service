# PJT_Final - 영화추천 서비스 구현

## 프로젝트 소개

- Django와 AWS 이용한 웹사이트 제작

## 팀원 정보 및 개발 분담 내역

- 김기은
  - App-account 기능 구현 및 Design
- 심규현
  - App-movie 기능 구현 및 Design
- 이가경
  - API Crawling 및 기타 Design

## 목표 서비스 및 실제 구현 정도

### 로그인/회원가입 페이지

- 구현 목표
  - 기본 로그인/회원가입 기능과 Social Login 3가지(Kakao, Naver, Google)
- 실제 구현
  - 기본 로그인/회원가입 기능과 Kakao 로그인 구현

### 회원 정보 페이지/기능

- 구현 목표
  - 회원정보 수정, 비번 변경, 로그아웃, 회원탈퇴, 프로필 사진 수정 기능
- 실제 구현
  - 프로필 사진을 제외한 나머지 기능 구현

### 유저 목록 페이지

- 구현 목표
  - 유저들의 영향력(댓글 수, 팔로워 수) 등에 따른 계급별 유저 나열 및 추천 유저 표시
- 실제 구현
  - 단순 유저 목록 나열

### 유저 상세 페이지

- 구현 목표
  - 영화별로 작성한 댓글과 평점 표시
  - `좋아요`한 영화 표시
  - 팔로워/팔로잉 정보와 해당 유저들 리스트 보기
- 실제 구현
  - 영화별 댓글, 평점 및 좋아요한 영화 표시
  - 팔로워/팔로잉 숫자 표시

### 영화 리스트 페이지

- 구현 목표
  - 장르별 영화 표시
- 실제 구현
  - 장르 구별 없이 모든 영화 표시

### 영화 추천 알고리즘

- 구현 목표
  - user가 누른 좋아요와 리뷰의 평점을 종합하여 영화 추천
- 실제 구현
  - 신규 유저의 경우 영화 DB 중 랜덤으로 3개의 영화 추천
  - 기존 유저의 경우 가장 최근에 `좋아요` 누른 영화의 장르 중에서 3개의 영화 추천

### 영화 상세 페이지/기능

- 구현 목표
  - 영화 상세 정보 표시, 댓글 작성 및 표시, 좋아요 기능
- 실제 구현
  - 구현 목표 기능 달성
  - 주요 출연진 표시
  - 영화 관련 유튜브 동영상 표시 기능

### 개발일지

- 2019.11.22 ~ 2019.11.25
  - DB 추출
  - 기본 기능 구현

![image](https://user-images.githubusercontent.com/52814897/69780366-6d306c00-11ee-11ea-977a-f47638d3ac88.png)

- 2019.11.26 ~ 2019.11.28
  - 세부 디자인 추가 및 수정
  - 추가 기능 구현

![image](https://user-images.githubusercontent.com/52814897/69780550-efb92b80-11ee-11ea-9fce-9ca3c3df1a67.png)

## ERD

![KKK-Triple-K](https://user-images.githubusercontent.com/52814897/69778411-8c77cb00-11e7-11ea-8d21-180972c77c3c.png)

## 핵심 기능

- 영화 추천 알고리즘
- 관련 유튜브 동영상 표시
- Naver Search

## 배포 서버 URL

### Movie Service

- http://triple-k.prgypar4mi.ap-northeast-2.elasticbeanstalk.com

## 시행 착오

### Github Conflict

- 문제
  - 3명의 팀원이 github merge 과정에서 나타나는 충돌 문제가 자주 발생
- 해결
  - 명확한 역할 분담과 지속적인 소통을 통한 변수명 및 url 주소 일치

### DB Crawling Error 처리

- 문제

  1. 추출하고자 하는 데이터가 null일 경우 에러 발생

     ![KKK-Triple-K](https://trello-attachments.s3.amazonaws.com/5ddb8fe7dbe90818f1abd7af/422x314/5922450ee44acfa2518a11bb9cfd0c36/null.PNG.png)

  2. 5명의 출연진만 뽑을 때, 출연진이 5명 이하일 경우 Index out of range 에러 발생

     ![KKK-Triple-K](https://trello-attachments.s3.amazonaws.com/5ddb8fe7dbe90818f1abd7af/363x89/f8ec6fc32527b8d87d70d92aab636c35/out_of_index_error.PNG.png)

- 해결

  1. 조건문을 통해 데이터의 값이 null일 경우 빈리스트 처리

     ![KKK-Triple-K](https://trello-attachments.s3.amazonaws.com/5ddb8fe7dbe90818f1abd7af/789x81/c8f221ec704648cb25f75cd4694f5500/null_solution.PNG.png)

  2. try / excpet 구문을 통해 index 에러 발생시 for문 종료

     ![KKK-Triple-K](https://trello-attachments.s3.amazonaws.com/5ddb8fe7dbe90818f1abd7af/205x351/e0136a87015a6409021bfe875a0d7441/out_of_solution.PNG.png)

  

### Youtube Key 가리기

- 문제
  - Youtube Secret Key가 코드 내부에 나타나지 않게 처리 필요
- 해결
  - `movies` folder > `static` 폴더 생성 > `movies` 폴더 생성 > `js` 폴더 생성 > `config.js` 파일 생성
  - `const config = { YOUTUBE_API_KEY : 'abcdefg' }`
  - 원래는 `dotenv` 라는 외부 라이브러리르 써야하는데 이는 node.js라는 외부 백엔드 프레임워크를 사용할 때만 가능하다.
  - 그래서 static 파일로 `config.js` 파일을 만들어서 그 안에 API KEY를 선언해고 template에서 `load static`을 이용해서 static 파일을 불러와서 사용해야 한다.

###  배포시 Dumpdata Error

- 문제
  - Loaddata시 기존에 사용하던 `Django 2.2.5`에서는 발생하지 않던 foreign key 문제가 배포시 사용하는 `Django 2.1.1`버전에서 발생
- 해결
  - 하나로 통합하였던 seed data를 분리하고, dumpdata시 `--natural-foreign` 옵션을 추가하여 에러 해결

## 느낀점

