#include <string>
#include <vector>
#include <algorithm> // sort 정렬 알고리즘을 사용하기 위한 헤더 파일
#include <queue>	// 우선순위 큐를 사용하기 위한 헤더 파일
using namespace std;

int solution(vector<int> scovil, int K) { // 스코빌 지수와 k값
	int count = 0;	// 믹스 횟수
	int first, second;	// 가장 덜 매운 맛, 두번째로 덜 매운 맛
	priority_queue<int, vector<int>, greater<int>> tmp;	//우선순위 큐를  greater<int> 오름차순으로  
	for (int i = 0; i < scovil.size(); i++)
		tmp.push(scovil[i]);	// temp 큐에 입력받은 스코빌 지수를 우선순위 큐 방식으로 푸쉬

	while (tmp.top() < K && tmp.size() > 1) {	// 반복
		count++;	// 스코빌 지수의 데이터가 1보다 크면 믹스 횟수를 인크리먼트
		first = tmp.top();	// 오름차순으로 정렬되어있으니 가장 작은 값
		tmp.pop();		// 첫번째 덜 매운 맛
		second = tmp.top();	// 두번째 작은 값
		tmp.pop();	// 두번째 덜 매운 맛
		tmp.push(first + second * 2);	// 믹스된 값을 다시 푸쉬( 푸쉬해도 우선순위 큐에 의해 자동 정렬)
	}
	if (tmp.top() < K)
		return -1;
	return count;
}