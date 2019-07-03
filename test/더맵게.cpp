#include <string>
#include <vector>
#include <algorithm> // sort ���� �˰����� ����ϱ� ���� ��� ����
#include <queue>	// �켱���� ť�� ����ϱ� ���� ��� ����
using namespace std;

int solution(vector<int> scovil, int K) { // ���ں� ������ k��
	int count = 0;	// �ͽ� Ƚ��
	int first, second;	// ���� �� �ſ� ��, �ι�°�� �� �ſ� ��
	priority_queue<int, vector<int>, greater<int>> tmp;	//�켱���� ť��  greater<int> ������������  
	for (int i = 0; i < scovil.size(); i++)
		tmp.push(scovil[i]);	// temp ť�� �Է¹��� ���ں� ������ �켱���� ť ������� Ǫ��

	while (tmp.top() < K && tmp.size() > 1) {	// �ݺ�
		count++;	// ���ں� ������ �����Ͱ� 1���� ũ�� �ͽ� Ƚ���� ��ũ����Ʈ
		first = tmp.top();	// ������������ ���ĵǾ������� ���� ���� ��
		tmp.pop();		// ù��° �� �ſ� ��
		second = tmp.top();	// �ι�° ���� ��
		tmp.pop();	// �ι�° �� �ſ� ��
		tmp.push(first + second * 2);	// �ͽ��� ���� �ٽ� Ǫ��( Ǫ���ص� �켱���� ť�� ���� �ڵ� ����)
	}
	if (tmp.top() < K)
		return -1;
	return count;
}