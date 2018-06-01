# 개인 맞춤형 블로그 구현
> #### 학습한 내용을 바탕으로 블로그를 제작합니다.

## 결과물
* [결과 사이트](http://lcwblog.ap-northeast-2.elasticbeanstalk.com)

## 목표
1. 인스타그램을 모방해 사진을 보여주는 방식의 UI로 제작한다.
2. FBV만을 사용한다.
3. 막히는 부분은 Askdjango - 기본편을 보며 해결하되, 기록으로 남긴다.
4. 기능별로 commit하며, 이번 기회를 통해 Markdown을 익힌다.
5. 최종 결과는 AWS를 이용해 배포한다.

## 프로젝트에 적용한 것들
* el_pagination - 페이지네이션
* Bootstrap3 - 모든 페이지 직접 구현
* Sentry - 에러로깅
* select_related - 쿼리셋 최적화
* django-imagekit - 썸네일 생성 및 저장
* Jquery, Javascript, Ajax - 비동기 댓글 생성 및 조회
* 환경변수를 이용한 Secret_Key 분리
* Elastic Beanstalk, S3, RDS를 이용한 배포

## 참고 사이트
1. [hannal님의 블로그](http://blog.hannal.com)
2. [askdjango](https://nomade.kr)
3. [documents](https://djangoproject.com)
4. [초보몽키님의 블로그](https://wayhome25.github.io)
5. [stackoverflow](https://stackoverflow.com)
