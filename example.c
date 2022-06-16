/* File : example.c */
 
 #include <time.h>
 double My_variable = 3.0;

// 팩토리얼 연산
 int fact(int n) {
     if (n <= 1) return 1;
     else return n*fact(n-1);
 }
 
 // 단순한 나누기 연산
 int my_mod(int x, int y) {
     return (x%y);
 }
 	

// 시간 가져오는 함수
 char *get_time()
 {
     time_t ltime;
     time(&ltime);
     return ctime(&ltime);
 }