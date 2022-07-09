#include <stdio.h>
int main(){
	int arr[10]={1,10,5,8,7,6,4,3,2,9};

	for(int i=0;i<9;i++){
		for(int j=i+1;j<10;j++){
			if(arr[i]>arr[j]){
				int tmp=arr[i];
				arr[i]=arr[j];
				arr[j]=tmp;
			}
		}
	}

	for(int i=0;i<10;i++){
		printf("%d ",arr[i]);
	}
}