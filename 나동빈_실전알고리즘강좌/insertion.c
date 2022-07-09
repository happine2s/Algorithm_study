#include <stdio.h>
int main(){
	int arr[10]={1,10,5,8,7,6,4,3,2,9};

	for(int i=1;i<10;i++){
		int tmp=arr[i];
		for(int j=i-1;j>-1;j--){
			if(arr[j]>tmp){
				int a=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=a;
			}
		}
	}
	
	for(int i=0;i<10;i++){
		printf("%d ",arr[i]);
	}
}