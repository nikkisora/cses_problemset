#include <iostream>
#include <string>
#include <cstdint>

int vis[7][7] = {0};
std::string s;
int ans = 0;

bool isOk(int x, int y){
    return x >= 0 && y >= 0 && x <= 6 && y <= 6 && !(vis[x][y]==1);
}

int Path(int step, int x, int y){
    
    if(step == s.length()){
        if(x==6 && y==0) ans++;
        else return 0;
    }
    if(x==6 && y==0) return 0;
    
    vis[x][y] = 1;

    if(s[step] == '?' || s[step] == 'L'){
        if(isOk(x+1, y) && !(!isOk(x+2, y) && isOk(x+1, y+1) && isOk(x+1, y-1)))
            Path(step+1, x+1, y);
    }
    if(s[step] == '?' || s[step] == 'R'){
        if(isOk(x-1, y) && !(!isOk(x-2, y) && isOk(x-1, y+1) && isOk(x-1, y-1)))
            Path(step+1, x-1, y);
    }
    if(s[step] == '?' || s[step] == 'U'){
        if(isOk(x, y+1) && !(!isOk(x, y+2) && isOk(x+1, y+1) && isOk(x-1, y+1)))
            Path(step+1, x, y+1);
    }
    if(s[step] == '?' || s[step] == 'D'){
        if(isOk(x, y-1) && !(!isOk(x, y-2) && isOk(x+1, y-1) && isOk(x-1, y-1)))
            Path(step+1, x, y-1);
    }
    
    vis[x][y] = 0;
}

int main(){
    std::cin >> s;
    Path(0, 6, 6);
    std::cout << ans << std::endl;
}