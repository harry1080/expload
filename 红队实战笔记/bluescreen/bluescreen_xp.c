#include <windows.h>
int main(){
	HWINSTA hWinSta;
	hWinSta = CreateWindowStation("abc123", NULL, 55, NULL);
	SetHandleInformation(hWinSta, HANDLE_FLAG_PROTECT_FROM_CLOSE, HANDLE_FLAG_PROTECT_FROM_CLOSE);
	CloseWindowStation(hWinSta); 
	return 0;
}
