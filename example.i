/* example.i */
 %module example
 %{
 /* 헤더파일과 함수들을 이곳에 넣어주도록 하자. */
 extern double My_variable;
 extern int fact(int n);
 extern int my_mod(int x, int y);
 extern char *get_time();
 %}
 
 extern double My_variable;
 extern int fact(int n);
 extern int my_mod(int x, int y);
 extern char *get_time();