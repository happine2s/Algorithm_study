#include <stdio.h>
int arr[10]={1,5,10,8,7,6,4,3,2,9};
int num=10;

void print(){
	for(int i=0;i<10;i++){
		printf("%d ",arr[i]);
	}
}

void quick(int *arr, int l, int r){
	int pivot=l;
	int i=pivot,j,tmp;
	if(l<r){
		for(j=i+1;j<=r;j++){
			if(arr[pivot]>arr[j]){
				i++; //피벗보다 작으면 왼쪽, 크면 오른쪽으로 교체
					 //i는 피벗보다 작아서 교체 못한 j를 기억->i++ 후 큰 수와 교체 위함
				tmp=arr[i];
				arr[i]=arr[j];
				arr[j]=tmp;
			}
		}
		tmp=arr[pivot];
		arr[pivot]=arr[i];
		arr[i]=tmp;

		pivot=i; //피벗을 기준으로 2분할하여 다시 퀵 정렬
		quick(arr,l,pivot-1);
		quick(arr,pivot+1,r);
	}
	else{
		return;
	}
}

int main(){
	quick(arr,0,num-1);
	print();
}