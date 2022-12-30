#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iomanip>
using namespace std;
#define MAX_CITIES 100

struct City
  {
     int   id;
     double x;
     double y;
  };

class Route
  {
   private:
     int   length;
     int   path[MAX_CITIES];
     double cost;
   public:     
     void  init(int num_cities);
     void  display_path(City cities[]);
     void  find_cost(City cities[]);
     void  permute(int k, int n, City cities[], double &best_route);
  }; 

double distance (double x1, double y1, double x2, double y2);
void swap (int &x, int &y);

int main() 
{
   double best_route;
   int num_cities=0;
   Route route;   
   City cities[MAX_CITIES];

   ifstream infile("states.txt");         // the input data file;

   clock_t begintime, endtime;
   float elapsedtime=0;
   srand (time(NULL));

  infile >> num_cities;
  cout << "The number of cities: " << num_cities << endl; // display #cities

   for (int i=0; i < num_cities; i++)     // Read coordinates from data file 
    {
     infile >> cities[i].id;
     infile >> cities[i].x;
     infile >> cities[i].y;
//     cout << "City-" << cities[i].id << " has coordiates of x: "
//          << cities[i].x << " and y: " << cities[i].y << endl;
    }
   infile.close();
   


   cout << "Exhaustive Search" << endl;

   route.init(num_cities);
   best_route = INFINITY;
   
   begintime =  clock();
   route.permute(0,num_cities, cities, best_route);
   endtime =  clock();

   elapsedtime = ((float)endtime - (float)begintime) / CLOCKS_PER_SEC;
   cout << "Elapsed time is : " << elapsedtime << endl;
  
   return 0;
}

void Route::display_path(City cities[])
{
 cout << "Route is : ";
 for (int j=0; j < length; j++)
  cout << cities[path[j]].id << " ";
 cout << "Cost: " << setprecision(3) << fixed << cost << endl;
}

void Route::init(int num_cities)
{
 length = num_cities;
 for (int j=0; j<length; j++)
   path[j]=j; 
}


void Route::find_cost(City cities[])
{
  cost=0;
  for (int j=0; j < length-1; j++)
    cost += distance (cities[path[j]].x, cities[path[j]].y,
                      cities[path[j+1]].x, cities[path[j+1]].y);
  cost += distance (cities[path[length-1]].x, cities[path[length-1]].y, 
                    cities[path[0]].x, cities[path[0]].y);
}

void swap (int &x, int &y)
{
  int temp;
  temp = x;
  x = y;
  y = temp;
}


void Route::permute (int k, int n, City cities[], double &best_route)
{
  if (k==n)
    {
     find_cost(cities);
     if (cost < best_route)
       { 
         best_route = cost;
         display_path(cities);
       }
        
    }
  else
   {
     for (int i=k; i<n; i++)
      {
        swap(path[k], path[i]);
        permute(k+1, n, cities, best_route); 
        swap(path[k], path[i]);
      }
   }
}
       
double distance (double x1, double y1, double x2, double y2)
{
  return sqrt((y2-y1)*(y2-y1) + (x2-x1)*(x2-x1));
}

