#include <stdio.h>
int main(){
	int arr[10]={1,10,5,8,7,6,4,3,2,9};

	for(int i=0;i<10;i++){
		for(int j=0;j+1<10;j++){
			if(arr[j]>arr[j+1]){
				int tmp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=tmp;
			}
		}
	}

	for(int i=0;i<10;i++){
		printf("%d ",arr[i]);
	}
}