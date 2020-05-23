// NOTE: write your custom function to test below in yourfunction()
// vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <algorithm> 
#include <chrono> 
#include <vector>
#include <iomanip>
using namespace std;
using namespace std::chrono; 
// function files
#include "isort.h"
#include "qsort.h"
int testSize = 2000;

int yourfunction(vector<int> testCase){
	auto start = high_resolution_clock::now(); 
////////////////////////////////////////////////////////
	// write function here



//////////////////////////////////////////////////////////
	auto stop = high_resolution_clock::now(); 
	auto duration = duration_cast<microseconds>(stop - start); 
	return duration.count();
}

void generateTestCase(vector<int> (&testCase)){

	for (int i=0;i<testSize;i++){
		testCase.push_back(rand()%1000);
	}

}	

void atericks(int n){
	for (int i=0; i<n; i++){
		cout<<"*";
	}
}

void graph(vector<int> y){
	cout << setw(10) << "  # of Inputs" << "               " << "Runtime (microseconds)"<<endl;
	vector<int> x;
	double max;
	for (int i=0;i<y.size();i++){
		x.push_back(i*100);
	}
	for (int i=0;i<y.size();i++){
		max = *max_element(y.begin(), y.end());
		cout<<setw(10)<<x[i];
		atericks( y[i]/(max/30) );
		cout << "     "<<y[i]<<endl;
	}

}

void menu(){
	cout<<"C # - change Test Size (default 2000)"<<endl;
	cout<<"F   - test YOUR function"<<endl;
	cout<<"I   - test insertion sort"<<endl;
	cout<<"Q   - test quick sort"<<endl;
	cout<<endl;
}

int main(){
	// (1) generate random test case
	cout << "Big - O Runtime Tester"<<endl<<endl;
	menu();
	while (true){
	vector<int> testCase;
	vector<int> y; 
	generateTestCase(testCase);

	char functionChoice;
	cin >> functionChoice;

	if (functionChoice == 'I' || functionChoice == 'i'){
		// insertion sort
		cout<<"Insertion Sort"<<endl;
		int index = 0; 
		while (index <= testSize){
			y.push_back(insertionSort(vector<int>(
			testCase.begin(),testCase.begin()+index)));
			index += 100;
		}
		graph(y);
	}else if (functionChoice == 'Q' || functionChoice == 'q'){
		// quick sort
		cout<<"Quick Sort"<<endl;
		int index = 0; 
		while (index <= testSize){
			y.push_back(quickSort(vector<int>(
			testCase.begin(),testCase.begin()+index)));
			index += 100;
		}
		graph(y);
	}else if (functionChoice == 'C' || functionChoice == 'c'){
		cin >> testSize;
		cout<<"test size changed to "<<testSize<<endl;
	}else if (functionChoice == 'M' || functionChoice == 'm'){
		menu();
	}
	else {
		// custom function
		cout<<"Custom Function"<<endl;
		int index = 0; 
		while (index <= testSize){
			y.push_back(yourfunction(vector<int>(
			testCase.begin(),testCase.begin()+index)));
			index += 100;
		}
		graph(y);
	}
	// plot graph
	
	cout << "Press M to View Menu" << endl;

	}

    return 0;
}
