# #include <iostream>
# #include <algorithm>
# using namespace std;
#
# int DP[2][101][101];
# void solution(int a, int b);
# int solve(int turn, int left_a, int left_b);
#
# int main(){
#     solution(100, 100);
#     return 0;
# }
# //디피에 담는 정보가 뭐져....?
# void solution(int a, int b){
#     for (int i = 0; i < 101; i++){
#         for (int j = 0; j < 101; j++){
#             DP[0][i][j] = -1;
#             DP[1][i][j] = -1;
#         }
#     }
#     cout << solve(0, a, b);
# }
#
# int solve(int turn, int left_a, int left_b){
#     if (left_a == 0 && left_b == 0)
#     {
# //    turn = 0 은 A순서, 1은 B순서
# //    A순서에 0이면 B승리이므로 1 return, 반대면 0 return
#         return turn ^ 1;
#     }
#     int& res = DP[turn][left_a][left_b];
#     //??
#     if (res != -1)
#     {
#         return res;
#     }
#     res = turn ^ 1;
#     for (int i = 1; i <= left_a; i++)
#     {
#         res = solve(turn ^ 1, left_a - i, left_b);
#         //??
#         if (res != (turn ^ 1))
#         {
#             return res;
#         }
#     }
#     for (int i = 1; i <= left_b; i++)
#     {
#         res = solve(turn ^ 1, left_a, left_b - i);
#         if (res != (turn ^ 1))
#         {
#             return res;
#         }
#     }
#     int c = min(left_a, left_b);
#     for (int i = 1; i <= c; i++)
#     {
#         res = solve(turn ^ 1, left_a - i, left_b - i);
#         if (res != (turn ^ 1))
#         {
#             return res;
#         }
#     }
#     return res;
# }