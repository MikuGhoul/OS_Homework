#include <iostream>
#include <vector>
#include <string>

std::vector<int> _ANS_THREAD;
std::vector<bool> _FINISH;
std::vector<std::vector<int>> MAX = { { 7,5,3 },{ 3,2,2 },{ 9,0,2 },{ 2,2,2 },{ 4,3,3 } };
std::vector<std::vector<int>> Allocation = { { 0,1,0 },{ 2,0,0 },{ 3,0,2 },{ 2,1,1 },{ 0,0,2 } };
std::vector<int> Available = { 3,3,2 };
std::vector<std::vector<int>> Need;
std::vector<int> Work;
int sum = 0, source_num;
void dfs(const int & runned_thread, const int & all_thread, const int & first_thread)
{
	if (runned_thread == all_thread) {
		std::cout << "Option " << ++sum << ": ";
		for (const auto &_ans : _ANS_THREAD)
			std::cout << _ans;
		std::cout << std::endl;
		return;
	}

	for (int i = 0; i != all_thread; ++i) {
		if (_FINISH[i])
			continue;

		bool flag = true;

		for (int j = 0; j != source_num; ++j)
			if (Need[i][j] > Work[j])
				{ flag = false; break; }
		if (!flag)
			continue;
		// �ҵ�һ����������need��finish���̣߳����� Work
		for (int j = 0; j != source_num; ++j)
			Work[j] += Allocation[i][j];
		_FINISH[i] = true;
		_ANS_THREAD.push_back(i);
		
		dfs(runned_thread + 1, all_thread, first_thread);

		// dfs���ݻ���
		_ANS_THREAD.pop_back();
		for (int j = 0; j != source_num; ++j)
			Work[j] -= Allocation[i][j];
		_FINISH[i] = false;
	}
}
int main(int argc, char *argv[])
{
	/// calc Need
	std::vector<std::vector<int>>::iterator max_begin = MAX.begin();	// Question
	std::vector<std::vector<int>>::iterator allocation_begin = Allocation.begin();
	for (; max_begin != MAX.end() && allocation_begin != Allocation.end(); ++max_begin, ++allocation_begin) {
		std::vector<int>::iterator _max_begin = (*max_begin).begin();
		std::vector<int>::iterator _allocation_begin = (*allocation_begin).begin();
		std::vector<int> temp;
		for (; _max_begin != (*max_begin).end() && _allocation_begin != (*allocation_begin).end(); ++_max_begin, ++_allocation_begin)
			temp.push_back(*_max_begin - *_allocation_begin);
		Need.push_back(temp);
	}

	/// input thread and request list
	int thread, request_num; source_num = Available.size(); std::vector<int> Request;
	std::cout << "P0/P1/P2/P3/P4\nChoose a thread: (Example: 4)" << std::endl;
	std::cin >> thread;
	std::cout << "\nInput a request list: (Example: 1, 4, 7)" << std::endl;
	for (int i = 0; i != source_num; ++i) {
		std::cin >> request_num;
		Request.push_back(request_num);
	}

	/// banker_algorithm
	// step 1
	for (int i = 0; i != source_num; ++i) {
		if (Request[i] <= Need[thread][i]) continue;
		std::cout << "Request Error. Request source num >= Need source num" << std::endl;
		return 0;
	}

	// step 2
	for (int i = 0; i != source_num; ++i) {
		if (Request[i] <= Available[i]) continue;
		std::cout << "Request Waiting. Request source num >= Available source num." << std::endl;
		return 0;
	}

	// step 3
	for (int i = 0; i != source_num; ++i) {
		Available[i] -= Request[i];
		Allocation[thread][i] += Request[i];
		Need[thread][i] -= Request[i];
	}

	// step 4
	Work = Available;
	for (int i = 0; i != MAX.size(); ++i)
		_FINISH.push_back(false);
	_ANS_THREAD.push_back(thread);	// ���еİ�ȫ���ж��������thread��ʼ
	_FINISH[thread] = true;
	for (int i = 0; i != source_num; ++i)
		Work[i] += Allocation[thread][i];

	dfs(1, MAX.size(), thread);
	return 0;
}