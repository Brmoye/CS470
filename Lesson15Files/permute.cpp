#include <iostream>
#include <iomanip>
using namespace std;

void swap (int &x, int &y)
{
  int temp;
  temp = x;
  x = y;
  y = temp;
}

void printList(int list[], int size)
{
  for (int i=0; i<size; i++)
    cout << setw(3) << list[i];
  cout << endl;
} 

void permute (int list[], int k, int size)
{
  if (k==size)
    printList(list, size); 
  else
   {
     for (int i=k; i<size; i++)
      {
        swap(list[k], list[i]);
        permute(list, k+1, size); 
        swap(list[k], list[i]);
      }
   }
}

int main()
{
  int list[] = {1,2,3,4};
  permute(list,0,4);
  return 0;
}  
